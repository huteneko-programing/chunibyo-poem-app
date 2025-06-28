# 必要ライブラリのインストール（初回のみ）
# pip install streamlit pollinations.ai requests

import streamlit as st
from pollinations import Text
import requests
import sqlite3
import os
from datetime import datetime
from urllib.parse import quote

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

# --- テキスト生成 ---
def generate_text(prompt):
    model = Text(model="mistral")  # "openai" や "qwen-coder" も可
    return model(prompt)

# --- 画像生成 ---
def generate_image_url(prompt):
    return f"https://image.pollinations.ai/prompt/{quote(prompt)}"

# --- 音声合成 URL ---
def generate_audio_url(prompt):
    return f"https://text.pollinations.ai/{quote(prompt)}?model=openai-audio&voice=nova"

# --- Streamlit UI ---
st.set_page_config(page_title="PollinationsエンタメAIツール", layout="centered")
st.title("🎨 Pollinations AI 複合生成アプリ")

init_db()

prompt = st.text_input("プロンプトを入力してください")

if st.button("✨ 生成！") and prompt:
    with st.spinner("AIが頑張って生成中..."):
        text = generate_text(prompt)
        image_url = generate_image_url(prompt)
        audio_url = generate_audio_url(prompt)
        save_prompt(prompt, text)

    st.subheader("📝 テキスト出力")
    st.success(text)

    st.subheader("🖼 画像出力")
    st.image(image_url, caption="Pollinationsによる画像生成")

    st.subheader("🔊 音声合成")
    st.audio(audio_url)

st.markdown("---")
st.subheader("📜 最近のプロンプト履歴")
for t, p, r in get_history():
    st.markdown(f"- {t} - **{p}** → {r[:50]}...") 