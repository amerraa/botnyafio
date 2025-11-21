from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/c02153188c51b26312125-294065edaae729df14.jpg",
                caption="✨ **𝗕𝗼𝘁𝗻𝘆𝗮𝗳𝗶𝗼 Berhasil Diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 9.0𝗕𝗼𝘁𝗻𝘆𝗮𝗳𝗶𝗼t\n➠ **Ketik** `.ping` **Untuk Mengecek Bot**\n➠ **Ketik** `.help` **Untuk Melihat Informasi Module**\n━━━━━━━━━━━\n➠ **Powered By:** @botnyafio ",
                buttons=[(Button.url("Support", "https://t.me/botnyafio"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
