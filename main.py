from discord.ext import commands
import discord
from keys import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="\\", intents=intents)

bot.load_extension("my_cog")  # make sure my_cog.py is in the same directory or properly pathed

bot.run(DISCORD_TOKEN)