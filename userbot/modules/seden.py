# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.seden(?: |$)(.*)")
async def seden(event):
    """ For .seden command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Please specify a Seden module name.")
    else:
        await event.edit("Please specify which Seden module do you want help for !!\
            \nUsage: .seden <module name>")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "` * "
        await event.reply(string)
