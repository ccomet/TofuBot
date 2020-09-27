import discord
import json
import os
from datetime import datetime
from threading import Timer

client = discord.Client()
prefix = "tofu "


# Hello Response
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(prefix + "hello"):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith(prefix + "ping"):
        await message.channel.send("pong")


client.run(os.environ['DISCORD_TOKEN'])
