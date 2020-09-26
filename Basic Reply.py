# Work with Python 3.6
import discord

client = discord.Client()
prefix = "?"

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