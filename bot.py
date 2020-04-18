# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(message)

    if message.content.startswith('jonny'):
        await message.channel.send('is ahri main')
    
    if message.content.startswith('calvin'):
        await message.channel.send('rolls big snowballs')

    if message.content.startswith('flora'):
        await message.channel.send('is a morgana pro')

    if message.content.startswith('djordje'):
        await message.channel.send('is happiest league player')
    
    if message.content.startswith('seth'):
        await message.channel.send('is a bot')
    
    if message.content.startswith('alex'):
        await message.channel.send('is the master..yi')

client.run(TOKEN)