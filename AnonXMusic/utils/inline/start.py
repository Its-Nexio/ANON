from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [ InlineKeyboardButton(text="ᴛʜᴇ ɢʀᴀʙʙɪɴɢ 𐏓", url=f"https://t.me/+9BzQheU_WO1jY2M1")],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url=f"https://t.me/miss_angel52"),  # Error Fixed
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="ᴀʙᴏᴜᴛ", url=f"https://t.me/where_lucy")],
    ]
    return buttons