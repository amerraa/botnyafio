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
                "https://graph.org/file/cfd5ef2f6fff1b20d5a83-eef19b7cffc549bca3.jpg",
                caption="✨ **𝗥𝗼𝘀𝗲𝗽𝗮𝘄-Userbot Berhasil Diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 9.0𝗥𝗼𝘀𝗲𝗽𝗮𝘄-Userbot\n➠ **Ketik** `.ping` **Untuk Mengecek Bot**\n➠ **Ketik** `.help` **Untuk Melihat Informasi Module**\n━━━━━━━━━━━\n➠ **Powered By:** @rosepaw ",
                buttons=[(Button.url("Store", "https://t.me/rosepaw"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
