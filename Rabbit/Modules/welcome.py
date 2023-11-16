import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Rabbit import app  
from Rabbit import BOT_USERNAME

photo = [
    "https://telegra.ph/file/1b819cfbcb2a2d3c738f6.jpg",
    "https://telegra.ph/file/3021c823c7f006658682f.jpg",
    "https://telegra.ph/file/05561f0fbf323e057ab87.jpg",
    "https://telegra.ph/file/7a6b51ee0077724254ca7.jpg",
    "https://telegra.ph/file/b3de9e03e5c8737ca897f.jpg",
    "https://telegra.ph/file/0b6bb91986ef3a143033b.jpg",
    "https://telegra.ph/file/2b5b66c9a0989afa0779a.jpg",
    "https://telegra.ph/file/471339bb1901a007c0c2f.jpg",
    "https://telegra.ph/file/ab7d958d707ef649bc3c3.jpg",
    "https://telegra.ph/file/4f877f2843f31fcc32242.jpg",
    "https://telegra.ph/file/ecefaa3e00fb911826673.jpg",
    "https://telegra.ph/file/2a10683a2166f7cf4940b.jpg",
    "https://telegra.ph/file/cda35ca740e1229626e48.jpg",
    "https://telegra.ph/file/9f7186cd3d87199426e03.jpg",
    "https://telegra.ph/file/7fe39f1baa1a93b9a3f0e.jpg",
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"ʜᴇʏ {message.from_user.mention} ᴡᴇʟᴄᴏᴍᴇ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ."
                f"•────────────────•"
                f"•➢ **ɢʀᴏᴜᴘ ɴᴀᴍᴇ** » {message.chat.title}"
                f"•────────────────•"
                f"•➢ **ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ** » @{message.chat.username}"
                f"•────────────────•"
                f"•➢ **ᴜsᴇʀ ɪᴅ** » {message.from_user.id}"
                f"•────────────────•"
                f"•➢ **ɴᴇᴡ ᴜsᴇʀ ᴜsᴇʀɴᴀᴍᴇ** » @{message.from_user.username}"
                f"•────────────────•"
                f"•➢ **ᴄᴏᴍᴘʟᴇᴛᴇᴅ** {count} **ᴍᴇᴍʙᴇʀs**"
                f"•────────────────•"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"• ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ •", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
         ]))
