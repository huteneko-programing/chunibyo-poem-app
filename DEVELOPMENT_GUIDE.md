# 厨二病ポエムアプリ開発ガイド 🎬

YouTube動画制作を考慮した段階的な開発手順

## 📋 開発の基本方針

### 動画制作のポイント
- **1つの動画 = 1つの機能追加/改善**
- **各段階でコミットして履歴を残す**
- **実装しながら説明できるようにする**
- **視聴者が理解しやすい進捗にする**

## 🎯 開発段階の設計

### Phase 1: プロジェクト初期セットアップ (動画1)
**目標**: 基本的な開発環境の構築

#### 実装手順
1. **プロジェクト作成**
   ```bash
   mkdir chunibyo-poem-app
   cd chunibyo-poem-app
   git init
   ```

2. **仮想環境セットアップ**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **基本ライブラリインストール**
   ```bash
   pip install streamlit requests
   pip freeze > requirements.txt
   ```

4. **基本ファイル作成**
   - `README.md` (プロジェクト説明)
   - `.gitignore` (除外ファイル設定)

5. **初回コミット**
   ```bash
   git add .
   git commit -m "✨ プロジェクト初期セットアップ完了"
   ```

#### 動画での説明ポイント
- 仮想環境の重要性
- 依存関係管理の基本
- Gitの基本的な使い方

---

### Phase 2: 基本的なStreamlitアプリ作成 (動画2)
**目標**: 最小限の機能を持つアプリの作成

#### 実装手順
1. **最小限のapp.py作成**
   ```python
   import streamlit as st
   
   st.title("🎨 厨二病ポエムアプリ")
   prompt = st.text_input("プロンプトを入力してください")
   
   if st.button("生成！") and prompt:
       st.write(f"入力: {prompt}")
   ```

2. **動作確認**
   ```bash
   streamlit run app.py
   ```

3. **コミット**
   ```bash
   git add app.py
   git commit -m "📱 基本的なStreamlitアプリを作成"
   ```

#### 動画での説明ポイント
- Streamlitの基本構文
- インタラクティブな要素の追加
- アプリの起動方法

---

### Phase 3: テキスト生成機能の追加 (動画3)
**目標**: 厨二病らしいテキスト生成機能

#### 実装手順
1. **テキスト生成ロジック追加**
   ```python
   def generate_chunibyo_text(prompt):
       templates = [
           f"「{prompt}」という言葉に宿る闇の力が...",
           f"君の心に響く「{prompt}」の真意..."
       ]
       return random.choice(templates)
   ```

2. **UIに統合**
   ```python
   if st.button("✨ 厨二病生成！") and prompt:
       text = generate_chunibyo_text(prompt)
       st.success(text)
   ```

3. **コミット**
   ```bash
   git add app.py
   git commit -m "📝 厨二病テキスト生成機能を追加"
   ```

#### 動画での説明ポイント
- 関数の定義と使用方法
- ランダム選択の実装
- エラーハンドリングの基本

---

### Phase 4: 画像生成機能の追加 (動画4)
**目標**: Pollinations APIを使用した画像生成

#### 実装手順
1. **画像生成URL作成**
   ```python
   def generate_image_url(prompt):
       return f"https://image.pollinations.ai/prompt/{quote(prompt)}"
   ```

2. **UIに統合**
   ```python
   image_url = generate_image_url(prompt)
   st.image(image_url, caption="厨二病な画像生成")
   ```

3. **エラーハンドリング追加**
   ```python
   try:
       st.image(image_url, caption="厨二病な画像生成")
   except Exception as e:
       st.error(f"画像の読み込みに失敗しました: {str(e)}")
   ```

4. **コミット**
   ```bash
   git add app.py
   git commit -m "🖼 画像生成機能を追加"
   ```

#### 動画での説明ポイント
- 外部APIの使用方法
- URLエンコーディングの重要性
- エラーハンドリングの実装

---

### Phase 5: 音声合成機能の追加 (動画5)
**目標**: gTTSを使用した音声生成

#### 実装手順
1. **gTTSライブラリインストール**
   ```bash
   pip install gtts
   pip freeze > requirements.txt
   ```

2. **音声生成機能追加**
   ```python
   from gtts import gTTS
   import tempfile
   
   def generate_audio(text):
       tts = gTTS(text=text, lang='ja')
       with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
           tts.save(fp.name)
           return fp.name
   ```

3. **UIに統合**
   ```python
   audio_file = generate_audio(text)
   with open(audio_file, 'rb') as f:
       st.audio(f.read(), format='audio/mp3')
   os.unlink(audio_file)  # 一時ファイル削除
   ```

4. **コミット**
   ```bash
   git add .
   git commit -m "🎤 音声合成機能を追加"
   ```

#### 動画での説明ポイント
- 新しいライブラリの追加方法
- 一時ファイルの管理
- 音声ファイルの処理

---

### Phase 6: データベース機能の追加 (動画6)
**目標**: SQLiteを使用した履歴保存機能

