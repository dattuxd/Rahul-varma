import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonX import app  

photo = [
    "https://telegra.ph/file/c7b551119ea15dc365f68.jpg",
    "https://telegra.ph/file/1d19bdc70cb7ef3d60001.jpg",
    "https://telegra.ph/file/cb746616b6189e00fec71.jpg",
    "https://telegra.ph/file/71f57ec08d362b2247c6b.jpg",
    "https://telegra.ph/file/aef32840b7c2943031ad6.jpg",
    "https://telegra.ph/file/005f3268e52de060eab78.jpg",
    "https://telegra.ph/file/c04036447f2936ee4dd75.jpg",
    "https://telegra.ph/file/5cf94672c06083e36773f.jpg",
    "https://telegra.ph/file/952bac570b471a4243c8d.jpg",

]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat

    for members in message.new_chat_members:

            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🥀𝐇ᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
                f"**☘️𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**⚡️𝐂ʜᴀᴛ 𝐔.𝐍:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**💖𝐔ʀ 𝐈d:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**✨️𝐔ʀ 𝐔.𝐍:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🌠𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🥳 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ 🥳", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
