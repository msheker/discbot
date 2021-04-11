import discord
from keys import DISCORD_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('\0x '):
        num = message.content.split(" ")[1]
        await message.channel.send(num)

client.run(DISCORD_TOKEN)
