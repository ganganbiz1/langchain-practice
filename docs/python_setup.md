# MacでのPython 3.13セットアップガイド（pyenv使用）

このガイドでは、M3 MacBookでpyenvを使用してPython 3.13をインストールする方法を説明します。

## 前提条件

- macOS（Monterey以上推奨）
- Homebrewがインストール済み

## 1. Homebrewのインストール（未インストールの場合）

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## 2. pyenvのインストール

```bash
brew update
brew install pyenv
```

## 3. シェル設定の更新

### Zshの場合（デフォルト）

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

設定を反映するために新しいターミナルを開くか、以下を実行します：

```bash
source ~/.zshrc
```

## 4. Pythonのビルドに必要な依存関係をインストール

```bash
brew install openssl readline sqlite3 xz zlib
```

## 5. Python 3.13のインストール

利用可能なPythonバージョンを確認します：

```bash
pyenv install --list | grep "3.13"
```

Python 3.13.0をインストールします：

```bash
pyenv install 3.13.0
```

## 6. Python 3.13をグローバルまたはローカルで設定

### グローバルに設定（システム全体）

```bash
pyenv global 3.13.0
```

### プロジェクトのディレクトリでのみ使用する場合

プロジェクトディレクトリに移動して：

```bash
cd /path/to/your/project
pyenv local 3.13.0
```

## 7. インストールの確認

```bash
python --version
```

`Python 3.13.0` と表示されれば成功です。

## 8. プロジェクトでのPoetryの使用

このプロジェクトはPoetryを使用して依存関係を管理しています。Poetryをインストールして利用するには：

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Poetryへのパスを追加：

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

プロジェクトディレクトリで依存関係をインストール：

```bash
cd /path/to/langchain-practice
poetry install
```

仮想環境を有効化（オプション）：

```bash
poetry shell
```

## トラブルシューティング

### ビルド中のエラー

ビルド中にエラーが発生した場合、Xcodeコマンドラインツールが最新であることを確認してください：

```bash
xcode-select --install
```

### SSL/TLSエラー

SSL関連のエラーが発生した場合、OpenSSLパスを明示的に指定してみてください：

```bash
CFLAGS="-I$(brew --prefix openssl)/include" \
LDFLAGS="-L$(brew --prefix openssl)/lib" \
pyenv install 3.13.0
``` 