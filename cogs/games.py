"""Games commands"""

import discord
from discord.ext import commands

import asyncio
import random

from english_words import english_words_lower_set

import file_storage


class Game(commands.Cog, name='games'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='hangman', description='don\'t kill innocent people', usage='hangman')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def hangman(self, ctx):

        if file_storage.user_data[ctx.author.id]['is_banned']:
            return

        hangman_ui = {0: '** **\n    ___\n   |\n   |\n   |\n   |\n   |\n-----',
                      1: '** **\n    ___\n   |   O\n   |\n   |\n   |\n   |\n-----',
                      2: '** **\n    ___\n   |   O\n   |    |\n   |\n   |\n   |\n-----',
                      3: '** **\n    ___\n   |   O\n   | \ |\n   |\n   |\n   |\n-----',
                      4: '** **\n    ___\n   |   O\n   | \ | /\n   |\n   |\n   |\n-----',
                      5: '** **\n    ___\n   |   O\n   | \ | /\n   |   /\n   |\n   |\n-----',
                      6: '** **\n    ___\n   |   O\n   | \ | /\n   |   /\ \n   |\n   |\n-----', }

        answer = ' '.join(random.sample(english_words_lower_set, 1))
        display = ['`_`' for i in range(len(answer))]
        count = 0
        deaths = 0
        invalid_char = []
        char_used = []

        hangman_header = await ctx.channel.send(f'Time to play hangman:\n{" ".join(display)}')
        hangman_game_msg = await ctx.channel.send(hangman_ui[deaths])

        while count < len(answer):
            await hangman_game_msg.edit(content=hangman_ui[deaths])
            if deaths == 6:
                await hangman_header.edit(
                    content=f'Time to play hangman:\nInvaild Characters: {" ".join(invalid_char)}\n{" ".join(display)}\n**the word was `{answer}`**')
                return
            try:
                user_input = await self.client.wait_for('message', timeout=30, check=lambda
                    msg: msg.author == ctx.author and msg.channel == ctx.channel)
            except asyncio.TimeoutError:
                return await ctx.channel.send('Timed out, game canceled.')
            else:
                guess = user_input.content[0]
                guess = guess.lower()
                answer_guess = [i for i, s in enumerate(answer) if s == guess]
                if answer_guess:
                    for i in answer_guess:
                        display[i] = f'`{guess}`'
                    count += 1
                    if guess not in char_used:
                        char_used.append(guess)
                if not answer_guess and guess not in invalid_char:
                    deaths += 1
                    invalid_char.append(guess)
                await hangman_header.edit(
                    content=f'Time to play hangman:\nInvaild Characters: {" ".join(invalid_char)}\n{" ".join(display)}')
        await ctx.channel.send(f'🥳 **GG, the word was `{answer}`** 🥳')


async def setup(client):
    await client.add_cog(Game(client))
