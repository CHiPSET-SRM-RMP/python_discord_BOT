#music functionality
import discord
from discord import voice_client
from discord.ext import commands

@client.event
async def connect(* reconnect ,timeout = 10):
await voice_client()
    await ctx.send('the bot is connected')
@client.command()
async def ping(ctx):
    await ctx.send(f'pong!{round(client.latency*1000)}ms')