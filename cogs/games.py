"""Games commands"""


import discord
from discord.ext import commands

import asyncio
import random

from english_words import english_words_lower_set


class Game(commands.Cog, name='games'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='hangman', description='don\'t kill innocent people', usage='hangman')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def hangman(self, ctx):
        answer = random.sample(english_words_lower_set, 1)
        joinanswer = ' '.join(answer)
        display = []
        display.extend(joinanswer)
        for i in range(len(display)):
            display[i] = '`_`'
        joindisplay = ' '.join(display)
        # clue = dictionary.meaning(joinanswer)
        # msg = await ctx.channel.send(f'Time to play hangman:\n**CLUE**:{clue}\n{joindisplay}')
        msg = await ctx.channel.send(f'Time to play hangman:\n{joindisplay}')
        msg2 = await ctx.channel.send('** **\n    ___\n   |\n   |\n   |\n   |\n   |\n-----')
        count = 0
        deaths = 0
        charactersn = []
        usedcharacters = []
        charactersjoin = ' '.join(charactersn)
        while count < len(joinanswer):
            if deaths == 1:
                await msg2.edit(content='** **\n    ___\n   |   O\n   |\n   |\n   |\n   |\n-----')
            elif deaths == 2:
                await msg2.edit(content='** **\n    ___\n   |   O\n   |    |\n   |\n   |\n   |\n-----')
            elif deaths == 3:
                await msg2.edit(content='** **\n    ___\n   |   O\n   | \ |\n   |\n   |\n   |\n-----')
            elif deaths == 4:
                await msg2.edit(content='** **\n    ___\n   |   O\n   | \ | /\n   |\n   |\n   |\n-----')
            elif deaths == 5:
                await msg2.edit(content='** **\n    ___\n   |   O\n   | \ | /\n   |   /\n   |\n   |\n-----')
            elif deaths == 6:
                return await msg2.edit(
                    content=f'** **\n    ___\n   |   O\n   | \ | /\n   |   /\ \n   |\n   |\n-----\n**YOU LOSE, The word is `{joinanswer}`**')
            try:
                msg3 = await self.client.wait_for('message', timeout=30, check=lambda
                    msg: msg.author == ctx.author and msg.channel == ctx.channel)
            except asyncio.TimeoutError:
                return await ctx.channel.send('Timed out, game canceled.')
            else:
                guess = msg3.content[0]
                guess = guess.lower()
                for i in range(len(joinanswer)):
                    if joinanswer[i] == guess:
                        display[i] = f'`{guess}`'
                        if str(guess) not in usedcharacters:
                            count += 1
                            # await msg3.add_reaction('\u2705')
                usedcharacters.append(guess)
                if str(guess) not in joinanswer:
                    deaths += 1
                    # await msg3.add_reaction('\u274c')
                    if str(guess) not in charactersn:
                        charactersn.append(guess)
                joindisplay = ' '.join(display)
                charactersjoin = ' '.join(charactersn)
                # await msg.edit(content=f'Time to play hangman:\n**CLUE**:{clue}\nInvaild Characters: {charactersjoin}\n{joindisplay}')
                await msg.edit(content=f'Time to play hangman:\nInvaild Characters: {charactersjoin}\n{joindisplay}')
        await ctx.channel.send(f'🥳 **GG, the word was `{joinanswer}`** 🥳')


def setup(client):
    client.add_cog(Game(client))
