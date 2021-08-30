import discord
import os
import discord.ext
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Python Starter Bot is Online")


@client.command()
async def ping(ctx):
    await ctx.send("pong!")


client.run(os.getenv("TOKEN"))
