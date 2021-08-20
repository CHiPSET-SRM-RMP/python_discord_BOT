#music functionality
import discord
from discord import voice_client
from discord import client
from discord import guild
from discord.ext import commands
import Code_discord

@client.command()
async def join(ctx):
    await voice_client.VoiceClient.connect(self, reconnect= True, timeout= None)
    await guild.Guild.change_voice_state(self, channel= '655484906331176970', self_mute= False, self_deaf= False)