import os
from dotenv import load_dotenv
from client import Client

from typing import Literal, Optional

import discord
from discord.ext import commands


load_dotenv()

BOT_TOKEN = os.environ["DISCORD_TOKEN"]
channel_id = int(os.environ["CHANNEL_ID"])  # channel id has to be an int

intents = discord.Intents().all()

bot = Client(BOT_TOKEN, intents)
bot.activate()
