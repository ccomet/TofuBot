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
    i = 0
    while not client.is_closed:
        await message.channel.send(client.get_channel("759472278261071934"), "I am running")
        i += 1
        if i >= 1:
            break
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)