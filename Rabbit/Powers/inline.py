from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from Rabbit import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data="close")]]
)


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


helpmenu = [
    [
        InlineKeyboardButton(
            text="ᴇᴠᴇʀʏᴏɴᴇ",
            callback_data="rabbit_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="• sᴜᴅᴏ •", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data="rabbit_home"),
        InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="• sᴜᴩᴩᴏʀᴛ •", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="• ʙᴀᴄᴋ •", callback_data="rabbit_help"),
        InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data="close"),
    ],
