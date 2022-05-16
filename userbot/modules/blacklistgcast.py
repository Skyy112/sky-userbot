# FROM TRANS-BOT <https://github.com/RyuuXS/TRANS-BOT>
# t.me/helpforRYUU & t.me/Belajarbersamaryuu
# ⚠️ JANGAN HAPUS CREDIT INI !!
# Recode by @sky

import os 

import heroku3

from userbot import BLACKLIST_GCAST
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, HEROKU_API_KEY, HEROKU_APP_NAME
from userbot.utils import edit_delete, edit_or_reply, kyy_cmd

heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
blchat = os.environ.get("BLACKLIST_GCAST") or ""

@kyy_cmd(pattern="addblacklist(?:\s|$)([\s\S]*)")
async def add(event):
  xx = await edit_or_reply(event, "`Processing...`")
  var = "BLACKLIST_GCAST"
  gc = event.chat_id
  if HEROKU_APP_NAME is not None:
    app = Heroku.app(HEROKU_APP_NAME)
  else:
    await edit_delete(
      xx,
      "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
      
    )
    return
  heroku_Config = app.config()
  if event is None:
    return
  blchat = f"{BLACKLIST_GCAST} {gc}"
  nenwbl = blchat.replace("{", "")
  nenwbl = nenwbl.replace("}", "")
  blcht = nenwbl.replace(",", "")
  gcastblc = blcht.replace("[", "")
  gcid = gcastblc.replace("]", "")
  gcast_blc = gcid.replace("set() ", "")
  await xx.edit(
      f"**Berhasil Menambahkan** `{gc}` **ke Daftar GCast Blacklist.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
  )
  heroku_Config[var] = gcast_blc
  
  
@kyy_cmd(pattern="delblacklist(?:\s|$)([\s\S]*)")
async def _(event):
    xx = await edit_or_reply(event, "`Processing...`")
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    gett = str(gc)
    if gett in blchat:
        nenwbl = blchat.replace(gett, "")
        await xx.edit(
            f"**Berhasil Menghapus** `{gc}` **dari Daftar GCast Blacklist.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        var = "BLACKLIST_GCAST"
        heroku_Config[var] = nenwbl
    else:
        await edit_delete(
            xx, "**Pengguna ini tidak ada dalam Daftar GCast Blacklist.**", 45
        )
        
        
CMD_HELP.update(
    {
        "blacklistgcast": f"**Modules : **`blacklistgcast`\
        \n\n • **Command :** `{cmd}addblacklist`\
        \n • **Function : **Untuk menambah blacklist Gcast kalian\
        \n\n • **Command :** `{cmd}delblacklist`\
        \n • **Function : **Untuk mengurangi blacklist Gcast kalian\
    "
    }
)
