import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # charge le fichier .env

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command()
async def spam(ctx):
    for _ in range(10):
        await ctx.send("@everyone")

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
