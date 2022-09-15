import discord
from discord.ext import commands

import os

import art
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import utils.utils


class ImageCog(commands.Cog, name='image'):

    def __int__(self, client):
        self.client = client

    commands.command(name='ascii', description='ascii art', usage='ascii <text|image|random> <text-or-image>')

    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ascii(self, ctx, arg0, *, arg1):
        ascii_art = art.text2art(arg1, font='random')
        try:
            with open('._ascii.temp.txt', 'w+') as f:
                f.write(ascii_art)
            # await message.channel.send(f'**NOTE:** Too much character may result in poor formatting.\n```{asciit}```', file=discord.File('._ascii.temp.txt'))
            await ctx.channel.send(file=discord.File('._ascii.temp.txt'))
            os.remove('._ascii.temp.txt')
        except discord.HTTPException:
            await ctx.channel.send('This message is too long to convert to ascii.')
        if arg0.lower() == 'image' or arg0.lower() == 'i':
            await ctx.channel.send('Currently Unsupported.')
        elif arg0.lower() == 'random' or arg0.lower() == 'r':
            ascii_art = art.art("random")
            await ctx.channel.send(f"`{ascii_art}`")
        else:
            await ctx.channel.send('The correct usage is `ascii <text|image> <text-or-image>`.')

    @commands.command(name='clippy', aliases=['paperclip'],
                      description='It looks like your writing a letter, would you like some help?',
                      usage='clippy <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def clippy(self, ctx, *, msg):
        image = Image.open('assests/clippy.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 20)
        text2 = utils.utils.bend(30, msg)
        draw.text((51, 34), f"{text2}", (0, 0, 0), font=font)
        image.save('sample-out-clippy.PNG')
        await ctx.send(file=discord.File('sample-out-clippy.PNG'))
        os.remove('sample-out-clippy.PNG')

    @commands.command(name='ohnoes', description='Oh noes', usage='ohnoes <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ohnoes(self, ctx, *, msg):
        image = Image.open('assests/ohnoes.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 15)
        text2 = utils.utils.bend(33, msg)
        draw.text((172, 66), f"{text2}", (0, 0, 0), font=font)
        image.save('sample-out.PNG')
        await ctx.send(file=discord.File('sample-out.PNG'))
        os.remove('sample-out.PNG')


async def setup(client):
    client.add_cog(ImageCog(client))
