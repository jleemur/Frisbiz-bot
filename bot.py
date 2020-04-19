from os import getenv
from dotenv import load_dotenv
from discord.ext import commands
from random import shuffle
import requests

# get environment from .env file
load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='<BIZ>')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def junkyard(ctx, p1: str, p2: str, p3: str, p4: str, p5: str):
    # constant role index's
    TOP, JG, MID, BOT, SUP = 0, 1, 2, 3, 4

    roles = [r.lower() for r  in [p1, p2, p3, p4, p5]]
    shuffle(roles)

    # calvin jungle nunu hack
    calvin_str = ""
    if 'calvin' in roles:
        calvin_index = roles.index('calvin')
        roles[calvin_index], roles[JG] = roles[JG], roles[calvin_index]
        calvin_str =  " (as nunu)"

    # flora support morgana hack
    flora_str = ""
    if 'flora' in roles:
        flora_index = roles.index('flora')
        roles[flora_index], roles[SUP] = roles[SUP], roles[flora_index]
        flora_str =  " (as morgana)"


    await ctx.channel.send(
        f"Top: {roles[TOP]}\n"
        f"Jungle: {roles[JG]}{calvin_str}\n"
        f"Mid: {roles[MID]}\n"
        f"Bottom: {roles[BOT]}\n"
        f"Support: {roles[SUP]}{flora_str}\n"
    )


@bot.command()
async def memes(ctx, subreddit='leagueofmemes'):
    response = requests.get(f"https://meme-api.herokuapp.com/gimme/{subreddit}").json()

    if 'code' in response:
        # error
        await ctx.channel.send(f"{response.get('code')} - {response.get('message')}")
    else:
        # success
        await ctx.channel.send(response.get('url'))


# @bot.event
# async def on_message(message):
#     print(message)
#     await bot.process_commands(message)


bot.run(TOKEN)