'''
discord bot 
28/6/2020
kartik tripathi
'''

#importing modules
import discord
import logging
import json
import Music
import Basic_functionalities
from discord import user
from discord.ext import commands


'''
# importing logger and loging all the process of bot in a text file.
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
'''


#making bot (intent are the previlage esclation for the bot so that it can access the member lisst or the the gluid)
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

def get_prefix(client, message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, intents = intents)

# assigning tprefix acc to server.


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Karnatus'))
    print("Bot's up and running")

@client.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
        
    prefixes[str(guild.id)] = '. '
    
    with open('prefixes.json','w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
        prefixes.pop(str(guild.id))
        with open('prefixes.json','w') as f:
            json.dump(prefixes,f,indent=4)

@client.command()
async def change_prefix(ctx, prefix):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open('prefixes.json','w') as f:
            json.dump(prefixes, f, indent = 4)
            await ctx.send(f'prefix changed to {prefix}') 



# calling bot
client.run('ODU4NjA0NDk3NzY4MDIyMDI2.YNgjwA.ir62cwQsbo10p0pkHGMoK4OLWz8')
