import discord



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

client.run(os.environ['DISCORD_TOKEN'])
