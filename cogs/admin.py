"""Bot admin commands"""


import discord
from discord.ext import commands

import os

from file_storage import user_data


class Admin(commands.Cog, name='admin'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='pid', aliases=['process'], description='get the process id of the bot.', usage='pid')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pid(self, ctx):
        if user_data[ctx.author.id]['is_admin']:
            await ctx.channel.send(f'This doens\'t really mean anything but:\n`PID:` **{os.getpid()}**')

    @commands.command(name='op', aliases=['operator'], description='bot admins', usage='admin <user>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def op(self, ctx, user: discord.User):
        if user_data[ctx.author.id]['is_admin']:
            if user_data[user.id]['is_admin']:
                await ctx.channel.send('User is already bot admin.')
                return
            user_data[user.id]['is_admin'] = True
            if 'admin' not in user_data[user.id]['badge']:
                user_data[user.id]['badge'].append('admin')
            await ctx.channel.send(f'Successfully made **{user}** bot admin.')

    @commands.command(name='deop', description='deop bot admins', usage='deop <user>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def deop(self, ctx, user: discord.User):
        if user_data[ctx.author.id]['is_admin']:
            if not user_data[user.id]['is_admin']:
                await ctx.channel.send('User is not bot admin.')
                return
            user_data[ctx.author.id]['is_admin'] = False
            if 'admin' in user_data[user.id]['badge']:
                user_data[user.id]['badge'].remove('admin')
            await ctx.channel.send(f'Successfully deoped **{user}**.')

    @commands.command(name='botban', description='bot ban people', usage='botban <user>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def botban(self, ctx, user: discord.User):
        if user_data[ctx.author.id]['is_admin']:
            if not user_data[user.id]['is_banned']:
                user_data[user.id]['is_banned'] = True
                await ctx.channel.send(f'Successfully bot banned **{user}**.')
            else:
                await ctx.channel.send('User was already bot banned.')

    @commands.command(name='botunban', description='unban people from botbanned.', usage='botunban <user>')
    async def botunban(self, ctx, user: discord.User):
        if user_data[ctx.author.id]['is_admin']:
            if user_data[user.id]['is_banned']:
                user_data[user.id]['is_banned'] = False
                await ctx.channel.send(f'Successfully pardoned **{user}**.')
            else:
                await ctx.channel.send('User is not bot banned.')


async def setup(client):
    await client.add_cog(Admin(client))
