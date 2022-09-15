import discord
from discord.ext import commands

import math

import utils.constants


class Configuration(commands.Cog, name='configuration'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='serverinfo', aliases=['guildinfo', 'guild', 'server'],
                      description='check server information', usage='serverinfo')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverinfo(self, ctx):
        if not ctx.guild.features:
            features = 'None'
        else:
            features = '\n'.join(ctx.guild.features)
        channel_amount = len(ctx.guild.text_channels)
        vc_amount = len(ctx.guild.voice_channels)
        level2fa = {discord.MFALevel.require_2fa: "Enabled",
                    discord.MFALevel.disabled: 'Disabled'}
        creation_date = math.floor(ctx.guild.created_at.timestamp())
        embed = discord.Embed(title='Server Info', color=utils.constants.random_color())
        embed.set_author(name=f'{ctx.guild}', icon_url=ctx.guild.icon.url)
        embed.add_field(name='Basic',
                        value=f'**Member Count:** {ctx.guild.member_count}\n**Creation Date:** <t:{creation_date}> (<t:{creation_date}:R>)\n**Owner:** <@!{ctx.guild.owner_id}>\n**Text Channels:** {channel_amount}\n**Voice Channels:** {vc_amount}')
        embed.add_field(name='Security',
                        value=f'**2fa:** {level2fa[ctx.guild.mfa_level]}\n**Verification Level:** {ctx.guild.verification_level}')
        embed.add_field(name='Features', value=f'{features}', inline=False)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.channel.send(embed=embed)

    @commands.command(name='userinfo', aliases=['user'], description='check user information', usage='userinfo <user>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        creation_date = math.floor(user.created_at.timestamp())
        embed = discord.Embed(title='User Info', color=utils.constants.random_color())
        embed.set_author(name=f'{user}', icon_url=user.avatar.url)
        embed.add_field(name='ID', value=f'{user.id}')
        embed.add_field(name='Creation Date', value=f'<t:{creation_date}> (<t:{creation_date}:R>)')
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.channel.send(embed=embed)


async def setup(client):
    await client.add_cog(Configuration(client))
