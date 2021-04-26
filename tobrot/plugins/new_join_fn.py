#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging

import pyrogram
from tobrot import AUTH_CHANNEL, LOGGER


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    # channel_id = str(AUTH_CHANNEL)[4:]
    # message_id = 99
    # display the /help

    await message.reply_text(
        """༺LEECHER BOT༻ \n COMMANDS HELP : \n 1. /gleechwb - Reply to link to upload in gdrive \n 2./leechwb - Reply to link to upload in telegram \n 3. /ytdlwb - Reply to youtube link \n 4. /pytdlwb - Reply to a youtube playlist link \n 5. /renewme - To clear Storage of Bot \n 6. /tleechwb - For telegram leech \n 7. /cancelwb - Reply to link for cancel uploading \n 8. /statuswb - To check current status \n 9. /clearthumbnailwb - To clear thumbnails \n 10. /savethumbnailwb - To save thumbnail \n\n NOTE : ONLY REPLY TO LINKS WORKS DONT DO /command link""",
        disable_web_page_preview=True,
    )
