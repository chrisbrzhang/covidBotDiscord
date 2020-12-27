import discord
import csv
from discord.ext import commands
import asyncio
import time 
import csv
import pandas as pd 
import os



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
async def main(): #Insert discord Token here.
    await client.start('Discord Token')
    
@client.command()
async def ping(ctx):
    await ctx.send('Ping is ' + str(round(client.latency*1000)) + 'ms' )
   
@client.command()
async def link(ctx):
    await ctx.send('https://www.worldometers.info/coronavirus/country/')

@client.command()
async def country(ctx,arg):
    await ctx.send("Running..... ")
    os.system('python Corona_Reader.py') #must have a file called Corona_Reader.py in same directry
    col_list = ["Country", "Total_Cases","New_Cases","Total_Death"]
    df = pd.read_csv("covidBOT_data.csv", usecols=col_list)
    country = str(arg)
    counter = 0
    for row in range(0,len(df)):
        if(df["Country"][row]== country and counter == 0):
            await ctx.send("Total Cases: ")
            await ctx.send(df["Total_Cases"][row])
            await ctx.send("New Cases: ")
            await ctx.send(df["New_Cases"][row])
            await ctx.send("Total Death ") 
            await ctx.send(df["Total_Death"][row])
            counter = counter+1   
            break
        elif(row == len(df)-1):
            await ctx.send("Your Country does not Exist! Use correct Capitals and Spelling")

loop=asyncio.get_event_loop() 
loop.run_until_complete(main())