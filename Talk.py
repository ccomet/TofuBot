import discord
import os


client = discord.Client()
prefix = "?"

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.content.startswith(prefix+"hello"):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith(prefix+"bot"):
        await message.channel.send("I am here")
    elif message.content.startswith(prefix+"ping"):
        await message.channel.send("pong")

#Kyo id == <@352330857286991902>
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Hello")
        if str(message.author) == "Xenon#3636":
            await message.channel.send("Hello " + "<@528299195325480960>")
        else:
            await message.channel.send("Tofu")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.environ['DISCORD_TOKEN'])
