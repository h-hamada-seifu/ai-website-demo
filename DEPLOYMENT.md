# デプロイメント設定ガイド

このリポジトリは、GitHub Pagesを使用して2つの環境にデプロイされます：

## 🌐 環境

### 1. 本番環境（Production）
- **URL**: `https://h-hamada-seifu.github.io/ai-website-demo/`
- **トリガー**: mainブランチへのプッシュ（HTMLまたはCSSファイルの変更時）
- **用途**: 一般公開用のウェブサイト

### 2. PRプレビュー環境（Preview）
- **URL**: `https://h-hamada-seifu.github.io/ai-website-demo/preview/pr-{PR番号}/index.html`
- **トリガー**: Pull Requestの作成・更新
- **用途**: レビュー前の確認用

## ⚙️ GitHub Pages 初期設定

初回のみ、以下の設定が必要です：

1. **リポジトリの Settings タブを開く**

2. **左メニューから「Pages」を選択**

3. **Source（ソース）設定**:
   - **Source**: `GitHub Actions` を選択
   - ⚠️ 重要: `Deploy from a branch` ではなく `GitHub Actions` を選択してください

4. **保存**

これで設定完了です！

## 🚀 デプロイフロー

### 本番デプロイ
```
PRマージ → mainブランチに反映 → GitHub Actions実行 → 本番公開
```

### PRプレビュー
```
PR作成/更新 → GitHub Actions実行 → プレビューURL生成 → PRにコメント投稿
```

## 📝 注意事項

- PRプレビューは `gh-pages` ブランチの `/preview/pr-{番号}/` ディレクトリに保存されます
- 本番環境は常に最新のmainブランチの内容が反映されます
- HTMLファイルがルートディレクトリに存在しない場合、本番デプロイでデフォルトページが生成されます

## 🔗 関連ワークフロー

- `.github/workflows/deploy_pages.yml` - 本番デプロイ
- `.github/workflows/preview_pr.yml` - PRプレビューデプロイ
- `.github/workflows/ai_generate_and_pr.yml` - AI生成とPR作成
