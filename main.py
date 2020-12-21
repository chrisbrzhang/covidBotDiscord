import discord
import csv
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

f = open('covidBOT_data.csv')
csv_f = csv.reader(f)

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_leave(member):
    print(f'{member} has left the server')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

        if message.content.startswith('!IM'): ##need the csv file
            msg = 'Current number of cases are:\n'
            await channel.send(msg)
            for row in csv_f:
                await channel.send(('send the csv content'))
        else:
            await message.delete()

            


@client.command()
async def IM(ctx, arg):
    await ctx.send('https://www.worldometers.info/coronavirus/country/' + arg)





client.run('Nzg5NjE4NTgxMzM5MzczNjA5.X90rnA.YVp1N3WXN__xdowuFh4VtAmx98Y')