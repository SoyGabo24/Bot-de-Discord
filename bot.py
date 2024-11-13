import discord
from discord.ext import commands
import random
from datetime import datetime, timedelta
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

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
async def roll(ctx, dice: str):
    """Rolls a dice in 6 format."""
    try:
        rolls, limit = map(int, dice.split('6'))
    except Exception:
        await ctx.send('Format has to be in 6!')
        return

    result = ', '.join(str(random.randint(1, 6)) for r in range(rolls))
    await ctx.send(result)
@bot.command()
async def randomdate(ctx):
    # Crea la fecha random del año
    start_date = datetime(datetime.now().year, 1, 1)
    random_days = random.randint(0, 364)  # Un año tiene 365 dias xd
    random_date = start_date + timedelta(days=random_days)

    # Envia la fecha al usuario (en este caso nosotros)
    await ctx.send(f'Your random date is: {random_date.strftime("%B %d, %Y")}')
@bot.command()
async def meme(ctx):
    with open('Imagenes/Meme 1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def memesrandom(ctx):
    memes = os.listdir("Imagenes")
    with open(f'Imagenes/{random.choice(memes)}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
def perro():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = perro()
    await ctx.send(image_url)
@bot.command()
async def fortnitestrats(ctx):
    await ctx.send(f'Te voy a hablar acerca de como puedes subir de rango en fortnite')
    await ctx.send(f'El subir de rango puede ayudarte a mejorar tus skills y mecanicas')
    # Enviar una pregunta al usuario
    await ctx.send("Quieres algunas strats para poder subir de rango en fortnite? Responde con 'sí' o 'no'.")
# Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("1. Jugar de manera inteligente, cae en un lugar del mapa en el cual no caiga nadie para poder lootear facilmente")
            await ctx.send("2. Cuando ya tengas un inventario decente, puedes pushear e ir al rush para poder ganar kills y al mismo tiempo un buen posicionamiento")
            await ctx.send("3. Tener el cuenta que el rango se sube más rapido con un buen team, puedes jugar con un amigo q sea bueno para que los dos puedan subir")  
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Quieres saber más acerca de este tema? Responde con 'si' o 'no'.")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['sí', 'si']:
            await ctx.send("Cuando juegas bien tus partidas, usualmente el matchmaking te puede emparejar con gente buena, usa eso como ventaja cuando juegue en duos fill") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
bot.run("Your Token")
