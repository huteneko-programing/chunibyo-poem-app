"""
厨二病ポエムアプリのユーティリティ関数
"""

import os
import tempfile
from typing import Optional
from gtts import gTTS
import streamlit as st

def create_temp_audio_file(text: str, lang: str = 'ja', slow: bool = False) -> Optional[str]:
    """
    一時的な音声ファイルを作成
    
    Args:
        text: 音声化するテキスト
        lang: 言語コード
        slow: ゆっくり再生するかどうか
    
    Returns:
        一時ファイルのパス、失敗時はNone
    """
    try:
        tts = gTTS(text=text, lang=lang, slow=slow)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            tts.save(fp.name)
            return fp.name
    except Exception as e:
        st.error(f"音声ファイル作成エラー: {str(e)}")
        return None

def cleanup_temp_file(file_path: str) -> bool:
    """
    一時ファイルを削除
    
    Args:
        file_path: 削除するファイルのパス
    
    Returns:
        削除成功時はTrue、失敗時はFalse
    """
    try:
        if os.path.exists(file_path):
            os.unlink(file_path)
            return True
        return False
    except Exception as e:
        st.error(f"一時ファイル削除エラー: {str(e)}")
        return False

def validate_prompt(prompt: str) -> bool:
    """
    プロンプトの妥当性をチェック
    
    Args:
        prompt: チェックするプロンプト
    
    Returns:
        妥当な場合はTrue、そうでなければFalse
    """
    if not prompt or not prompt.strip():
        return False
    if len(prompt.strip()) < 2:
        return False
    return True

def format_timestamp(timestamp: str) -> str:
    """
    タイムスタンプをフォーマット
    
    Args:
        timestamp: フォーマットするタイムスタンプ
    
    Returns:
        フォーマットされたタイムスタンプ
    """
    try:
        # 既にフォーマットされている場合はそのまま返す
        if ":" in timestamp and "-" in timestamp:
            return timestamp
        return timestamp
    except:
        return timestamp 