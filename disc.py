import discord
from discord.ext import commands
from keys import DISCORD_TOKEN

bot = commands.Bot(command_prefix="\\")

@bot.command(name='0x', help="Hex to decimal converter")
async def _0x(ctx, num):
    num = num.lower()
    res = 0
    abc = "0123456789abcdef"
    for x in num:
        res = res * 16
        if x not in abc:
            await ctx.send("ERROR: Expected hex, got: " + num)
            return
        res = res + abc.index(x)
        print(num,"->",res)
    await ctx.send(str(res))

@bot.command(name="resume", help="Provides resume in ppdf format")
async def _resume(ctx):
    msg = await bot.get_channel(830733990994247710).history(limit=1).flatten()
    res = msg[0].attachments[0].url
    print(msg)
    await ctx.send(res)

bot.run(DISCORD_TOKEN)
