from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.utils.decorators.language import language
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()

    # Pehle photo bhej rahe hain
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )

    # Ping aur system stats nikal rahe hain
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()

    # Response time calculate kar rahe hain
    resp = (datetime.now() - start).microseconds / 1000

    # Inline buttons create kar rahe hain
    buttons = [
        [
            InlineKeyboardButton("OVERALL STATS", callback_data="overall_stats"),
            InlineKeyboardButton("CLOSE", callback_data="close"),
        ],
    ]
    
    # Caption ko edit kar rahe hain aur buttons add kar rahe hain
    await response.edit_caption(
        caption=_["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=InlineKeyboardMarkup(buttons),
    )