FROM python:3.13-slim-bookworm

WORKDIR /app

# システムの依存関係をインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Poetryをインストール
RUN pip install poetry

# 依存関係のみをインストール（プロジェクトファイルはコピーしない）
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-root

# アプリケーションのコードをコピー
COPY . .

# アプリケーションを実行
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 