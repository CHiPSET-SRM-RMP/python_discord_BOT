#music functionality
import discord
from discord import voice_client
from discord.client import client
from discord.ext import commands

@client.command()
async def startq(ctx):
    voicechannel = discord.utils.get(ctx.guild.channels, name='queue')
    vc = await voicechannel.connect()
    vc.play(discord.FFmpegPCMAudio("countdown.wav"), after=lambda e: print('done', e))
