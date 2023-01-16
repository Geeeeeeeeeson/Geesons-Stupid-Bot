"""Fun commands"""

import discord
from discord.ext import commands

import random

import file_storage


class Fun(commands.Cog, name='fun'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='8ball', description='Lucky 8ball', usage='8ball <question>',
                      aliases=['magic8ball', 'magicball', 'ball'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def eightball(self, ctx, *, msg):
        if file_storage.user_data[ctx.author.id]['is_banned']:
            return
        await ctx.send(random.choice(['Try asking again later.',
                                      'Not sure.',
                                      'Think harder.',
                                      'Yes!',
                                      'Maybe.',
                                      'Absolutely Not.',
                                      'My source say no.',
                                      'Most likely!',
                                      'Very doubtful.',
                                      'Don\'t count on it.',
                                      'It is certain.',
                                      'As I see it, yes.',
                                      'Outlook not so good.',
                                      'My reply is no.',
                                      'Better not tell you now.',
                                      'Signs point to yes.',
                                      'You may relay on it.', ]))

    @commands.command(name='backwards', aliases=['bw'], description='sdrawkcab ti yas lliw I dna gnihtemos em llet uoY',
                      usage='backwards <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def backwards(self, ctx, *, msg):
        if file_storage.user_data[ctx.author.id]['is_banned']:
            return
        await ctx.send(msg[::-1])

    @commands.command(name='impostor',
                      description='this commands sends a webhook with the other users name and profile picture',
                      usage='impostor <user> <message>')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def impostor(self, ctx, i_user: discord.User, *, msg):
        if file_storage.user_data[ctx.author.id]['is_banned']:
            return
        hooks = await ctx.channel.webhooks()
        hook = discord.utils.get(hooks, name='Geeson\'s Stupid Bot')
        if hook is None:
            hook = await ctx.channel.create_webhook(name='Geeson\'s Stupid Bot', avatar=None, reason=None)
        await hook.send(content=msg, username=i_user.name, avatar_url=i_user.avatar.url)
        await ctx.message.delete()


async def setup(client):
    await client.add_cog(Fun(client))
