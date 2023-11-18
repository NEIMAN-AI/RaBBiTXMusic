import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from config import OWNER_ID
from Rabbit import BUNNY_MENTION, app, app2
from config import LOG_GROUP_ID as SUNAME


@app.on_message(filters.command(["leaveall", "assleaveall"]) & filters.user(OWNER_ID))
async def ass_leaveall(_, message: Message):
    lear = await message.reply_text(f"» {BUNNY_MENTION} sᴛᴀʀᴛᴇᴅ ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛs...")
    left = 0
    failed = 0
    chats = []
    async for dialog in app2.get_dialogs():
        chats.append(int(dialog.chat.id))
    schat = (await app.get_chat(SUNAME)).id
    for i in chats:
        if i in (-1001901276605, int(schat)):
            continue
        try:
            await app2.leave_chat(int(i))
            left += 1
        except FloodWait as e:
            flood_time = int(e.value)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
            failed += 1
    try:
        await lear.edit_text(
            f"<u>**» {BUNNY_MENTION} sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛs :**</u>\n\n**ʟᴇғᴛ :** `{left}`\n**ғᴀɪʟᴇᴅ :** `{failed}`"
        )
    except:
        await message.reply_text(
            f"<u>**» {BUNNY_MENTION} sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛs :**</u>\n\n**ʟᴇғᴛ :** `{left}`\n**ғᴀɪʟᴇᴅ :** `{failed}`"
        )
