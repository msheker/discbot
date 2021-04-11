import discord
from discord.ext import commands
from keys import DISCORD_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('\\0x '):
        num = message.content.split(" ")[1].lower()
        res = 0
        abc = "0123456789abcdef"
        for x in num:
            res = res * 16
            if x not in abc:
                await messsage.channel.send("ERROR: Expected hex, got: " + num)
                return
            res = res + abc.index(x)
        print(num,"->",res)
        await message.channel.send(str(res))

bot = commands.Bot(command_prefix=">")

@bot.command(name='0x', help="Hex to decimal converter")
async def _0x(ctx, num):
    num = num.lower()
    res = 0
    abc = "0123456789abcdef"
    for x in num:
        res = res * 10
        if x not in abc:
            await ctx.send("ERROR: Expected hex, got: " + num)
            return
        res = res + abc.index(x)
        print(num,"->",res)
    await ctx.send(str(res))

@bot.command(name="resume", help="Provides resume in ppdf format")
async def _resume(ctx):

    await ctx.send()


client.run(DISCORD_TOKEN)
