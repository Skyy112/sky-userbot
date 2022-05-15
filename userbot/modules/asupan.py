# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import kyy_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo


@kyy_cmd(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@AsupanKyyUserbot", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"ᴀsᴜᴘᴀɴ ʙʏ [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


@kyy_cmd(pattern="desahcewe$")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahcewe = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(desahcewe), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahan cewe.**")

CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}desahcewe`\
        \n  •  **Function : **Untuk Mengirim voice desah cewe secara random.\
    "
    }
)
