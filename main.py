import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "botname",
    bot_token=os.environ["6572682589:AAF5takH59uV7c5PnYjs0BLFwktovJqrxmo"],
    api_id=int(os.environ["25992046"]),
    api_hash=os.environ["6d5400a082dd8fc7989d4a60371934a8"],
)

@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text("Start Message Here")

@bughunter0.on_message(filters.forwarded and filters.channel)
async def channeltag(bot, message):
   try:
       forward_msg = await message.copy(message.chat.id)
       await message.delete()
   except:
       await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")
    
bughunter0.run()
