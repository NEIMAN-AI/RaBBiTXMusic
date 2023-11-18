import asyncio
import importlib
import os
# importing some necessary modules
from pyrogram import idle
# importing some variables from __init__.py
import config
from Rabbit import (
    BUNNY_ID,
    BUNNY_NAME,
    BUNNY_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    app,
    app2,
    pytgcalls,
)
# importing all modules
import config
from Rabbit.Modules import ALL_MODULES
from config import LOG_GROUP_ID as LOGGER_GRP

# connecting all modules with the bot
async def rabbit_startup():
    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("Rabbit.Modules." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    LOGGER.info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")
# sending message is logger group
    try:
        await app.send_message(
            LOGGER_GRP,
            f"** {BOT_NAME} sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**\n\n **__ᴅᴏɴ'ᴛ ғᴏʀɢᴏᴛ ᴛᴏ ᴊᴏɪɴ @RaBBiT_GuYs__**\n\n **ᴇɴᴊᴏʏ ʏᴏᴜʀ ʙᴏᴛ** 🎧",
        )
    except:
        LOGGER.error(
            f"{BOT_NAME} failed to send message at , go & check. logs fast!!"
        )

    try:
        await app2.send_message(
            LOGGER_GRP,
            f"**{BUNNY_NAME} sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**\n\n **__ᴅᴏɴ'ᴛ ғᴏʀɢᴏᴛ ᴛᴏ ᴊᴏɪɴ @RaBBiT_GuYs__**\n\n **ᴇɴᴊᴏʏ ʏᴏᴜʀ ʙᴏᴛ** 🎧",
        )
    except:
        LOGGER.error(
            f"{BUNNY_NAME} failed to send message at ,  go & check logs fast!!."
        )

    await app2.send_message(BOT_USERNAME, "/start")

    LOGGER.info(f"[•] Bot Started As {BOT_NAME}.")
    LOGGER.info(f"[•] Assistant Started As {BUNNY_NAME}.")

    LOGGER.info(
        "[•] music bot deploed successfully enjoy..."
    )
    await pytgcalls.start()
    await idle()

# starting the bot
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(rabbit_startup())
    LOGGER.error("rabbit Music Bot Stopped. bye bye !!")
