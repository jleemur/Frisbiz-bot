from os import getenv
from dotenv import load_dotenv
from discord.ext import commands
import requests
import lol

# get environment from .env file
load_dotenv()
DISCORD_TOKEN = getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='<BIZ>')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def junkyard(ctx, p1: str, p2: str, p3: str, p4: str, p5: str):
    message = lol.junkyard(p1, p2, p3, p4, p5)
    await ctx.channel.send(message)


@bot.command()
async def memes(ctx, subreddit='leagueofmemes'):
    message = lol.memes(subreddit)
    await ctx.channel.send(message)


@bot.command()
async def summoner(ctx, name):
    message = lol.summoner(name)
    await ctx.channel.send(message)


# @bot.event
# async def on_message(message):
#     print(message)
#     await bot.process_commands(message)


bot.run(DISCORD_TOKEN)