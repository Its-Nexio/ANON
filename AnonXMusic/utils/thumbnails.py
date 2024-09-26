import aiofiles
import aiohttp
import os
from PIL import Image

from AnonXMusic import app

async def get_thumb(videoid, user_id):
    thumbnail_url = f"https://img.youtube.com/vi/{videoid}/maxresdefault.jpg"
    save_path = f"cache/{videoid}_{user_id}.png"
    if os.path.isfile(save_path):
        return save_path

    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail_url) as response:
            if response.status == 200:
                f = await aiofiles.open(save_path, mode="wb")
                await f.write(await response.read())
                await f.close()
                return save_path
            else:
                return None  # Here you need to add error handling if the thumbnail is not found.