#### 実装手順
1. **データベース初期化関数**
   ```python
   def init_db():
       conn = sqlite3.connect("history.db")
       c = conn.cursor()
       c.execute('''CREATE TABLE IF NOT EXISTS prompts (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       timestamp TEXT,
                       prompt TEXT,
                       result TEXT
                   )''')
       conn.commit()
       conn.close()
   ```

2. **保存・取得機能**
   ```python
   def save_prompt(prompt, result):
       conn = sqlite3.connect("history.db")
       c = conn.cursor()
       c.execute("INSERT INTO prompts (timestamp, prompt, result) VALUES (?, ?, ?)",
                 (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), prompt, result))
       conn.commit()
       conn.close()
   
   def get_history():
       conn = sqlite3.connect("history.db")
       c = conn.cursor()
       c.execute("SELECT timestamp, prompt, result FROM prompts ORDER BY id DESC LIMIT 10")
       rows = c.fetchall()
       conn.close()
       return rows
   ```

3. **UIに統合**
   ```python
   init_db()
   # 生成時に保存
   save_prompt(prompt, text)
   # 履歴表示
   for t, p, r in get_history():
       st.markdown(f"- {t} - **{p}** → {r[:50]}...")
   ```

4. **コミット**
   ```bash
   git add .
   git commit -m "💾 データベース機能を追加"
   ```

#### 動画での説明ポイント
- SQLiteの基本操作
- データベース設計の考え方
- 履歴機能の実装

---

### Phase 7: エラー処理と互換性問題の解決 (動画7)
**目標**: 実際のエラーに対処し、安定性を向上

#### 実装手順
1. **問題の特定**
   - Python 3.9でのTypeAliasエラー
   - pollinations.aiライブラリの互換性問題

2. **解決策の実装**
   ```python
   # pollinations.aiライブラリを削除
   pip uninstall pollinations.ai -y
   
   # API直接呼び出しに変更
   def generate_text(prompt):
       # 簡易版のテキスト生成
       return f"「{prompt}」という言葉に宿る闇の力..."
   ```

3. **コミット**
   ```bash
   git add .
   git commit -m "🔧 互換性問題を解決し、エラー処理を改善"
   ```

#### 動画での説明ポイント
- エラーの原因特定方法
- 互換性問題の解決策
- デバッグの基本

---

### Phase 8: コードリファクタリング (動画8)
**目標**: 保守性と拡張性の向上

#### 実装手順
1. **設定ファイルの分離**
   ```python
   # config.py
   DATABASE_NAME = "history.db"
   CHUNIBYO_TEMPLATES = [...]
   ```

2. **クラスベース設計への変更**
   ```python
   class DatabaseManager:
       def __init__(self):
           pass
   
   class ChunibyoTextGenerator:
       def __init__(self):
           pass
   ```

3. **ユーティリティ関数の分離**
   ```python
   # utils.py
   def create_temp_audio_file(text, lang='ja'):
       pass
   ```

4. **段階的なコミット**
   ```bash
   git add config.py
   git commit -m "⚙️ 設定ファイルを分離"
   
   git add utils.py
   git commit -m "🔧 ユーティリティ関数を分離"
   
   git add app.py
   git commit -m "🏗️ クラスベース設計にリファクタリング"
   ```

#### 動画での説明ポイント
- リファクタリングの重要性
- クラス設計の基本
- コードの保守性向上

---

## 🎬 動画制作のコツ

### 各動画の構成
1. **導入 (30秒)**
   - 今回の目標
   - 前回の振り返り

2. **実装 (5-8分)**
   - 実際のコーディング
   - エラーの対処
   - 動作確認

3. **まとめ (1-2分)**
   - 今回の成果
   - 次回の予告

### 視聴者への配慮
- **コードの説明**: 各行の意味を簡潔に説明
- **エラーの共有**: 実際のエラーとその解決過程を見せる
- **進捗の可視化**: 各段階でアプリの動作を確認
- **コミット履歴**: Gitの使い方を自然に学べるように

### 技術的なポイント
- **段階的な実装**: 一度に多くの機能を追加しない
- **エラーハンドリング**: 実際のエラーに対処する過程を見せる
- **ベストプラクティス**: 良いコードの書き方を自然に伝える
- **拡張性**: 将来の機能追加を考慮した設計

## 📈 期待される学習効果

### 視聴者が学べること
- **Streamlit**: Webアプリ開発の基本
- **Python**: 実践的なプログラミング
- **Git**: バージョン管理の基本
- **API連携**: 外部サービスの活用
- **データベース**: データの永続化
- **エラー処理**: 実践的なデバッグ
- **リファクタリング**: コードの改善手法

### 開発者の成長
- **段階的開発**: 計画的な機能追加
- **問題解決**: 実際のエラーへの対処
- **コード品質**: 保守性の高いコード設計
- **ドキュメント**: 開発過程の記録

このガイドに従って開発することで、視聴者にとって価値のある動画シリーズを作成できます！ 