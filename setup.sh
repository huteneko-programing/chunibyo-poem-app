#!/bin/bash

# 厨二病ポエムアプリ セットアップスクリプト (macOS/Linux)

echo "🎨 厨二病ポエムアプリのセットアップを開始します..."

# Pythonのバージョン確認
echo "📋 Pythonのバージョンを確認中..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python3が見つかりません。Python3をインストールしてください。"
    exit 1
fi

# 仮想環境の作成
echo "🐍 仮想環境を作成中..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ 仮想環境の作成に失敗しました。"
    exit 1
fi

# 仮想環境のアクティベート
echo "🔧 仮想環境をアクティベート中..."
source venv/bin/activate

# pipのアップグレード
echo "⬆️ pipをアップグレード中..."
pip install --upgrade pip

# ライブラリのインストール
echo "📦 必要なライブラリをインストール中..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ ライブラリのインストールに失敗しました。"
    exit 1
fi

# 環境情報の出力
echo "📝 環境情報を出力中..."
python -c "import sys; print(f'Python: {sys.version}')" > environment_info.txt
pip freeze >> environment_info.txt

echo "✅ セットアップが完了しました！"
echo ""
echo "🚀 アプリを起動するには:"
echo "   source venv/bin/activate"
echo "   streamlit run app.py"
echo ""
echo "🌐 ブラウザで http://localhost:8501 にアクセスしてください。" 