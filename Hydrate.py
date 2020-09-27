import discord
import os
from datetime import datetime
from threading import Timer

client = discord.Client()
prefix = "?"

x = datetime.today()
y = x.replace(day=x.day, hour=20, minute=20, second=30, microsecond=0)
delta_t = y - x

secs = delta_t.seconds + 1


@client.event
async def drink_water():
    await message.channel.send("Time to drink water")


t = Timer(secs, drink_water)
t.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.author) == "Kyo#9355":
        await message.channel.send("Hello " + "<@352330857286991902>")
    else:
        await message.channel.send("Tofu")
