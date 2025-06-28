# 仮想環境セットアップガイド 🐍

## 📋 前提条件

### 必要なソフトウェア
- **Python 3.9.x** (推奨: 3.9.6)
- **Git** (バージョン管理用)
- **エディタ** (VS Code, PyCharm等)

### Pythonのインストール確認
```bash
# macOS/Linux
python3 --version

# Windows
python --version
```

## 🖥️ OS別セットアップ手順

### macOS/Linux の場合

#### 1. 仮想環境の作成
```bash
# プロジェクトディレクトリに移動
cd chunibyo-poem-app

# 仮想環境を作成
python3 -m venv venv

# 仮想環境をアクティベート
source venv/bin/activate
```

#### 2. アクティベート確認
```bash
# プロンプトに(venv)が表示されることを確認
(venv) username@computer:~/chunibyo-poem-app$

# Pythonのパスを確認
which python
# 出力例: /Users/username/chunibyo-poem-app/venv/bin/python
```

### Windows の場合

#### 1. 仮想環境の作成
```cmd
# プロジェクトディレクトリに移動
cd chunibyo-poem-app

# 仮想環境を作成
python -m venv venv

# 仮想環境をアクティベート
venv\Scripts\activate
```

#### 2. PowerShell を使用する場合
```powershell
# プロジェクトディレクトリに移動
cd chunibyo-poem-app

# 仮想環境を作成
python -m venv venv

# 仮想環境をアクティベート
.\venv\Scripts\Activate.ps1
```

#### 3. アクティベート確認
```cmd
# プロンプトに(venv)が表示されることを確認
(venv) C:\Users\username\chunibyo-poem-app>

# Pythonのパスを確認
where python
# 出力例: C:\Users\username\chunibyo-poem-app\venv\Scripts\python.exe
```

## 📦 ライブラリのインストール

### バージョン固定の重要性
プロジェクトの再現性を保つため、特定のバージョンを使用します。

#### 1. 基本ライブラリのインストール
```bash
# 仮想環境がアクティベートされていることを確認
(venv) $

# 基本ライブラリをインストール
pip install streamlit==1.46.1
pip install requests==2.32.4
pip install gtts==2.5.4
```

#### 2. 依存関係の確認
```bash
# インストールされたライブラリを確認
pip list

# requirements.txtに出力
pip freeze > requirements.txt
```

#### 3. 推奨バージョン一覧
```txt
# requirements.txt の内容例
altair==5.5.0
blinker==1.9.0
cachetools==6.1.0
certifi==2025.6.15
charset-normalizer==3.4.2
click==8.1.8
exceptiongroup==1.3.0
gitdb==4.0.12
gitpython==3.1.44
gtts==2.5.4
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.10
jinja2==3.1.6
jsonschema==4.24.0
jsonschema-specifications==2025.4.1
markupsafe==3.0.2
narwhals==1.44.0
numpy==2.0.2
packaging==25.0
pandas==2.3.0
pillow==11.2.1
protobuf==6.31.1
pyarrow==20.0.0
pydeck==0.9.1
python-dateutil==2.9.0.post0
pytz==2025.2
pyyaml==6.0.1
pyzmq==26.0.2
referencing==0.36.2
requests==2.32.4
rpds-py==0.25.1
six==1.17.0
smmap==5.0.2
sniffio==1.3.1
streamlit==1.46.1
tenacity==9.1.2
toml==0.10.2
tornado==6.5.1
typing-extensions==4.14.0
tzdata==2025.2
urllib3==2.5.0
watchdog==4.0.0
```

## 🔧 トラブルシューティング

### よくある問題と解決方法

#### 1. Pythonが見つからない (Windows)
```cmd
# PythonがPATHに追加されているか確認
python --version

# 見つからない場合は、Pythonを再インストール
# https://www.python.org/downloads/ からダウンロード
# インストール時に「Add Python to PATH」にチェック
```

#### 2. 仮想環境がアクティベートされない
```bash
# macOS/Linux
source venv/bin/activate

# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# PowerShellで実行ポリシーエラーが出る場合
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 3. pipのアップグレード警告
```bash
# pipを最新版にアップグレード
pip install --upgrade pip
```

#### 4. ライブラリのインストールエラー
```bash
# キャッシュをクリアして再インストール
pip cache purge
pip install -r requirements.txt --no-cache-dir
```

## 📝 開発環境の確認

### 動作確認手順
```bash
# 1. 仮想環境がアクティベートされていることを確認
(venv) $

# 2. 必要なライブラリがインストールされていることを確認
pip list | grep streamlit
pip list | grep requests
pip list | grep gtts

# 3. アプリを起動
streamlit run app.py

# 4. ブラウザで http://localhost:8501 にアクセス
```

### 環境情報の出力
```bash
# 環境情報をファイルに出力
python -c "import sys; print(f'Python: {sys.version}')" > environment_info.txt
pip freeze >> environment_info.txt
```

## 🎯 動画制作での説明ポイント

### 各OSでの違いを説明
- **macOS/Linux**: `source venv/bin/activate`
- **Windows CMD**: `venv\Scripts\activate`
- **Windows PowerShell**: `.\venv\Scripts\Activate.ps1`

### バージョン管理の重要性
- 同じバージョンを使用することで再現性を保証
- `requirements.txt`による依存関係の管理
- チーム開発での環境統一

### トラブルシューティング
- 実際のエラーとその解決過程を見せる
- よくある問題の対処法を説明
- デバッグの基本を教える

## 📚 参考リンク

- [Python公式サイト](https://www.python.org/)
- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [venv公式ドキュメント](https://docs.python.org/3/library/venv.html)
- [pip公式ドキュメント](https://pip.pypa.io/)

このガイドに従ってセットアップすることで、どのOSでも同じ環境で開発を開始できます！ 