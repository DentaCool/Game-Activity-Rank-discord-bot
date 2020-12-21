import discord
from discord.ext import commands
import os

# TODO: change prefix for server by command
client = commands.Bot(command_prefix='$')


def init_bot_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(filename)


@client.event
async def on_ready():
    print("Ready!")
    custom = discord.Game(name="")
    init_bot_cogs()
    await client.change_presence(status=discord.Status.idle, activity=custom)


if __name__ == '__main__':
    client.run(os.getenv("TOKEN"))
