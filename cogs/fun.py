import discord
from discord.ext import commands

import random


class Fun(commands.Cog, name='fun'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='8ball', description='Lucky 8ball', usage='8ball <question>',
                      aliases=['magic8ball', 'magicball', 'ball'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def eightball(self, *, msg):
        random.choice(['Try asking again later.',
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
                       'You may relay on it.', ])

    @commands.command(name='backwards', aliases=['bw'], description='sdrawkcab ti yas lliw I dna gnihtemos em llet uoY', usage='backwards <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def backwards(self, ctx, *, msg):
        invalid_char = ['<', '>']
        for i in invalid_char:
            if i in msg:
                return await ctx.channel.send(f'I may not reverse a message with a custom emoji or mention.\nBlacklisted characters `{invalid_char}`')
        await ctx.channel.send(msg[::-1])

    @commands.command(name='impostor', aliases=['imposter', 'sus'], description='this command makes it seem like the other person sent the message', usage='impostor <user> <message>')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def impostor(self, ctx, i_user: discord.User, *, msg):
        hooks = await ctx.channel.webhooks()
        hook = discord.utils.get(hooks, name='Geeson\'s Stupid Bot')
        if hook is None:
            hook = await ctx.channel.create_webhook(name='Geeson\'s Stupid Bot', avatar=None, reason=None)
        await hook.send(content=msg, username=i_user.name, avatar_url=i_user.avatar.url)
        await ctx.message.delete()


async def setup(client):
    await client.add_cog(Fun(client))
