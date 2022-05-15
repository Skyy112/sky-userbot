""" Userbot module for other small commands. """
from userbot import CMD_HELP, owner, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, kyy_cmd


@kyy_cmd(pattern="lhelp$")
async def usit(e):
    await edit_or_reply(
                        f"**Halo {owner} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `{cmd}help` Atau Bisa Minta Bantuan Ke:\n"
                        "\n[Telegram](t.me/yaudahhlahhhh)"
                        "\n[Repo](https://github.com/Skyy112/sky-userbot)"


@kyy_cmd(pattern="vars$")
async def var(m):
    await edit_or_reply(m,
                        f"**Disini Daftar Vars Dari {owner}:**\n"
                        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Skyy112/sky-userbot/main/varshelper.txt)")


CMD_HELP.update({
    "helper":
    f"`{cmd}lhelp`\
\nUsage: Bantuan Untuk sky-userbot.\
\n`{cmd}vars`\
\nUsage: Melihat Daftar Vars."
})
