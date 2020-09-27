import discord
import json
import os
from datetime import datetime
from threading import Timer

client = discord.Client()
prefix = "tofu"


# Hello Response
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(prefix + "hello"):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    if message.content.startswith("hello"):
        if str(message.author) == "Kyo#9355":
            await message.channel.send("Hello " + "<@352330857286991902>")
        if str(message.author) == "Xenon#3636":
            await message.channel.send("Hello " + "<@528299195325480960>")


client.run(os.environ['DISCORD_TOKEN'])
