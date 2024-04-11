import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
bot.run('lDqVp_vMOs4fc2Moc2EshPNcRKmlepxV')
