# Work with Python 3.6
import discord

TOKEN = "NzU5MTE1NjIwNjc5NDE3ODc4.X24zgw.68I_TkhDqXBSE3Y_pvv99v-dYyU"

client = discord.Client()
prefix = "?"

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Hello")


@client.event
async def on_ready():

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)