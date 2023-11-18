from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from Rabbit import BOT_NAME, app


@app.on_message(
    filters.command(["var", "vars"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>**{BOT_NAME} ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs :**</u>

**ᴀᴘɪ_ɪᴅ :** `{config.API_ID}`
**ᴀᴘɪ_ʜᴀsʜ :** `{config.API_HASH}`

**ʙᴏᴛ_ᴛᴏᴋᴇɴ :** `{config.BOT_TOKEN}`
**ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ :** `{config.DURATION_LIMIT}`

**ᴏᴡɴᴇʀ_ɪᴅ :** `{config.OWNER_ID}`
**sᴜᴅᴏ_ᴜsᴇʀs :** `{config.SUDO_USERS}`

**ᴘɪɴɢ_ɪᴍɢ :** `{config.PING_IMG}`
**ᴀʟɪᴠᴇ_ɪᴍɢ :** `{config.ALIVE_IMG}`
**sᴛᴀʀᴛ_ɪᴍɢ :** `{config.START_IMG}`

**sᴜᴘᴘᴏʀᴛ_ᴄʜᴀᴛ :** `{config.SUPPORT_CHAT}`
**sᴜᴘᴘᴏʀᴛ_ᴄʜᴀɴɴᴇʟ :** `{config.SUPPORT_CHANNEL}`

**sᴇssɪᴏɴ :** `{config.SESSION}`""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("» ғᴀɪʟᴇᴅ ᴛᴏ sᴇɴᴅ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "» ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘᴍ, ɪ'ᴠᴇ sᴇɴᴛ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs ᴛʜᴇʀᴇ."
        )
