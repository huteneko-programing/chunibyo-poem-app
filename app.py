# 必要ライブラリのインストール（初回のみ）
# pip install streamlit requests gtts

import streamlit as st
import requests
import sqlite3
import os
from datetime import datetime
from urllib.parse import quote
import json
import random
from typing import Optional, List, Tuple
from config import *
from utils import create_temp_audio_file, cleanup_temp_file, validate_prompt, format_timestamp

class DatabaseManager:
    """データベース管理クラス"""
    
    def __init__(self, db_name: str = DATABASE_NAME):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        """データベースの初期化"""
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS prompts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT,
                        prompt TEXT,
                        result TEXT
                    )''')
        conn.commit()
        conn.close()
    
    def save_prompt(self, prompt: str, result: str):
        """プロンプトと結果を保存"""
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO prompts (timestamp, prompt, result) VALUES (?, ?, ?)",
                  (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), prompt, result))
        conn.commit()
        conn.close()
    
    def get_history(self, limit: int = HISTORY_LIMIT) -> List[Tuple[str, str, str]]:
        """履歴を取得"""
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT timestamp, prompt, result FROM prompts ORDER BY id DESC LIMIT ?", (limit,))
        rows = c.fetchall()
        conn.close()
        return rows

class ChunibyoTextGenerator:
    """厨二病テキスト生成クラス"""
    
    def __init__(self):
        self.chunibyo_templates = CHUNIBYO_TEMPLATES
    
    def generate(self, prompt: str) -> str:
        """厨二病テキストを生成"""
        try:
            template = random.choice(self.chunibyo_templates)
            return template.format(prompt=prompt)
        except Exception as e:
            return f"厨二病な力の解放中にエラーが発生しました: {str(e)}"

class ImageGenerator:
    """画像生成クラス"""
    
    def __init__(self, base_url: str = IMAGE_BASE_URL):
        self.base_url = base_url
    
    def generate_url(self, prompt: str) -> str:
        """画像生成URLを作成"""
        return f"{self.base_url}{quote(prompt)}"

class AudioGenerator:
    """音声生成クラス"""
    
    def __init__(self, lang: str = AUDIO_LANGUAGE, slow: bool = AUDIO_SLOW):
        self.lang = lang
        self.slow = slow
    
    def generate(self, text: str) -> Optional[str]:
        """音声ファイルを生成"""
        return create_temp_audio_file(text, self.lang, self.slow)

class ChunibyoApp:
    """厨二病ポエムアプリのメインクラス"""
    
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.text_generator = ChunibyoTextGenerator()
        self.image_generator = ImageGenerator()
        self.audio_generator = AudioGenerator()
    
    def setup_page(self):
        """ページ設定"""
        st.set_page_config(page_title=PAGE_TITLE, layout="centered")
        st.title(f"🎨 {APP_TITLE}")
    
    def display_text_output(self, text: str):
        """テキスト出力を表示"""
        st.subheader("📝 厨二病テキスト出力")
        st.success(text)
    
    def display_image_output(self, image_url: str):
        """画像出力を表示"""
        st.subheader("🖼 厨二病画像出力")
        try:
            st.image(image_url, caption="厨二病な画像生成")
        except Exception as e:
            st.error(f"画像の読み込みに失敗しました: {str(e)}")
            st.info("画像URL: " + image_url)
    
    def display_audio_output(self, audio_file: Optional[str]):
        """音声出力を表示"""
        st.subheader("🔊 厨二病音声合成")
        if audio_file:
            with open(audio_file, 'rb') as f:
                st.audio(f.read(), format='audio/mp3')
            # 一時ファイルを削除
            cleanup_temp_file(audio_file)
        else:
            st.error("音声の生成に失敗しました")
    
    def display_history(self):
        """履歴を表示"""
        st.markdown("---")
        st.subheader("📜 厨二病履歴")
        for timestamp, prompt, result in self.db_manager.get_history():
            formatted_timestamp = format_timestamp(timestamp)
            st.markdown(f"- {formatted_timestamp} - **{prompt}** → {result[:50]}...")
    
    def run(self):
        """アプリを実行"""
        self.setup_page()
        
        # プロンプト入力
        prompt = st.text_input(
            "厨二病なプロンプトを入力してください", 
            placeholder=PLACEHOLDER_TEXT
        )
        
        # 生成ボタン
        if st.button(BUTTON_TEXT) and prompt:
            if not validate_prompt(prompt):
                st.error("プロンプトが短すぎます。もう少し詳しく入力してください。")
                return
                
            with st.spinner(LOADING_TEXT):
                # 各機能を実行
                text = self.text_generator.generate(prompt)
                image_url = self.image_generator.generate_url(prompt)
                audio_file = self.audio_generator.generate(text)
                
                # データベースに保存
                self.db_manager.save_prompt(prompt, text)
                
                # 結果を表示
                self.display_text_output(text)
                self.display_image_output(image_url)
                self.display_audio_output(audio_file)
        
        # 履歴を表示
        self.display_history()

def main():
    """メイン関数"""
    app = ChunibyoApp()
    app.run()

if __name__ == "__main__":
    main() 