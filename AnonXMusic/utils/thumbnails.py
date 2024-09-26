import aiofiles
import aiohttp
import os
from PIL import Image, ImageDraw, ImageFont

async def get_thumb(videoid, user_id, bot_name):
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

                # Open the thumbnail image and type text on it
                img = Image.open(save_path)
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("arial.ttf", 20)  # Set the font and size as per your requirement.
                text_width, text_height = draw.textsize(bot_name, font=font)
                draw.text((img.width - text_width - 10, 10), bot_name, font=font, fill="white")

                img.save(save_path)
                return save_path
            else:
                return None  # Here you need to add error handling if the thumbnail is not found.