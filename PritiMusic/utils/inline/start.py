import random 
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton
import config
from PritiMusic import app

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]

def start_panel(_):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])

    buttons = [
        [
            InlineKeyboardButton(
                text=_["SO_B_1"], 
                url=f"https://t.me/{app.username}?startgroup=true",
                style=group_style
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], 
                url=config.SUPPORT_CHAT,
                style=group_style
            ),
        ],
    ]
    return buttons

def private_panel(_):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=alone_style
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID, style=group_style),
            InlineKeyboardButton(text="ᴄʟᴏɴᴇ", callback_data="clone_page", style=group_style)
        ],
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", callback_data="support_page", style=group_style),
            InlineKeyboardButton(text=" sᴏᴜʀᴄᴇ", callback_data="gib_source", style=group_style)
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper", style=alone_style)
        ],
    ]
    return buttons

def support_panel(_):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])

    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT, style=group_style),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL, style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper", style=alone_style)
        ]
    ]
    return buttons

def about_panel(_):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])

    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID, style=group_style),
            InlineKeyboardButton(text=_["S_B_11"], url=config.GITHUB, style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL, style=group_style),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT, style=group_style)
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper", style=alone_style)
        ]
    ]
    return buttons
