from AnonX.core.bot import AnonXBot
from AnonX.core.dir import dirr
from AnonX.core.git import git
from AnonX.core.userbot import Userbot
#from AnonX.core.misc import dbb, heroku
from pyrogram import Client
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = AnonX()
api = SafoneAPI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
