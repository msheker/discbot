import discord
from discord.ext import commands
from keys import DISCORD_TOKEN
import requests
from bs4 import BeautifulSoup as bs

bot = commands.Bot(command_prefix="\\")

@bot.event
async def on_ready():
    print("Connected")
    return

@bot.command(name='0x', help="Hex to decimal converter")
async def _0x(ctx, num):
    print("Hex")
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

@bot.command(name="resume", help="Provides resume in pdf format")
async def _resume(ctx):
    print("Resume")
    msg = await bot.get_channel(830733990994247710).history(limit=1).flatten()
    res = msg[0].attachments[0].url
    print(msg)
    await ctx.send(res)

@bot.command(name="ow", help="search for overwatch profile info")
async def _ow(ctx):
    soup = bs(requests.get("https://playoverwatch.com/en-us/career/pc/MehGL-1252/").text, 'html.parser')
    [tnk,dps,sup,ig,ig1,ig2] = soup.findAll("div","competitive-rank-level")
    [tnk,dps,sup] = [tnk.text,dps.text,sup.text]
    print(f"Tank: {tnk}; DPS: {dps}; Support: {sup}")
    await ctx.send(f"Tank: {tnk}\n DPS: {dps}\n Support: {sup}")

bot.run(DISCORD_TOKEN)
