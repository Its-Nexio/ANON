from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    
    # phale image ke sath reply kar rahe hai
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    
    # ping or system stats nikalna
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    
    # calculating the response time
    resp = (datetime.now() - start).microseconds / 1000
    
    # editing quotes with style
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )

    # adding button to quotes style
    buttons = [
        [
            InlineKeyboardButton("OVERALL STATS", callback_data="overall_stats"),
            InlineKeyboardButton("CLOSE", callback_data="close"),
        ],
    ]
    
    await response.edit_caption(
        caption=_["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=InlineKeyboardMarkup(buttons),
    )