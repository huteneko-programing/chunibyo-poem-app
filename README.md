# 厨二病ポエムアプリ 🎨

Pollinations AIを使用した複合生成アプリです。テキスト、画像、音声を同時に生成できます。

## 機能

- 📝 AIテキスト生成（Mistralモデル使用）
- 🖼 AI画像生成（Pollinations API使用）
- 🔊 AI音声合成（OpenAI Audio使用）
- 💾 プロンプト履歴の保存（SQLite使用）

## セットアップ

1. 仮想環境を作成
```bash
python3 -m venv venv
```

2. 仮想環境をアクティベート
```bash
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate  # Windows
```

3. 依存関係をインストール
```bash
pip install -r requirements.txt
```

## 実行方法

```bash
streamlit run app.py
```

## 使用方法

1. プロンプトを入力
2. 「✨ 生成！」ボタンをクリック
3. テキスト、画像、音声が同時に生成されます
4. 履歴は自動的に保存されます

## 技術スタック

- Streamlit
- Pollinations AI
- SQLite
- Python 3.9+
