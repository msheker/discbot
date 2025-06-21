# game_bot.py

import discord
from discord.ext import commands, tasks
import requests
from bs4 import BeautifulSoup as bs

class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last = False
        self.check.start(993412113517248603, 277291651486187520)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Connected")

    @commands.command(name="ow", help="search for overwatch profile info")
    async def _ow(self, ctx):
        soup = bs(requests.get("https://playoverwatch.com/en-us/career/pc/MehGL-1252/").text, 'html.parser')
        [tnk, dps, sup, *_] = soup.findAll("div", "competitive-rank-level")
        [tnk, dps, sup] = [tnk.text, dps.text, sup.text]
        print(f"Tank: {tnk}; DPS: {dps}; Support: {sup}")
        await ctx.send(f"Tank: {tnk}\nDPS: {dps}\nSupport: {sup}")

    @tasks.loop(seconds=60)
    async def check(m1_id, m2_id):
        g = self.bot.get_guild(470050245997363220)
        m1 = g.get_member(m1_id)
        m2 = g.get_member(m2_id)

        cur = m1.client_status.desktop == 'online'
        print(f'in {cur} == !{self.last}')

        if cur and not self.last:
            self.last = cur
            await g.get_channel(829706919408042054).send(f'{m2.mention} :eyes:')


def setup(bot):
    bot.add_cog(GameCog(bot))
