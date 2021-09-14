import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is ready and online!")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    await channel.send(f"Quack! Quack! {member.mention} has made it! Give them a warm, cozy hug <3 :')")

@bot.command(name='quack')
async def quack(ctx):
    response = "Quack! Quack! :) <3"
    await ctx.send(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "Quack!":
        await message.channel.send("Quack! Quack! <33")


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)