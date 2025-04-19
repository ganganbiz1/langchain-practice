# Poetryの使い方ガイド

このプロジェクトでは、Pythonパッケージ管理にPoetryを使用しています。このドキュメントでは、pyenvと組み合わせたPoetryの基本的な使い方を解説します。

## Poetryとは

Poetryは依存関係管理とパッケージングを一つのツールで行うためのPythonツールです。
- 依存関係の自動管理
- 仮想環境の自動作成
- 簡単なパッケージ公開
- ロックファイルによる再現可能な環境

## 事前準備

1. [pyenvを使ったPythonのインストール](python_setup.md)が完了していること
2. プロジェクトディレクトリで `.python-version` ファイルが有効であること

## 1. Poetryのインストール

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetryへのパスを追加（初回のみ）

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### インストールの確認

```bash
poetry --version
```

## 2. プロジェクトでの基本的な使い方

### 依存関係のインストール

既存のプロジェクトの依存関係をインストールするには:

```bash
cd /path/to/langchain-practice
poetry install
```

### 仮想環境を有効化

```bash
poetry shell
```

これにより、プロジェクト専用の仮想環境が有効になります。

### 通常のコマンドをPoetry経由で実行

仮想環境を有効化せずにコマンドを実行する場合:

```bash
poetry run python script.py
poetry run uvicorn app.main:app --reload
```

### 新しいパッケージの追加

```bash
# 通常の依存関係
poetry add package-name

# 開発用の依存関係
poetry add --dev package-name
```

### 依存関係の更新

```bash
poetry update
```

特定のパッケージのみ更新する場合:

```bash
poetry update package-name
```

### 仮想環境の情報

```bash
# 仮想環境の場所を表示
poetry env info --path

# 全情報を表示
poetry env info
```

## 3. プロジェクト固有の使い方

LangChainプロジェクトでは、以下のコマンドが特に役立ちます:

### アプリケーションの実行

```bash
poetry run uvicorn app.main:app --reload
```

### サンプルスクリプトの実行

```bash
poetry run python notebooks/basic_langchain.py
```

## 4. トラブルシューティング

### 仮想環境の再作成

依存関係に問題がある場合:

```bash
# 仮想環境を削除
poetry env remove python

# 再インストール
poetry install
```

### pyenvとPoetryの連携エラー

pyenvで設定したPythonバージョンとpoetry.tomlで指定しているバージョンが一致しない場合:

```bash
# プロジェクト直下に.python-versionファイルがあることを確認
cat .python-version

# pythonのバージョン確認
python --version

# Poetryの設定を確認
poetry env info
``` 