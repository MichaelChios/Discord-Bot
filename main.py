import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
# from keep_alive import keep_alive

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)
commandDict = {"?": "Private message", "!clear": "Clears all messages in the channel", "!join": "Joins the voice channel", "!play <url>": "Plays music from the URL",
               "!help": "Displays all commands"}

# Connection to the server
@bot.event
async def on_ready():
    print(f'I have logged in as {bot.user}')

# Respond to messages
@bot.event
async def on_message(message):
    if (message.author == bot.user):
        return
    
    # Private message
    if (message.content.startswith('?')):
        await message.author.send('Hello!')
    
    # Clear messages
    elif (message.content.startswith('!clear')):
        await message.channel.purge()
        await message.channel.send('Messages have been cleared!')
        
    # Join a voice channel
    elif (message.content.startswith('!join')):
        if (message.author.voice):
            channel = message.author.voice.channel
            await channel.connect()
        else:
            await message.channel.send('You are not in a voice channel!')
            
    # Play music
    elif (message.content.startswith('!play')):
        if (message.author.voice):
            channel = message.author.voice.channel
            voice = discord.utils.get(bot.voice_clients, guild=message.guild) # Check if bot is already in a voice channel
            if (not voice):
                voice = await channel.connect()
            url = message.content.split(' ')[1]
            voice.play(discord.FFmpegPCMAudio(url))
        else:
            await message.channel.send('You are not in a voice channel!')
            
    # Kick a member (Doesn't work)
    elif (message.content.startswith('!kick')):
        if (message.author.guild_permissions.kick_members):
            member = message.mentions[0]
            await member.kick()
            await message.channel.send(f'{member} has been kicked!')
        else:
            await message.channel.send('You do not have the permission to kick members!')
            
    # Show permissions
    elif (message.content.startswith('!permissions')):
        permissions = message.author.guild_permissions
        await message.channel.send(f'{message.author} has the following permissions: {permissions}')
    
    # Help command    
    elif (message.content.startswith('!help')):
        await message.channel.send('Here are the commands you can use: ')
        for key, value in commandDict.items():
            await message.channel.send(f'{key}: {value}')
        
    # General message
    else:
        await message.channel.send('Hello!')

load_dotenv()
# keep_alive()
bot.run(os.getenv('TOKEN'))
