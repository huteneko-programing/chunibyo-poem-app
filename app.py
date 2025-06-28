# 必要ライブラリのインストール（初回のみ）
# pip install streamlit requests

import streamlit as st
import requests
import sqlite3
import os
from datetime import datetime
from urllib.parse import quote
import json

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

# --- テキスト生成（Pollinations API使用） ---
def generate_text(prompt):
    try:
        # Pollinations Text APIを使用
        url = "https://text.pollinations.ai/"
        params = {
            "prompt": prompt,
            "model": "mistral"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.text
        else:
            return f"テキスト生成エラー: {response.status_code}"
    except Exception as e:
        return f"テキスト生成中にエラーが発生しました: {str(e)}"

# --- 画像生成 ---
def generate_image_url(prompt):
    return f"https://image.pollinations.ai/prompt/{quote(prompt)}"

# --- 音声合成 URL ---
def generate_audio_url(prompt):
    return f"https://text.pollinations.ai/{quote(prompt)}?model=openai-audio&voice=nova"

# --- Streamlit UI ---
st.set_page_config(page_title="厨二病ポエムアプリ", layout="centered")
st.title("🎨 厨二病ポエムアプリ")

init_db()

prompt = st.text_input("厨二病なプロンプトを入力してください", placeholder="例: 闇の力を宿した剣士が月明かりの下で戦う")

if st.button("✨ 厨二病生成！") and prompt:
    with st.spinner("厨二病な力を解放中..."):
        text = generate_text(prompt)
        image_url = generate_image_url(prompt)
        audio_url = generate_audio_url(prompt)
        save_prompt(prompt, text)

    st.subheader("📝 厨二病テキスト出力")
    st.success(text)

    st.subheader("🖼 厨二病画像出力")
    st.image(image_url, caption="厨二病な画像生成")

    st.subheader("🔊 厨二病音声合成")
    st.audio(audio_url)

st.markdown("---")
st.subheader("📜 厨二病履歴")
for t, p, r in get_history():
    st.markdown(f"- {t} - **{p}** → {r[:50]}...") 