import os
import sys
import json
from google import genai
from pydantic import BaseModel, Field

# Pydanticを使って、AIの出力構造を定義します
# AIは必ずこの「File」のリスト形式でコードを出力するよう強制されます [2]
class File(BaseModel):
    """ウェブサイトを構成する単一のファイルを表現するモデル。"""
    filename: str = Field(..., description="ファイルの名前。例: index.html, style.css, about.html")
    content: str = Field(..., description="ファイルに書き込むソースコードの完全な内容。")

# --- メイン処理 ---
if __name__ == "__main__":
    # ワークフローから渡された依頼内容を取得
    if len(sys.argv) < 2:
        print("Error: 依頼内容が指定されていません。")
        sys.exit(1)
    
    # 依頼内容
    request_description = sys.argv[1]

    # 環境変数からAPIキーを安全に取得します [3]
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEYが環境変数に設定されていません。")
        sys.exit(1)

    # 依頼プロンプトの設計 (AIに具体的な出力を指示)
    prompt = f"""
    依頼内容: 「{request_description}」というテーマに基づき、以下の3ファイルを生成してください。
    1. index.html (メインページ)
    2. about.html (詳細ページ)
    3. style.css (共通スタイルシート)

    すべてのファイルは、モダンなデザインと、依頼内容に沿ったコンテンツを含めること。
    index.html と about.html は、<link>タグを使って style.css を外部参照するように記述すること。
    あなたの回答は、Pydanticスキーマに厳密に従い、JSON形式でのみ出力してください。
    """

    try:
        client = genai.Client()
        
        # 構造化出力の設定 [2]
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": list[File], # Fileモデルのリストとして出力
            },
        )
        
        # AIからの構造化出力をPydanticオブジェクトとしてパース
        generated_files = response.parsed

        # 生成されたファイルをディスクに書き込む
        print("--- ファイル生成開始 ---")
        for file_obj in generated_files:
            filename = file_obj.filename
            content = file_obj.content
            
            # ファイル名をチェックし、コンテンツを書き込む
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ ファイル作成: {filename}")
        
        print("--- ファイル生成完了 ---")

    except Exception as e:
        print(f"AI生成またはファイル書き込み中にエラーが発生しました: {e}")
        sys.exit(1)