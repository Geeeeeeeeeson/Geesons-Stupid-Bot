"""Image commands"""


import discord
from discord.ext import commands

import os

import art
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import file_storage
import utils


class ImageCog(commands.Cog, name='image'):

    def __int__(self, client):
        self.client = client

    @commands.command(name='ascii', description='ascii art', usage='ascii <text>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ascii(self, ctx, *, msg):
        ascii_art = art.text2art(msg, font='random')
        with open('_ascii.temp.txt', 'w+') as f:
            f.write(ascii_art)
        await ctx.channel.send(file=discord.File('_ascii.temp.txt'))

    @commands.command(name='clippy', aliases=['paperclip'],
                      description='It looks like your writing a letter, would you like some help?',
                      usage='clippy <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def clippy(self, ctx, *, msg: str):
        image = Image.open('assets/clippy.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 20)
        draw.text((51, 34), utils.bend(msg, 30), fill=(0, 0, 0), font=font)
        image.save('_clippy.png')
        await ctx.send(file=discord.File('_clippy.png'))

    @commands.command(name='ohnoes', description='Oh noes', usage='ohnoes <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ohnoes(self, ctx, *, msg: str):
        await ctx.send('a')
        image = Image.open('assets/ohnoes.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 15)
        draw.text((172, 66), utils.bend(msg, 33), fill=(0, 0, 0), font=font)
        image.save('_ohnoes.png')
        await ctx.send(file=discord.File('_ohnoes.png'))


async def setup(client):
    await client.add_cog(ImageCog(client))
