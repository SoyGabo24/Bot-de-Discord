import discord
from discord.ext import commands
import random
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
TOKEN = "MTI5ODczOTkwNDMxODI3OTczMA.GqXaQ0.8yiC3HLOVMFGZEVHtvhA-BEdu44VTTRNp_DMRY"

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
bot.run("TOKEN")
