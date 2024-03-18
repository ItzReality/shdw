import os
from dotenv import load_dotenv
from client import Client

from typing import Literal, Optional

import discord
from discord.ext import commands


load_dotenv()

# intents = discord.Intents.all()
# client = discord.Client(intents=intents)
# intents.members = True
# bot = commands.Bot(command_prefix="!", intents=intents)
BOT_TOKEN = os.environ["DISCORD_TOKEN"]
channel_id = int(os.environ["CHANNEL_ID"])  # channel id has to be an int


intents = discord.Intents().all()

bot = Client(BOT_TOKEN, intents)


bot.activate()
