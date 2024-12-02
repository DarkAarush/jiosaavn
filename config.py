import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "18499702"))
API_HASH = getenv("d4dff36c2c1ebf6f8f6bc044b5bce9c9")

BOT_TOKEN = getenv("6051187601:AAFVHv00gc0SJhGwxkqmR_4uM8ZA528t7p4")

MONGO_DB_URI = getenv("mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002224506833"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐖𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄 🎶...")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5050578106").split()))

HEROKU_API_KEY = getenv("HRKU-5750435b-e69a-4751-9d27-1037a3dafa0d", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/DarkAarush/Aarush")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Cute_Copy_Aarush")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("BQEaSHYArQSTgbqa-Y44-OIAmt5R5vKSTXPg03QExQnkhB6b6yOvjhl6UVmHt91k99Lrk4mGiMLD9VQxeVh8zDclBPweW4l9B2NiS5zobCanhzzspMywuKLeIsMTLn1nQlI3rGJCLxhhBVn-RerjHIFxzxTjE3mHOCwcEuHg7aS8gckaHflps_cfF1jUR5wxmzY7jLs34mRz_VokOp9N0HTJw4qLAPYQXcR_Zncy-GUNxZQ5mxQg7r8kdR19KMuqvjkY478GDqLL4DW6Be-xyhAdoU_6C79bFgph600ZJ2M6ma23jLrI-dC64jjDvJ4sw0lbFHkltZZO8hwxahP5y0QPzKZWCgAAAAHLMGAEAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/dab9845af235076bde502.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/dab9845af235076bde502.jpg",
)

PLAYLIST_IMG_URL = "https://images.app.goo.gl/rcNY1uNxT7BtMZz89"

GLOBAL_IMG_URL = "https://images.app.goo.gl/rcNY1uNxT7BtMZz89"

STATS_IMG_URL = "https://images.app.goo.gl/rcNY1uNxT7BtMZz89"

TELEGRAM_AUDIO_URL = "https://images.app.goo.gl/h5DMKrHyzMSRhV3o9"

TELEGRAM_VIDEO_URL = "https://images.app.goo.gl/h5DMKrHyzMSRhV3o9"

STREAM_IMG_URL = "https://images.app.goo.gl/h5DMKrHyzMSRhV3o9"

SOUNCLOUD_IMG_URL = "https://images.app.goo.gl/h5DMKrHyzMSRhV3o9"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://graph.org/file/dab9845af235076bde502.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://graph.org/file/dab9845af235076bde502.jpg"
