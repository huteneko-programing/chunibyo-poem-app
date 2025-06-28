# 必要ライブラリのインストール（初回のみ）
# pip install streamlit requests gtts

import streamlit as st
import requests
import sqlite3
import os
from datetime import datetime
from urllib.parse import quote
import json
from gtts import gTTS
import tempfile

# --- DB 初期化 ---
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

# --- プロンプト保存 ---
def save_prompt(prompt, result):
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("INSERT INTO prompts (timestamp, prompt, result) VALUES (?, ?, ?)",
              (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), prompt, result))
    conn.commit()
    conn.close()

# --- プロンプト履歴取得 ---
def get_history():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("SELECT timestamp, prompt, result FROM prompts ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return rows

# --- テキスト生成（簡易版） ---
def generate_text(prompt):
    try:
        # 厨二病なテキストを生成（簡易版）
        chunibyo_responses = [
            f"「{prompt}」という言葉に宿る闇の力が、この世界に新しい物語を紡ぎ出す...",
            f"君の心に響く「{prompt}」の真意、それは運命の扉を開く鍵となるだろう。",
            f"「{prompt}」という呪文が解き放つ力、それはこの現実を超越する存在の証。",
            f"闇の深淵から響く「{prompt}」の響き、それは新たな伝説の始まりを告げる。",
            f"「{prompt}」という言葉に込められた想い、それはこの世界を変える力となる。"
        ]
        import random
        return random.choice(chunibyo_responses)
    except Exception as e:
        return f"厨二病な力の解放中にエラーが発生しました: {str(e)}"

# --- 画像生成 ---
def generate_image_url(prompt):
    return f"https://image.pollinations.ai/prompt/{quote(prompt)}"

# --- 音声合成（gTTS使用） ---
def generate_audio(text):
    try:
        tts = gTTS(text=text, lang='ja', slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            tts.save(fp.name)
            return fp.name
    except Exception as e:
        st.error(f"音声生成エラー: {str(e)}")
        return None

# --- Streamlit UI ---
st.set_page_config(page_title="厨二病ポエムアプリ", layout="centered")
st.title("🎨 厨二病ポエムアプリ")

init_db()

prompt = st.text_input("厨二病なプロンプトを入力してください", placeholder="例: 闇の力を宿した剣士が月明かりの下で戦う")

if st.button("✨ 厨二病生成！") and prompt:
    with st.spinner("厨二病な力を解放中..."):
        text = generate_text(prompt)
        image_url = generate_image_url(prompt)
        audio_file = generate_audio(text)
        save_prompt(prompt, text)

    st.subheader("📝 厨二病テキスト出力")
    st.success(text)

    st.subheader("🖼 厨二病画像出力")
    try:
        st.image(image_url, caption="厨二病な画像生成")
    except Exception as e:
        st.error(f"画像の読み込みに失敗しました: {str(e)}")
        st.info("画像URL: " + image_url)

    st.subheader("🔊 厨二病音声合成")
    if audio_file:
        with open(audio_file, 'rb') as f:
            st.audio(f.read(), format='audio/mp3')
        # 一時ファイルを削除
        os.unlink(audio_file)
    else:
        st.error("音声の生成に失敗しました")

st.markdown("---")
st.subheader("📜 厨二病履歴")
for t, p, r in get_history():
    st.markdown(f"- {t} - **{p}** → {r[:50]}...") 