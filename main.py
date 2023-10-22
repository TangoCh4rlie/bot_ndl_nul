import discord
from discord.ext import commands
import datetime

import os
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!", description="Bot Nuit de L'info", intents=intents
)

year = 2023
month = 12
day = 7
hour = 16
minute = 38


@bot.event
async def on_ready():
    print("Bot is ready!")


def getTime():
    # calculate the actual date dans time resting to the event
    now = datetime.datetime.now()
    event = datetime.datetime(year, month, day, hour, minute)
    time = event - now
    _month = time.days // 30
    _day = time.days % 30
    _hour = time.seconds // 3600
    _minute = (time.seconds // 60) % 60
    _second = time.seconds % 60
    time = f"Vite prépare toi il reste : {_month} mois {_day} jours {_hour} heures {_minute} minutes {_second} secondes"
    print(time)
    return time


@bot.command()
async def ndl(ctx):
    author = ctx.message.author.mention
    print(author)
    if author == "<@395583276175196160>":
        await ctx.send(
            "Frr arrete de spam, t'es chiant avec ta nuit de l'info à la con"
        )
    else:
        time = getTime()
        await ctx.send(time)


load_dotenv()

secret_key = os.getenv("SECRET_KEY")
print(secret_key)
bot.run(secret_key)
