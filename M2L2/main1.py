import discord


from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')


@bot.command()
async def carton(ctx):
    await ctx.send("""
CARTÓN – organizador de escritorio

Materiales:
Caja de cartón (tipo zapatillas o alimentos)
Tijera o cutter
Pegamento o cinta
Papel para decorar (opcional)

Instrucciones:
Elegí una caja resistente.
Cortá divisiones internas según lo que quieras ordenar (lápices, papeles, etc.).
Pegá las divisiones dentro de la caja para fijarlas.
Reforzá bordes con cinta si es necesario.
Decorá el exterior si querés hacerlo más prolijo.


PISTA DE AUTOS

Materiales:
Cartón grande
Tubos de papel o rollos de cocina
Cinta adhesiva
Autos pequeños

Instrucciones:
Armá una base con el cartón.
Usá tubos de cartón como rampas o túneles.
Pegá los tubos inclinados para crear bajadas.
Armá caminos conectando las rampas.
Probá con autos y ajustá inclinaciones.
""")




@bot.command()
async def plastico(ctx):
    await ctx.send("""


""")


@bot.command()
async def papel(ctx):
    await ctx.send("""


""")


@bot.command()
async def tapas(ctx):
    await ctx.send("""TAPITAS
juego de memoria
Materiales
Tapitas iguales
Papel o cartulina
Pegamento
Instrucciones
      1. Cortá círculos pequeños de papel.
      2. Dibujá pares de símbolos iguales.
      3. Pegá uno en cada tapita.
      4. Mezclá todas las tapitas boca abajo.
      5. Jugá encontrando pares iguales.


""")


@bot.command()
async def latas(ctx):
    await ctx.send("""LATAS 
portalápices 
Materiales 
Lata vacía limpia 
Pintura o papel decorativo 
Pegamento 
Instrucciones 
1.  Limpiá bien la lata y secala. 
2.  Cubrí bordes cortantes con cinta o papel. 
3.  Decorá el exterior. 
4.  Usalo para guardar lápices o herramientas. 
 


""")

@bot.command()
async def descargar(ctx):
await ctx.send(file=discord.File("Info reciclabot-300.pdf"))


bot.run("MTQ5MjI3NzYwMDI1NTYxMTA1MA.GkoWsf.zObrZ31hTFsRSoq0F5XrKtnb-F2W4Gstkjewk0")