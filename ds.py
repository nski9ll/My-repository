import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx, member: discord.Member):
    await ctx.send(f'Cześć,{member.name}, jestem bot {bot.user} !')

@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')
bot.run("MTE2MjA1MjM0MzM4NzM5NDEzOQ.Gg3zPf.CCkbREzhR65lQeCrolHRbvnw7Z1rBF_-nM1Ods")
