import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def animales(ctx):
    img_name = random.choice(os.listdir('images/animales'))
    with open(f'images/animales/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)




bot.run("MTQ4NzIwNTQ1NjU5MzE1ODIxNA.Gz2Ul1.1t9kla7sSi0mGl4IKsNp0WBFYvEG-MlvmseLkY")