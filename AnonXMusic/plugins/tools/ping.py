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

    # Pehle image ke saath reply karo, aur caption ko quotes me bhejo
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=f'\"{_["ping_1"].format(app.mention)}\"',  # Quotes added around the caption
    )

    # Ping aur system stats calculate karo
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    # Image ko delete karke, updated message ke saath edit karo
    await response.delete()

    # Fir message ko stats ke saath update karo
    await message.reply_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )