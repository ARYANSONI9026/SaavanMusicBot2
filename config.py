import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ───── Basic Bot Configuration ───── #
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", 7710642242))
OWNER_USERNAME = getenv("OWNER_USERNAME", "smartness_to_hai")
BOT_USERNAME = getenv("BOT_USERNAME", "Bella_Music_Robot")
BOT_NAME = getenv("BOT_NAME", "⏤͟͞●𝐵𝑒𝑙𝑙𝑎ᥫ᭡𝑀𝑢𝑠𝑖𝑐..♪♪🧚")
ASSUSERNAME = getenv("ASSUSERNAME", "knight_society")
EVALOP = list(map(int, getenv("EVALOP", "7714883515").split()))

# ───── Mongo & Logging ───── #
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", -1002311424197))

# ───── Limits and Durations ───── #
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ───── Custom API Configs ───── #
API_URL = getenv("API_URL") #optional
API_KEY = getenv("API_KEY") #optional
COOKIE_URL = getenv("COOKIE_URL") #necessary
DEEP_API = getenv("DEEP_API") #optional

# ───── Heroku Configuration ───── #
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ───── Git & Updates ───── #
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ARYANSONI9026/TestingMusicBot2")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")

# ───── Support & Community ───── #
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tabahi_tabahi")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tabahi_tabahi")

# ───── Assistant Auto Leave ───── #
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

# ───── Error Handling ───── #
DEBUG_IGNORE_LOG =True

# ───── Spotify Credentials ───── #
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ───── Session Strings ───── #
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ───── Server Settings ───── #
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))

# ───── Bot Media Assets ───── #

START_VIDS = [
    "https://files.catbox.moe/av5o3h.mp4",
    "https://files.catbox.moe/av5o3h.mp4",
    "https://files.catbox.moe/av5o3h.mp4"
]

STICKERS = [
    "CAACAgUAAx0Cd6nKUAACASBl_rnalOle6g7qS-ry-aZ1ZpVEnwACgg8AAizLEFfI5wfykoCR4h4E",
    "CAACAgUAAx0Cd6nKUAACATJl_rsEJOsaaPSYGhU7bo7iEwL8AAPMDgACu2PYV8Vb8aT4_HUPHgQ"
]
HELP_IMG_URL = "https://te.legra.ph/file/ec19cf227791a167abedc.jpg"
PING_VID_URL = "https://files.catbox.moe/1zfcm5.mp4"
PLAYLIST_IMG_URL = "https://telegra.ph/file/94e9eca3b0ec6e2dc6cd5.png"
STATS_VID_URL = "https://files.catbox.moe/d03zlc.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/mlztag.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/tiss2b.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/1d3da7.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/zhymxl.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/veykzq.jpg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ───── Utility & Functional ───── #
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── Bot Introduction Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🌈", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌", "🧨"]
AYUV = [
       "<b>𝖧𝖾𝗒 {0} !\n𝖨'𝗆 {1} ,</b>\n\n<b>๏ 𝗪𝗮𝗻𝗻𝗮 𝗟𝗶𝘀𝘁𝗲𝗻 𝗠𝘂𝘀𝗶𝗰 ?</b>\n➜ 𝖨'𝗆 𝖠 𝖥𝖺𝗌𝗍 𝖠𝗇𝖽 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖬𝗎𝗌𝗂𝖼 𝖯𝗅𝖺𝗒𝖾𝗋 𝖡𝗈𝗍 𝖶𝗂𝗍𝗁 𝖲𝗈𝗆𝖾 𝖠𝗐𝖾𝗌𝗈𝗆𝖾 𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌 .\n\n<b>๏ 𝗪𝗮𝗻𝗻𝗮 𝗞𝗻𝗼𝘄 𝗛𝗼𝘄 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲 ?</b>\n➜ 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 𝖳𝗁𝖾 𝖧𝖾𝗅𝗉 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖡𝗎𝗍𝗍𝗈𝗇 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖠𝖻𝗈𝗎𝗍 𝖬𝗒 𝖬𝗈𝖽𝗎𝗅𝖾𝗌 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 .",
       "<b>𝖧𝖾𝗒 {0} !\n𝖨'𝗆 {1} ,</b>\n\n<b>๏ 𝗪𝗮𝗻𝗻𝗮 𝗟𝗶𝘀𝘁𝗲𝗻 𝗠𝘂𝘀𝗶𝗰 ?</b>\n➜ 𝖨'𝗆 𝖠 𝖥𝖺𝗌𝗍 𝖠𝗇𝖽 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖬𝗎𝗌𝗂𝖼 𝖯𝗅𝖺𝗒𝖾𝗋 𝖡𝗈𝗍 𝖶𝗂𝗍𝗁 𝖲𝗈𝗆𝖾 𝖠𝗐𝖾𝗌𝗈𝗆𝖾 𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌 .\n\n<b>๏ 𝗪𝗮𝗻𝗻𝗮 𝗞𝗻𝗼𝘄 𝗛𝗼𝘄 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲 ?</b>\n➜ 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 𝖳𝗁𝖾 𝖧𝖾𝗅𝗉 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖡𝗎𝗍𝗍𝗈𝗇 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖠𝖻𝗈𝗎𝗍 𝖬𝗒 𝖬𝗈𝖽𝗎𝗅𝖾𝗌 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 .",
]

# ───── Runtime Structures ───── #
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ───── URL Validation ───── #
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
