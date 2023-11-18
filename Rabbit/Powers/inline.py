from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# importing some necessary module
import config
from Rabbit import BOT_USERNAME
# making inline button
close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data="close")]]
)

# making play buttons
buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)

# creating start button
pm_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="rabbit_help")],
    [
        InlineKeyboardButton(text="• ᴄʜᴀɴɴᴇʟ •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• sᴜᴩᴩᴏʀᴛ •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• sᴏᴜʀᴄᴇ •", url="https://github.com/ITZ-RaBBiT/RaBBiTXMusic"
        ),
        InlineKeyboardButton(text="• ᴅᴇᴠᴇʟᴏᴩᴇʀ •", user_id=config.OWNER_ID),
    ],
]

# creating group start button
gp_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="• ᴄʜᴀɴɴᴇʟ •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• sᴜᴩᴩᴏʀᴛ •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• sᴏᴜʀᴄᴇ •", url="https://github.com/ITZ-RaBBiT/RaBBiTXMusic"
        ),
        InlineKeyboardButton(text="• ᴅᴇᴠᴇʟᴏᴩᴇʀ •", user_id=config.OWNER_ID),
    ],
]

# creating help manu for the bot 
helpmenu = [
    [
        InlineKeyboardButton(
            text="ᴇᴠᴇʀʏᴏɴᴇ",
            callback_data="rabbit_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="• sᴜᴅᴏ •", callback_data="rabbit_cb sudo"),
        InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", callback_data="rabbit_cb owner"),
    ],
    [
        InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data="rabbit_home"),
        InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data="close"),
    ],
]

# creating help back button for bot help manu 
help_back = [
    [InlineKeyboardButton(text="• sᴜᴩᴩᴏʀᴛ •", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data="rabbit_help"),
        InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data="close"),
    ],
 ]
# code by MrRaBBiT on telegram
