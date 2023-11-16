from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from Powers.database import add_user, add_group, all_users, all_groups, users, remove_user
from Rabbit import app
from config import SUDO_USERS
import config


@app.on_message(filters.command("bcast") & filters.user(config.SUDO_USERS))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ ᴩʀᴏᴄᴇꜱꜱɪɴɢ...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"•ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟ ᴛᴏ `{success}` ᴜꜱᴇʀꜱ.\n• ꜰᴀɪʟᴅ ᴛᴏo `{failed}` ᴜꜱᴇʀꜱ.\n• ꜰᴏᴜɴᴅ `{blocked}` Blocked users \n• Found `{deactivated}` ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴜꜱᴇʀꜱ.")
