import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def add(ctx, left, right):
    try:
        left = int(left)
        right = int(right)
        await ctx.send(left + right)
    except ValueError:
        await ctx.send("Debes poner dos números enteros!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


bot.run("MTQ4MjEzMTgxNDYzNzM3NTcyOQ.GjOCnM.xqSkrCOcyME4_6I5Ws0nCL76tj2TwJliOQL49s")