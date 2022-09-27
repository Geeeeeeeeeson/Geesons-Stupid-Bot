"""Moderation Commands"""


import discord
from discord.ext import commands

import asyncio
import string

from utils.file_storage import guild_data as config


class Moderation(commands.Cog, name='moderation'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.channel.id in config[message.guild.id]['antidelete']:
            if message.content[0] == '≪':
                return
            await message.channel.send(f'≪{message.author.mention}≫ {message.content}',
                                       allowed_mentions=discord.AllowedMentions(everyone=False, users=False,
                                                                                roles=False))

    @commands.command(name='prefix', description='change the prefix for the server', usage='prefix [prefix]')
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx, *, msg: str = ''):
        if len(msg) > 10:
            await ctx.send('You may not have a prefix longer than 10 characters.')
            return
        if msg.lower() == 'reset' or msg == '' or msg.lower() == 'bot':
            config[ctx.guild.id]['prefix'] = 'bot '
            await ctx.channel.send(f'Reset the prefix to `bot`.')
            return
        if msg[-1] not in string.punctuation and msg[-1] not in string.digits:
            msg += ' '
        config[ctx.guild.id]['prefix'] = msg
        await ctx.channel.send(
            f'Successfully set the prefix to `{msg}`.\n\nIf your prefix ends with a symbol or number, you do not have '
            f'the add a space between the prefix and the command.')

    @commands.command(name='kick', description='kick users', usage='kick <user> [reason]')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason: str = ''):
        if user == self.client.user:
            await ctx.channel.send("You can't kick me with my own command you know.")
            return
        if user == ctx.guild.owner:
            await ctx.channel.send('That\'s the owner you dumbo.')
            return
        if user == ctx.author:
            await ctx.channel.send('Do you want me to kick you or no?')
            return
        await ctx.guild.kick(user, reason=reason)
        await ctx.channel.send(f'Successfully kicked **{user}**.')
        await user.send(f'You got kicked from **{ctx.guild.name}** by: {ctx.author}, reason: {reason}')

    @commands.command(name='ban', description='ban users', usage='ban <user> [reason]')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User, *, reason=''):
        if user == self.client.user:
            await ctx.channel.send("You can't ban me with my own command you know.")
            return
        if user == ctx.guild.owner:
            await ctx.channel.send('That\'s the owner you dumbo.')
            return
        if user == ctx.author:
            await ctx.channel.send('Do you want me to ban you or no?')
            return
        await ctx.guild.ban(user, reason=reason)
        await ctx.channel.send(f'Successfully banned **{user}**.')
        await user.send(f'You got banned from **{ctx.guild.name}** by: {ctx.author}, reason: {reason}')

    @commands.command(name='purge', aliases=['delete'], description='delete multipul messages at once',
                      usage='purge [amount]')
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def purge(self, ctx, amount: int = 2):
        if amount <= 1:
            return await ctx.channel.send('You must at least delete 2 messages.')
        await ctx.channel.purge(limit=amount + 1)
        msgpr = await ctx.channel.send(f'Successfully purged **{amount}** messages.')
        await asyncio.sleep(1)
        await msgpr.delete()

    @commands.command(name='antidelete', description='make users unable to delete messages', usage='antidelete')
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def antidelete(self, ctx):
        if ctx.channel.id not in config[ctx.guild.id]['antidelete']:
            config[ctx.guild.id]['antidelete'].append(ctx.channel.id)
            await ctx.channel.send('Turned on antidelete for this channel.')
        else:
            config[ctx.guild.id]['antidelete'].remove(ctx.channel.id)
            await ctx.channel.send('Turned off antidelete for this channel.')

    @commands.command(name='slowmode', aliases=['sm'], description='set custom slowmodes', usage='slowmode <time>')
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def slowmode(self, ctx, slowmode: int = 0):
        if slowmode < 0:
            await ctx.channel.send("Your slowmode can't be a negative number")
        if slowmode > 21600:
            await ctx.channel.send(f'Your int ({slowmode}) cannot be larger than **21600**.')
        await self.client.get_channel(ctx.channel.id).edit(reason='custom slowmode', slowmode_delay=int(slowmode))
        await ctx.channel.send(f'Set slowmode of <#{ctx.channel.id}> to **{slowmode}** seconds.')


async def setup(client):
    await client.add_cog(Moderation(client))
