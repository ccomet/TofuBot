import discord
import json
import os
from datetime import datetime
from threading import Timer

client = discord.Client()
prefix = "t "


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
    elif message.content.startswith(prefix + "i love you"):
        await message.channel.send("<@528299195325480960> loves you more")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.environ['DISCORD_TOKEN'])
