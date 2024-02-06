# copyright 2023 © Xron Trix | https://github.com/Xrontrix10

import logging, json
from uvloop import install
from pyrogram.client import Client
from main import API_ID, API_HASH, BOT_TOKEN, USER_ID, DUMP_ID
# Read the dictionary from the txt file
# with open("/content/Telegram-Leecher/credentials.json", "r") as file:
    # credentials = json.loads(file.read())

API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = BOT_TOKEN
OWNER = USER_ID
DUMP_ID = DUMP_ID


logging.basicConfig(level=logging.INFO)

install()

colab_bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
