"""
厨二病ポエムアプリの設定ファイル
"""

# データベース設定
DATABASE_NAME = "history.db"
HISTORY_LIMIT = 10

# 画像生成設定
IMAGE_BASE_URL = "https://image.pollinations.ai/prompt/"

# 音声生成設定
AUDIO_LANGUAGE = 'ja'
AUDIO_SLOW = False

# アプリ設定
APP_TITLE = "厨二病ポエムアプリ"
PAGE_TITLE = "厨二病ポエムアプリ"

# 厨二病テンプレート
CHUNIBYO_TEMPLATES = [
    "「{prompt}」という言葉に宿る闇の力が、この世界に新しい物語を紡ぎ出す...",
    "君の心に響く「{prompt}」の真意、それは運命の扉を開く鍵となるだろう。",
    "「{prompt}」という呪文が解き放つ力、それはこの現実を超越する存在の証。",
    "闇の深淵から響く「{prompt}」の響き、それは新たな伝説の始まりを告げる。",
    "「{prompt}」という言葉に込められた想い、それはこの世界を変える力となる。",
    "封印されし「{prompt}」の真実、今こそ解き放たれる時が来たのだ。",
    "「{prompt}」という禁断の言葉、それは神をも超越する力を持つ。",
    "君の魂に刻まれた「{prompt}」の記憶、それは永遠の物語の序章。",
    "「{prompt}」という究極の奥義、それは全てを支配する絶対の力。",
    "闇の契約者として「{prompt}」を解き放つ、それが我が使命。"
]

# UI設定
PLACEHOLDER_TEXT = "例: 闇の力を宿した剣士が月明かりの下で戦う"
BUTTON_TEXT = "✨ 厨二病生成！"
LOADING_TEXT = "厨二病な力を解放中..." 