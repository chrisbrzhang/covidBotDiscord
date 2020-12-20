import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

client.run('Nzg5NjE4NTgxMzM5MzczNjA5.X90rnA.YVp1N3WXN__xdowuFh4VtAmx98Y')