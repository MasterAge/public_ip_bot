import os

import requests
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


def get_ip() -> str:
    i = requests.get("https://ifconfig.me/ip").text
    return f"{i}:{port}"


port = 25565
server_ip = get_ip()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.command()
async def ip(ctx):
    await ctx.send(server_ip)


@bot.command()
async def refresh(ctx):
    global server_ip
    server_ip = get_ip()
    await ip(ctx)


@tasks.loop(seconds=3600)
async def auto_refresh(self):
    async with self.lock:
        global server_ip
        server_ip = get_ip()


bot.run(TOKEN)
