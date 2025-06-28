@echo off
REM 厨二病ポエムアプリ セットアップスクリプト (Windows)

echo 🎨 厨二病ポエムアプリのセットアップを開始します...

REM Pythonのバージョン確認
echo 📋 Pythonのバージョンを確認中...
python --version

if %errorlevel% neq 0 (
    echo ❌ Pythonが見つかりません。Pythonをインストールしてください。
    echo https://www.python.org/downloads/ からダウンロードしてください。
    pause
    exit /b 1
)

REM 仮想環境の作成
echo 🐍 仮想環境を作成中...
python -m venv venv

if %errorlevel% neq 0 (
    echo ❌ 仮想環境の作成に失敗しました。
    pause
    exit /b 1
)

REM 仮想環境のアクティベート
echo 🔧 仮想環境をアクティベート中...
call venv\Scripts\activate.bat

REM pipのアップグレード
echo ⬆️ pipをアップグレード中...
python -m pip install --upgrade pip

REM ライブラリのインストール
echo 📦 必要なライブラリをインストール中...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ ライブラリのインストールに失敗しました。
    pause
    exit /b 1
)

REM 環境情報の出力
echo 📝 環境情報を出力中...
python -c "import sys; print(f'Python: {sys.version}')" > environment_info.txt
pip freeze >> environment_info.txt

echo ✅ セットアップが完了しました！
echo.
echo 🚀 アプリを起動するには:
echo    venv\Scripts\activate
echo    streamlit run app.py
echo.
echo 🌐 ブラウザで http://localhost:8501 にアクセスしてください。
pause 