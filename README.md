# 厨二病ポエムアプリ 🎨

Pollinations AIを使用した複合生成アプリです。テキスト、画像、音声を同時に生成できます。

## 機能

- 📝 AIテキスト生成（Pollinations API使用）
- 🖼 AI画像生成（Pollinations API使用）
- 🔊 AI音声合成（Pollinations API使用）
- 💾 プロンプト履歴の保存（SQLite使用）

## セットアップ

### 前提条件
- **Python 3.9.x** (推奨: 3.9.6)
- **Git** (バージョン管理用)

### 簡単セットアップ

#### macOS/Linux
```bash
# セットアップスクリプトを実行
./setup.sh
```

#### Windows
```cmd
# セットアップスクリプトを実行
setup.bat
```

### 手動セットアップ

#### 1. 仮想環境を作成

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### 2. 依存関係をインストール
```bash
pip install -r requirements.txt
```

#### 3. アプリを起動
```bash
streamlit run app.py
```

## 使用方法

1. 厨二病なプロンプトを入力
2. 「✨ 厨二病生成！」ボタンをクリック
3. テキスト、画像、音声が同時に生成されます
4. 履歴は自動的に保存されます

## 技術スタック

- Streamlit
- Pollinations API（直接呼び出し）
- SQLite
- Python 3.9+

## トラブルシューティング

### よくある問題

#### Pythonが見つからない (Windows)
PythonがPATHに追加されていない可能性があります。
[Python公式サイト](https://www.python.org/downloads/)からダウンロードして、インストール時に「Add Python to PATH」にチェックしてください。

#### 仮想環境がアクティベートされない
**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows (CMD):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

#### ライブラリのインストールエラー
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

詳細なセットアップ情報は [SETUP_GUIDE.md](SETUP_GUIDE.md) を参照してください。

## 開発ガイド

動画制作を考慮した段階的な開発手順は [DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md) を参照してください。
