from os import getenv
from asyncio import sleep

from telethon import TelegramClient, events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.errors import ChatAdminRequiredError, ChannelPrivateError
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins


TOKEN1 = "6802193672:AAHrQUOfZkKP4tmLYjaiWs_ePJg2qopWL08"
TOKEN2 = "6518673116:AAF-A-BFPGyJwRN2_dTJK-As7ob9W1Boqps"
TOKEN3 = "6985495947:AAH6xUoha8LFxWEEbU0Uca_0ziI-qd2Q9Dg"
TOKEN4 = "6302692779:AAEOJycUBlYz1lJm5zQQ9A9RcOH-foJt6gI"
TOKEN5 = "5836583089:AAEPsmciESgYQvjS_NQdG6G1dbH75mykGgk"

API_ID = 25981592
API_HASH = "709f3c9d34d83873d3c7e76cdd75b866"

SUDO = [1854748754]
SUDO.append(5518687442)

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
    if event.sender_id in SUDO:
        fuck = await event.reply("🔁 __GETTING READY...__")
        try:
            chat_id = int(event.text.split(" ")[1])
        except:
            await fuck.edit("**Usage:**\n`/fuck [chat_id]`")
            return

        admins = await event.client.get_participants(chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins] + SUDO
        await fuck.edit("✅ __STARTED FUCKING THE GROUP...__")
        await sleep(3)

        async for user in event.client.iter_participants(chat_id):
            if user.id not in admins_id:
                try:
                    await event.client(EditBannedRequest(chat_id, user.id, RIGHTS))
                except (ChatAdminRequiredError, ChannelPrivateError):
                    break
                except:
                    continue


@bot1.on(events.NewMessage(pattern="^/start"))
@bot2.on(events.NewMessage(pattern="^/start"))
@bot3.on(events.NewMessage(pattern="^/start"))
@bot4.on(events.NewMessage(pattern="^/start"))
@bot5.on(events.NewMessage(pattern="^/start"))
async def start(event):
    await event.reply("🤖 **I AM STILL ALIVE...**")


bot1.run_until_disconnected()
bot2.run_until_disconnected()
bot3.run_until_disconnected()
bot4.run_until_disconnected()
bot5.run_until_disconnected()
