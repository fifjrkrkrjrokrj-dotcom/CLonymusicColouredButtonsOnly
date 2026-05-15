import random
from typing import Union
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PritiMusic import app

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]

def help_pannel(_, START: Union[bool, int] = None):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])

    first = [
        [
            InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1", style=group_style),
            InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2", style=group_style),
            InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["H_B_4"], callback_data="help_callback hb4", style=group_style),
            InlineKeyboardButton(text=_["H_B_5"], callback_data="help_callback hb5", style=group_style),
            InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["H_B_7"], callback_data="help_callback hb7", style=group_style),
            InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8", style=group_style),
            InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback hb9", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["H_B_10"], callback_data="help_callback hb10", style=group_style),
            InlineKeyboardButton(text=_["H_B_11"], callback_data="help_callback hb11", style=group_style),
            InlineKeyboardButton(text=_["H_B_12"], callback_data="help_callback hb12", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["H_B_13"], callback_data="help_callback hb13", style=group_style),
            InlineKeyboardButton(text=_["H_B_14"], callback_data="help_callback hb14", style=group_style),
            InlineKeyboardButton(text=_["H_B_15"], callback_data="help_callback hb15", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper", style=alone_style),
        ],
    ]
    return InlineKeyboardMarkup(first)


def first_page(_, is_owner: bool = False):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])

    first = [
        [
            InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1", style=group_style),
            InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2", style=group_style),
            InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["H_B_11"], callback_data="help_callback hb11", style=group_style),
            InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8", style=group_style),
            InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["H_B_13"], callback_data="help_callback hb13", style=group_style),
            InlineKeyboardButton(text=_["H_B_12"], callback_data="help_callback hb12", style=group_style),
            InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback cloghelp", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["H_B_10"], callback_data="help_callback hb10", style=group_style),
            InlineKeyboardButton(text=_["H_B_14"], callback_data="help_callback hb14", style=group_style),
            InlineKeyboardButton(text=_["H_B_15"], callback_data="help_callback hb15", style=group_style),
        ],
    ]
    
    if is_owner:
        first.append([
            InlineKeyboardButton(text="🛠 ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ", callback_data="help_callback chelp", style=alone_style),
        ])

    first.append([
        InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_home", style=alone_style),
    ])

    return InlineKeyboardMarkup(first)


def clone_help_panel(_):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])

    buttons = [
        [
            InlineKeyboardButton(text="ᴍᴀɴᴀɢᴇ", callback_data="help_callback clone_manage", style=alone_style),
        ],
        [
            InlineKeyboardButton(text="sᴛᴀʀᴛ", callback_data="help_callback clone_start", style=group_style),
            InlineKeyboardButton(text="ᴘɪɴɢ", callback_data="help_callback clone_ping", style=group_style),
        ],
        [
            InlineKeyboardButton(text="ᴘʟᴀʏ ᴍᴏᴅᴇ", callback_data="help_callback clone_play", style=group_style),
            InlineKeyboardButton(text="ʟᴏɢɢᴇʀ", callback_data="help_callback clone_logger", style=group_style),
        ],
        [
            InlineKeyboardButton(text="ʙᴜᴛᴛᴏɴs & ʀᴇɴᴀᴍᴇ", callback_data="help_callback clone_buttons", style=alone_style),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settings_back_helper", style=alone_style),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def clone_back_markup(_):
    alone_style = random.choice(STYLES)

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="help_callback chelp",
                    style=alone_style
                )
            ]
        ]
    )


def help_back_markup(_):
    alone_style = random.choice(STYLES)

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="settings_back_helper",
                    style=alone_style
                )
            ]
        ]
    )


def private_help_panel(_):
    alone_style = random.choice(STYLES)

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_4"],
                    url=f"https://t.me/{app.username}?start=help",
                    style=alone_style
                )
            ]
        ]
    )
