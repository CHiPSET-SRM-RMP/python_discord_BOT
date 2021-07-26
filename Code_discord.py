'''
discord bot 
28/6/2020
kartik tripathi
'''

#importing modules
import discord
import logging
import json
import random
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
        
    prefixes[str(guild.id)] = '.'
    
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

#assigning task


@client.command()
async def ping(ctx):
    await ctx.send(f'pong!{round(client.latency*1000)}ms')

@client.event
async def on_member_join(member):
    print(f'{member} has joined')
    
@client.event
async def on_member_remove(member):
    print(f'{member} has been removed')

@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ban(ctx,member:discord.member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx,*,member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator)==(member_name,-member.discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned{user.mention}')
            return

@client.command(alias = ['8 ball','test'])
async def _8ball(ctx,*,question):
    responces = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question:{question}\n Answer: {random.choice(responces)}')

# calling bot
client.run('ODU4NjA0NDk3NzY4MDIyMDI2.YNgjwA.ir62cwQsbo10p0pkHGMoK4OLWz8')
