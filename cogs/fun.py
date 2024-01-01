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
        await ctx.send(msg[::-1])

async def setup(client):
    await client.add_cog(Fun(client))
