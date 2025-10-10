# 🤖 AI Website Generator Demo

Google Gemini APIを使って、依頼内容を入力するだけで自動的にウェブサイトを生成し、GitHub Pagesで公開できるプロジェクトです。

## 📋 目次

- [機能概要](#機能概要)
- [必要なもの](#必要なもの)
- [セットアップ手順](#セットアップ手順)
  - [1. リポジトリのFork](#1-リポジトリのfork)
  - [2. Google Gemini APIキーの取得](#2-google-gemini-apiキーの取得)
  - [3. GitHubでのシークレット設定](#3-githubでのシークレット設定)
  - [4. GitHub Pagesの設定](#4-github-pagesの設定)
  - [5. GitHub Actionsの権限設定](#5-github-actionsの権限設定)
- [使い方](#使い方)
- [仕組み](#仕組み)
- [トラブルシューティング](#トラブルシューティング)

---

## 🎯 機能概要

このプロジェクトでは以下のことができます：

1. **AIによるウェブサイト自動生成**：テーマを入力するだけで、HTML/CSSファイルが自動生成されます
2. **自動PR作成**：生成されたコードは自動的にPull Requestとして作成されます
3. **プレビュー環境**：PR作成時に自動でプレビュー用URLが生成され、確認できます
4. **本番公開**：PRをマージすると、GitHub Pagesで本番公開されます

---

## 📦 必要なもの

- GitHubアカウント
- Google Gemini APIキー（無料で取得可能）
- Webブラウザ

> **初心者の方へ**：Gitコマンドやプログラミングの知識は不要です！すべてブラウザ上で完結します。

---

## 🚀 セットアップ手順

### 1. リポジトリのFork

まず、このプロジェクトを自分のGitHubアカウントにコピー（Fork）します。

1. このリポジトリのページ右上にある **「Fork」** ボタンをクリック
2. **「Create fork」** ボタンをクリック
3. 数秒待つと、あなたのアカウントにコピーされます

<details>
<summary>📸 画面イメージ（クリックして表示）</summary>

- リポジトリページの右上に「Fork」ボタンがあります
- クリックすると確認画面が表示されるので「Create fork」を押します

</details>

---

### 2. Google Gemini APIキーの取得

Google Gemini APIは、AIがウェブサイトを生成するために必要です。無料で利用できます。

#### 手順：

1. **Google AI Studioにアクセス**
   - [https://aistudio.google.com/](https://aistudio.google.com/) を開く
   - Googleアカウントでログイン

2. **APIキーを作成**
   - 左側のメニューから **「Get API key」** をクリック
   - **「Create API key」** ボタンをクリック
   - 新しいプロジェクトを作成するか、既存のプロジェクトを選択
   - **「Create API key in new project」** を選択（新規の場合）

3. **APIキーをコピー**
   - 生成されたAPIキー（`AI...`で始まる長い文字列）をコピー
   - ⚠️ **重要**：このキーは他人に見せないでください

<details>
<summary>📸 詳しい手順（クリックして表示）</summary>

1. Google AI Studioにログイン後、左メニューの「Get API key」をクリック
2. 「Create API key」ボタンを押す
3. プロジェクトを選択（または新規作成）
4. 生成されたAPIキーの右側にあるコピーボタンをクリック

</details>

---

### 3. GitHubでのシークレット設定

取得したAPIキーを、GitHubに安全に保存します。

#### 手順：

1. **Forkしたリポジトリのページを開く**
   - `https://github.com/あなたのユーザー名/ai-website-demo`

2. **設定画面を開く**
   - リポジトリページ上部の **「Settings」** タブをクリック

3. **Secretsページに移動**
   - 左サイドバーの **「Secrets and variables」** をクリック
   - **「Actions」** を選択

4. **新しいシークレットを作成**
   - **「New repository secret」** ボタンをクリック
   - **Name（名前）**：`GEMINI_API_KEY` と入力（大文字小文字を正確に）
   - **Secret（値）**：先ほどコピーしたAPIキーを貼り付け
   - **「Add secret」** ボタンをクリック

<details>
<summary>📸 設定画面の見つけ方（クリックして表示）</summary>

```
リポジトリトップ → Settings → 左メニュー「Secrets and variables」 → Actions → New repository secret
```

Name欄に `GEMINI_API_KEY`、Value欄にAPIキーを貼り付けます。

</details>

---

### 4. GitHub Pagesの設定

生成されたウェブサイトを公開するための設定です。

#### 手順：

1. **設定画面を開く**
   - リポジトリの **「Settings」** タブをクリック

2. **Pagesページに移動**
   - 左サイドバーの **「Pages」** をクリック

3. **ソースを設定**
   - **Source（ソース）**：`Deploy from a branch` を選択
   - **Branch（ブランチ）**：`gh-pages` を選択し、フォルダは `/ (root)` を選択
   - ⚠️ 注意：`GitHub Actions`ではなく、必ず`Deploy from a branch`を選んでください

4. **保存**
   - **「Save」** ボタンをクリック

<details>
<summary>🔍 補足説明（クリックして表示）</summary>

- `gh-pages`ブランチは、GitHub Actionsが自動的に作成します
- 最初は選択肢に表示されない場合があります。その場合は、後述の「使い方」を実行した後に再度設定してください

</details>

---

### 5. GitHub Actionsの権限設定

GitHub Actionsが自動的にコードをコミット・PR作成できるようにします。

#### 手順：

1. **設定画面を開く**
   - リポジトリの **「Settings」** タブをクリック

2. **Actionsページに移動**
   - 左サイドバーの **「Actions」** をクリック
   - **「General」** を選択

3. **権限を設定**
   - **「Workflow permissions」** セクションまでスクロール
   - **「Read and write permissions」** を選択
   - **「Allow GitHub Actions to create and approve pull requests」** にチェック

4. **保存**
   - **「Save」** ボタンをクリック

---

## 🎨 使い方

セットアップが完了したら、さっそく使ってみましょう！

### ウェブサイトを生成する

1. **Actionsタブを開く**
   - Forkしたリポジトリのページ上部にある **「Actions」** タブをクリック

2. **ワークフローを選択**
   - 左サイドバーから **「1. AIコード生成とPR作成」** をクリック

3. **ワークフローを実行**
   - 右側に表示される **「Run workflow」** ボタンをクリック
   - ドロップダウンが開くので、テキストボックスに依頼内容を入力
     - 例：「カフェのウェブサイト」
     - 例：「プログラミングスクールのLP」
   - 緑色の **「Run workflow」** ボタンをクリック

4. **待つ（約1〜2分）**
   - ワークフローが実行されます
   - ページをリロードすると、実行状況が確認できます

5. **Pull Requestを確認**
   - 完了すると、自動的にPull Requestが作成されます
   - **「Pull requests」** タブに移動して確認
   - PRの中にプレビューURLが記載されているので、クリックして確認できます

6. **本番公開（オプション）**
   - 内容が良ければ、PR画面で **「Merge pull request」** をクリック
   - これで本番環境（`https://あなたのユーザー名.github.io/ai-website-demo/`）に公開されます

<details>
<summary>💡 入力例（クリックして表示）</summary>

- 「おしゃれなカフェのウェブサイトを作って」
- 「ペットショップの紹介ページ」
- 「ポートフォリオサイト、青系の配色で」

AIが依頼内容を理解して、自動的にデザインとコンテンツを生成します。

</details>

---

## ⚙️ 仕組み

### アーキテクチャ

```
依頼入力（GitHub Actions）
    ↓
Gemini APIでコード生成（generate_website.py）
    ↓
Pull Request自動作成
    ↓
プレビュー環境デプロイ（gh-pagesブランチ）
    ↓
レビュー → マージ
    ↓
本番公開（GitHub Pages）
```

### ファイル構成

- **[generate_website.py](generate_website.py)**：Gemini APIを呼び出してHTML/CSSを生成するPythonスクリプト
- **[.github/workflows/ai_generate_and_pr.yml](.github/workflows/ai_generate_and_pr.yml)**：AI生成とPR作成の自動化ワークフロー
- **[.github/workflows/preview_pr.yml](.github/workflows/preview_pr.yml)**：PR用プレビュー環境のデプロイ
- **[.github/workflows/deploy_pages.yml](.github/workflows/deploy_pages.yml)**：本番環境へのデプロイ

---

## 🛠️ トラブルシューティング

### ❌ ワークフローが失敗する

**症状**：Actions実行時にエラーが出る

**原因と対処法**：

1. **APIキーが設定されていない**
   - 「[3. GitHubでのシークレット設定](#3-githubでのシークレット設定)」を再確認
   - シークレット名が `GEMINI_API_KEY` と正確に一致しているか確認

2. **APIキーの有効期限切れ・クォータ超過**
   - Google AI Studioで新しいAPIキーを発行
   - 無料枠の使用量を確認（[https://aistudio.google.com/](https://aistudio.google.com/)）

3. **権限不足**
   - 「[5. GitHub Actionsの権限設定](#5-github-actionsの権限設定)」を再確認

### ❌ プレビューURLが404エラー

**症状**：プレビューURLにアクセスすると「404 Not Found」

**対処法**：

1. GitHub Pagesが有効化されているか確認
   - Settings → Pages で `gh-pages` ブランチが選択されているか
2. 数分待ってから再度アクセス（初回は反映に時間がかかることがあります）

### ❌ gh-pagesブランチが選択肢にない

**対処法**：

1. 一度「使い方」の手順でワークフローを実行
2. ワークフローが成功すると自動的に `gh-pages` ブランチが作成されます
3. その後、Settings → Pages で選択可能になります

---

## 📚 参考情報

- [Google AI Studio](https://aistudio.google.com/)
- [GitHub Actions ドキュメント](https://docs.github.com/ja/actions)
- [GitHub Pages ドキュメント](https://docs.github.com/ja/pages)

---

## 📄 ライセンス

このプロジェクトは自由に使用・改変できます。

---

## 🤝 貢献

バグ報告や改善提案は、Issueまたはプルリクエストでお願いします！