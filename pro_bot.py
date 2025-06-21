# my_cog.py

import discord
from discord.ext import commands, tasks

class ProCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Connected")

    @commands.command(name='0x', help="Hex to decimal converter")
    async def _0x(self, ctx, num):
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
            print(num, "->", res)
        await ctx.send(str(res))

    @commands.command(name="resume", help="Provides resume in pdf format")
    async def _resume(self, ctx):
        print("Resume")
        msg = await self.bot.get_channel(830733990994247710).history(limit=1).flatten()
        res = msg[0].attachments[0].url
        print(msg)
        await ctx.send(res)

def setup(bot):
    bot.add_cog(ProCog(bot))
