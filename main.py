#! /usr/bin/env python3

import discord
from discord.ext import commands
from discord.ext import tasks

import asyncio
import pathlib as pl
import signal
import sys

import utils.file_storage
from utils.constants import Color


def terminate_handler(signal, frame):
    print(f'\n{Color.red}Caught termination signal, exiting.{Color.end}')
    utils.file_storage.save_all()
    sys.exit(0)


signal.signal(signal.SIGINT, terminate_handler)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


with open('client.token', 'r') as f:
    token = f.readline().strip()


client = commands.Bot(command_prefix='bott ', intents=intents)
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
    utils.file_storage.save_all()


async def main():
    save.start()
    await load_ext()
    await client.start(token)


if __name__ == '__main__':
    asyncio.run(main())
