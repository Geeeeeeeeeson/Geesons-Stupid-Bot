#! /usr/bin/env python3

import discord
from discord.ext import commands
from discord.ext import tasks

import asyncio
import pathlib as pl
import signal
import sys

import file_storage
from constants import Color
from file_storage import guild_data


def terminate_handler(signal, frame):
    print(f'\n{Color.red}Caught termination signal, exiting.{Color.end}')
    file_storage.save_all()
    sys.exit(0)


signal.signal(signal.SIGINT, terminate_handler)


intents = discord.Intents.all()


with open('client.token', 'r') as f:
    token = f.readline().strip()


def custom_prefix(client, message):
    if message.guild.id in guild_data:
        return guild_data[message.guild.id]['prefix']
    else:
        return 'bot '


client = commands.Bot(command_prefix=custom_prefix, intents=intents)
client.remove_command('help')


async def load_ext():
    p = pl.Path('./cogs')
    for file in [path for path in p.iterdir() if path.is_file()]:
        await client.load_extension(f'cogs.{file.name[:-3]}')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='bot help'))
    print(f'{Color.green}Logged in{Color.end}')


@tasks.loop(minutes=10.0)
async def save():
    file_storage.save_all()


async def main():
    print(f'{Color.cyan}Geeson\'s Stupid Bot VERSION {constants.VERSION}')
    save.start()
    await load_ext()
    await client.start(token)


if __name__ == '__main__':
    asyncio.run(main())
