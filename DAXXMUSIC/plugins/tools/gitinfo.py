import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from daxxhub import daxxhub as papadaxx
from DAXXMUSIC import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

###
@app.on_message(filters.command("pink"))
async def daxxhub(_, message):
    text = message.text[len("/pink") :]
    papadaxx(f"{text}").save(f"pink_{message.from_user.id}.png")
    await message.reply_photo(f"pink_{message.from_user.id}.png")
    os.remove(f"pink_{message.from_user.id}.png")
