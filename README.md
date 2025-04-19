# LangChain Practice

このプロジェクトは、LangChainの使い方を学習するためのプロジェクトです。

## 環境構築

### Poetryを使用する場合

```bash
# 依存関係のインストール
poetry install

# 仮想環境の有効化
poetry env activate
```

### Dockerを使用する場合

```bash
# コンテナのビルドと起動
docker compose up -d
```

## 機能

- FastAPIを使用したWebアプリケーション
- LangChainを使用した自然言語処理
- ChromaDBを使用したベクトルデータベース

## 環境構築

### 前提条件

- Docker
- Docker Compose
- Python 3.13（ローカル開発の場合）
- Poetry（ローカル開発の場合）

### Docker環境でのセットアップ手順

1. リポジトリをクローン
```bash
git clone <repository-url>
cd langchain-practice
```

2. Dockerコンテナの起動（初回は時間がかかります）
```bash
docker compose up -d
```
※初回実行時はLlama 3モデル（約4GB）のダウンロードが行われるため時間がかかります

3. APIにアクセス
ブラウザで http://localhost:8000/docs にアクセスして、APIドキュメントを確認できます。

### ローカル開発環境のセットアップ（Mac）

詳細な手順については以下のドキュメントを参照してください：

- [pyenvによるPython 3.13セットアップガイド](docs/python_setup.md)
- [Poetryの使い方ガイド](docs/poetry_setup.md)

#### クイックセットアップ（既にpyenvとPoetryがインストール済みの場合）

```bash
# Pythonバージョンを設定
pyenv install 3.13.0
pyenv local 3.13.0

# 依存関係のインストール
poetry install

# アプリケーションを実行
poetry run uvicorn app.main:app --reload
```

## 基本的な使い方

1. `/ask` エンドポイントに質問を送信
```bash
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d '{"question": "LangChainとは何ですか？"}'
```

2. サンプルコードの実行
```bash
# Docker環境の場合
docker exec -it langchain-practice_app_1 python notebooks/basic_langchain.py

# ローカル環境の場合
poetry run python notebooks/basic_langchain.py
```

## 使用している技術

- **LangChain**: LLMアプリケーション開発フレームワーク
- **Ollama**: ローカルでLLMを実行するためのツール
- **Meta Llama 3**: Metaの最新の高性能な無料LLM
- **FastAPI**: 高速なWebフレームワーク
- **ChromaDB**: ベクトルデータベース
- **Poetry**: Pythonのパッケージ管理ツール
- **pyenv**: 複数のPythonバージョンを簡単に管理するツール

## プロジェクト構成

- `app/main.py`: メインのFastAPIアプリケーション
- `pyproject.toml`: Poetryの設定ファイル
- `Dockerfile`: Pythonアプリケーションのビルド設定
- `docker-compose.yml`: マルチコンテナ設定（アプリ、Ollama、ChromaDB）
- `docs/`: セットアップ関連のドキュメント
- `notebooks/`: LangChainのサンプルコード
