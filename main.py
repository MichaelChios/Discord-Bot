import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
# from keep_alive import keep_alive

#client = discord.Client() # Client instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
commandDict = {"?": "Private message", "!clear": "Clears all messages in the channel", "!join": "Joins the voice channel"}

# Connection to the server
@bot.event
async def on_ready():
    print(f'I have logged in as {bot.user}')

# Responding to messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Private message
    if message.content.startswith('?'):
        await message.author.send('Hello!')
    
    # Clearing messages
    elif message.content.startswith('!clear'):
        await message.channel.purge()
        await message.channel.send('Messages have been cleared!')
        
    # Join a voice channel
    elif message.content.startswith('!join'):
        if (message.author.voice):
            channel = message.author.voice.channel
            await channel.connect()
        else:
            await message.channel.send('You are not in a voice channel!')
            
    elif (message.content.startswith('!help')):
        await message.channel.send('Here are the commands you can use: ')
        for key, value in commandDict.items():
            await message.channel.send(f'{key}: {value}')
        
    # General message
    else:
        await message.channel.send('Hello!')
        
# Disconnect from voice channel (Doesn't work)
@bot.command()
async def disconnect(ctx):
    if ctx.voice_client is None:
        await ctx.send("I'm not connected to a voice channel.")
    else:
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected from the voice channel.")

load_dotenv()
# keep_alive()
bot.run(os.getenv('TOKEN'))
