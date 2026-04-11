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
- Caja de cartón (tipo zapatillas o alimentos)
- Tijera o cutter
- Pegamento o cinta
- Papel para decorar (opcional)

Instrucciones:
1. Elegí una caja resistente.
2. Cortá divisiones internas según lo que quieras ordenar (lápices, papeles, etc.).
3. Pegá las divisiones dentro de la caja para fijarlas.
4. Reforzá bordes con cinta si es necesario.
5. Decorá el exterior si querés hacerlo más prolijo.


PISTA DE AUTOS

Materiales:
- Cartón grande
- Tubos de papel o rollos de cocina
- Cinta adhesiva
- Autos pequeños

Instrucciones:
1. Armá una base con el cartón.
2. Usá tubos de cartón como rampas o túneles.
3. Pegá los tubos inclinados para crear bajadas.
4. Armá caminos conectando las rampas.
5. Probá con autos y ajustá inclinaciones.
""")




@bot.command()
async def plastico(ctx):
    await ctx.send("""
PLÁSTICO
                   
maceta con botella
                   
Materiales
                   
1- Botella plástica
2- Tijera
3- Tierra y planta
4- Pintura (opcional)
5- Instrucciones
6- Cortá la botella a la mitad.
7- Usá la parte inferior como maceta.
8- Hacé agujeros pequeños en la base para drenaje.
9- Llená con tierra y plantá una semilla o planta.
10- Decorá si querés.
                   
                   
""")


@bot.command()
async def papel(ctx):
    await ctx.send("""
PAPEL
                   
máscaras de personajes
                   
MATERIALES
                   
1- Papel o cartón fino
2- Tijera
3- Marcadores o pintura
4- Elástico o hilo
                   
Instrucciones
                   
1- Dibujá la forma de una cara en el papel.
2- Recortá la máscara.
3- Hacé agujeros para los ojos.
4- Decorá con colores o dibujos.
5- Colocá elástico para sostenerla en la cabeza.
                   
                   
""")


@bot.command()
async def tapas(ctx):
    await ctx.send("""
TAPITAS
                   
juego de memoria
                   
MATERIALES
                   
1- Tapitas iguales
2- Papel o cartulina
3- Pegamento
                   
Instrucciones
                   
      1- Cortá círculos pequeños de papel.
      2- Dibujá pares de símbolos iguales.
      3- Pegá uno en cada tapita.
      4- Mezclá todas las tapitas boca abajo.
      5- Jugá encontrando pares iguales.

""")


@bot.command()
async def latas(ctx):
    await ctx.send("""
LATAS 
                   
portalápices
                    
MATERIALES
                    
1- Lata vacía limpia 
2- Pintura o papel decorativo 
3- Pegamento 
                   
Instrucciones 
                   
1-  Limpiá bien la lata y secala. 
2-  Cubrí bordes cortantes con cinta o papel. 
3-  Decorá el exterior. 
4-  Usalo para guardar lápices o herramientas. 
 

""")



bot.run("MTQ5MjI3NzYwMDI1NTYxMTA1MA.GkoWsf.zObrZ31hTFsRSoq0F5XrKtnb-F2W4Gstkjewk0")
