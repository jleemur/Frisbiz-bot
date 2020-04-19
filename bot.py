from os import getenv
from dotenv import load_dotenv
from discord.ext import commands, tasks
import requests
import lol

# get environment from .env file
load_dotenv()
DISCORD_TOKEN = getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='<BIZ>')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    check_for_new_matches.start()


@bot.command()
async def junkyard(ctx, p1: str, p2: str, p3: str, p4: str, p5: str):
    message = lol.junkyard(p1, p2, p3, p4, p5)
    await ctx.send(message)


@bot.command()
async def memes(ctx, subreddit='leagueofmemes'):
    message = lol.memes(subreddit)
    await ctx.send(message)


@bot.command()
async def top_champions(ctx, name: str):
    message = lol.top_champions(name)
    await ctx.send(message)


@bot.group()
async def summoners(ctx):
    return


@summoners.command()
async def list(ctx):
    # todo: list all registered summoners in db
    await ctx.send("Todo: list all registered summoners")


@summoners.command()
async def add(ctx, name: str):
    # todo: get summoner name, check if it's in db, add summoner to db
    try:
        message = lol.get_summoner(name)
    except Exception as err:
        message = err
    await ctx.send(message)


@summoners.command()
async def rm(ctx, name: str):
    # todo: get summoner name, check if it's in db, remove summoner from db
    try:
        message = lol.get_summoner(name)
    except Exception as err:
        message = err
    await ctx.send(message)


@tasks.loop(seconds=120)
async def check_for_new_matches():
    print('checking for new matches for registered summoners...')


# @bot.event
# async def on_message(message):
#     print(message)
#     await bot.process_commands(message)


bot.run(DISCORD_TOKEN)