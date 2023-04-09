"""Economy commands"""

import discord
from discord.ext import commands

import math
import random
import time
from typing import Optional

import constants
import file_storage
import utils
from file_storage import user_data


class Economy(commands.Cog, name='economy'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='profile', description='check the profile of a user', usage='profile [user]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def profile(self, ctx, user: discord.User = None):
        if user_data[ctx.author.id]['is_banned']:
            return

        user = user or ctx.author

        if user not in user_data:
            file_storage.user_update_with_defaults(user.id)

        xp = file_storage.user_data[user.id]['xp']
        level = file_storage.user_data[user.id]['level']
        next_level = file_storage.user_data[user.id]['next_level']
        xp_percentage = round((xp / next_level) * 100, 2)

        wallet = user_data[user.id]['economy']['money']['wallet']
        bank = user_data[user.id]['economy']['money']['bank']
        bank_limit = user_data[user.id]['economy']['money']['bank_limit']
        percentage = round((bank / bank_limit) * 100, 2)
        total = wallet + bank

        badges = [constants.BADGES[i] for i in user_data[user.id]['badge']]

        embed = discord.Embed(color=constants.random_color())
        embed.set_author(name=f'{user.name}\'s Profile', icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
        embed.add_field(name='Badges', value=f'{" ".join(badges)}', inline=False) if badges else None
        embed.add_field(name='XP', value=f'**Level**: {level:,}\n**XP**: {xp:,}/{next_level:,} ({xp_percentage}%)', inline=False)
        embed.add_field(name='Money', value=f'**Total**: {total:,}\n**Wallet**: {wallet:,}\n**Bank**: {bank:,}/{bank_limit:,} ({percentage}%)', inline=False)
        embed.set_thumbnail(url=user.avatar.url if user.avatar else user.default_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name='balance', aliases=['bal'], description='check the balance', usage='balance [user]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def balance(self, ctx, user: discord.User = None):
        if user_data[ctx.author.id]['is_banned']:
            return

        user = user or ctx.author

        if user not in user_data:
            file_storage.user_update_with_defaults(user.id)

        wallet = user_data[user.id]['economy']['money']['wallet']
        bank = user_data[user.id]['economy']['money']['bank']
        bank_limit = user_data[user.id]['economy']['money']['bank_limit']
        percentage = round((bank / bank_limit) * 100, 2)
        total = wallet + bank

        embed = discord.Embed(description=f'Total Money: {total:,}', color=constants.random_color())
        embed.set_author(name=f'{user.name}\'s Balance', icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
        embed.add_field(name='Wallet', value=f'{wallet:,}', inline=False)
        embed.add_field(name='Bank', value=f'{bank:,}/{bank_limit:,} ({percentage}%)', inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='daily', description='claim your daily money', usage='daily')
    async def daily(self, ctx):
        if user_data[ctx.author.id]['is_banned']:
            return

        if user_data[ctx.author.id]['economy']['login']['daily'] > time.time():
            waittime = user_data[ctx.author.id]['economy']['login']['daily'] - time.time()
            await ctx.send(embed=discord.Embed(color=constants.random_color(),
                                               description=f'Please wait **{math.floor(waittime / 3600)}h {math.floor((waittime / 60) % 60) if waittime % 60 != 59 else 59}m** to use this again!'))
            return

        amount = random.randint(1000, 2000)

        user_data[ctx.author.id]['economy']['login']['daily'] = time.time() + 86400
        user_data[ctx.author.id]['economy']['money']['wallet'] += amount
        await ctx.send(f'You have claimed your daily money of **{amount:,}**.')

    @commands.command(name='weekly', description='claim your weekly money', usage='weekly')
    async def weekly(self, ctx):
        if user_data[ctx.author.id]['is_banned']:
            return

        if user_data[ctx.author.id]['economy']['login']['weekly'] > time.time():
            waittime = user_data[ctx.author.id]['economy']['login']['weekly'] - time.time()
            await ctx.send(embed=discord.Embed(color=constants.random_color(),
                                               description=f'Please wait **{math.floor(waittime/86400)}d {math.floor(waittime/3600) % 24 if waittime % 24 != 23 else 23}h {math.ceil((waittime/60) % 60) if waittime % 60 != 59 else 59}m** to use this again!'))
            return

        amount = random.randint(5000, 10000)

        user_data[ctx.author.id]['economy']['login']['weekly'] = time.time() + 604800
        user_data[ctx.author.id]['economy']['money']['wallet'] += amount
        await ctx.send(f'You have claimed your weekly money of **{amount:,}**.')

    @commands.command(name='deposit', aliases=['dep'], description='deposit money into your bank', usage='deposit <amount>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def deposit(self, ctx, amount: str):
        if user_data[ctx.author.id]['is_banned']:
            return

        bank_limit = user_data[ctx.author.id]['economy']['money']['bank_limit']
        bank = user_data[ctx.author.id]['economy']['money']['bank']
        wallet = user_data[ctx.author.id]['economy']['money']['wallet']

        if amount.lower() == 'all' or amount.lower() == 'max':
            amount = bank_limit - bank if bank_limit - bank < wallet else wallet
        else:
            try:
                amount = int(amount)
                amount = wallet if wallet < amount or amount < 0 else amount
                amount = bank_limit - bank if bank_limit - bank < amount else amount
            except ValueError:
                await ctx.send('That\'s not a valid amount!')
                return

        user_data[ctx.author.id]['economy']['money']['wallet'] -= amount
        user_data[ctx.author.id]['economy']['money']['bank'] += amount
        await ctx.send(f'You have successfully deposited **{amount:,}** into your bank!')

    @commands.command(name='withdraw', aliases=['with', 'wd'], description='withdraw money from your bank', usage='withdraw <amount>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def withdraw(self, ctx, amount: str):
        if user_data[ctx.author.id]['is_banned']:
            return

        bank = user_data[ctx.author.id]['economy']['money']['bank']

        if amount.lower() == 'all' or amount.lower() == 'max':
            amount = bank
        else:
            try:
                amount = int(amount)
                amount = bank if bank < amount or amount < 0 else amount
            except ValueError:
                await ctx.send('That\'s not a valid amount!')
                return

        user_data[ctx.author.id]['economy']['money']['wallet'] += amount
        user_data[ctx.author.id]['economy']['money']['bank'] -= amount
        await ctx.send(f'You have successfully withdrawn **{amount:,}** from your bank!')

    @commands.command(name='share', aliases=['give'], description='share money with another user', usage='share <user> <amount>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def share(self, ctx, user: discord.User, amount: str):
        if user_data[ctx.author.id]['is_banned']:
            return

        if user.id == ctx.author.id:
            await ctx.send('You can\'t share money with yourself!')
            return
        if user.bot:
            await ctx.send('You can\'t share money with a bot!')
            return

        if user.id not in user_data:
            file_storage.user_update_with_defaults(user.id)

        wallet = user_data[ctx.author.id]['economy']['money']['wallet']

        if amount.lower() == 'all' or amount.lower() == 'max':
            amount = wallet
        else:
            try:
                amount = int(amount)
                amount = wallet if wallet < amount or amount < 0 else amount
            except ValueError:
                await ctx.send('That\'s not a valid amount!')
                return

        user_data[ctx.author.id]['economy']['money']['wallet'] -= amount
        user_data[user.id]['economy']['money']['wallet'] += amount
        await ctx.send(f'You have successfully shared **{amount:,}** with **{user.name}**!')

    @commands.command(name='inventory', aliases=['inv'], description='view your inventory and others', usage='inventory [user] [page]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def inventory(self, ctx, user: Optional[discord.User] = None, page: Optional[int] = 1):
        if user_data[ctx.author.id]['is_banned']:
            return

        user = user or ctx.author

        if user.id not in user_data or not user_data[user.id]['economy']['inventory']:
            file_storage.user_update_with_defaults(user.id)

        inventory = user_data[user.id]['economy']['inventory']
        total_pages = math.ceil(len(inventory) / 10)
        page = page if page < total_pages else total_pages
        items = [f'**{constants.INVENTORY[item]["emoji"]} {constants.INVENTORY[item]["name"]}** x{inventory[item]}'
                 for i, item in enumerate(inventory) if item != 'pickaxe' and inventory[item] > 0 and
                 item in constants.INVENTORY and (page - 1) * 10 < i <= page * 10]

        embed = discord.Embed(color=constants.random_color())
        embed.set_author(name=f'{user.name}\'s Inventory', icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
        embed.add_field(name='\u26cf\ufe0f Pickaxe', value=f'**Level:** {inventory["pickaxe"]["level"]}') if inventory['pickaxe']['has'] else None
        embed.add_field(name='', value='\n'.join(items) if items else 'User has no items!', inline=False)
        embed.set_footer(text=f'Page {page}/{total_pages}')
        await ctx.send(embed=embed)

    @commands.command(name='beg', description='beg for money', usage='beg')
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def beg(self, ctx):
        if user_data[ctx.author.id]['is_banned']:
            return

        amount = random.randint(100, 350)

        user_data[ctx.author.id]['economy']['money']['wallet'] += amount
        await ctx.send(f'You have begged for **{amount:,}**.')

    @commands.command(name='shop', description='view the shop', usage='shop [page] [item]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def shop(self, ctx, page: Optional[int] = 1, item: Optional[str] = None):
        if user_data[ctx.author.id]['is_banned']:
            return

        if item:

            item = item.lower().strip()

            if item not in constants.INVENTORY:
                await ctx.send('That\'s not a valid item!')
                return

            item = constants.INVENTORY[item]
            embed = discord.Embed(title=f'{item["emoji"]} {item["name"]}', description=item['description'], color=constants.random_color())
            embed.add_field(name='Rarity', value=item['rarity'])
            embed.add_field(name='Type', value=item['type'])
            embed.add_field(name='Price', value=f'{item["price"]:,} coins', inline=False)
            embed.add_field(name='Sell Price', value=f'{item["sell_price"]:,} coins' if item['sellable'] else 'Not Sellable', inline=False)
            await ctx.send(embed=embed)

        else:

            total_pages = math.ceil(len(constants.INVENTORY) / 10)
            page = page if page < total_pages else total_pages

            embed = discord.Embed(title='Shop', description='**Items**', color=constants.random_color())
            for i, item in enumerate(constants.INVENTORY):
                if (page - 1) * 10 <= i < page * 10:
                    item_dict = constants.INVENTORY[item]
                    embed.add_field(name=f'**{item_dict["emoji"]} {item_dict["name"]}** `id: {item}`',
                                    value=f'**Price:** {item_dict["price"]:,} coins', inline=False)
            embed.set_footer(text=f'Page {page}/{total_pages}')
            await ctx.send(embed=embed)

    @commands.command(name='buy', description='buy an item from the shop', usage='buy <item> [amount]')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def buy(self, ctx, item: str, amount: int = 1):
        if user_data[ctx.author.id]['is_banned']:
            return

        item = item.lower().strip()

        if item not in constants.INVENTORY:
            await ctx.send('That\'s not a valid item!')
            return

        item_id = item
        item = constants.INVENTORY[item]
        wallet = user_data[ctx.author.id]['economy']['money']['wallet']

        if wallet < item['price'] * amount:
            await ctx.send('You don\'t have enough money to buy that!')
            return

        if item_id == 'pickaxe':
            if user_data[ctx.author.id]['economy']['inventory']['pickaxe']['has']:
                await ctx.send('You already have a pickaxe!')
                return
            user_data[ctx.author.id]['economy']['inventory']['pickaxe']['has'] = True
            await ctx.send(f'You have successfully bought a **{item["emoji"]} {item["name"]}**.')
        else:
            if item_id not in user_data[ctx.author.id]['economy']['inventory']:
                user_data[ctx.author.id]['economy']['inventory'][item_id] = 0
            user_data[ctx.author.id]['economy']['inventory'][item_id] += amount
            await ctx.send(f'You have successfully bought **{amount}x {item["emoji"]} {item["name"]}**.')

        user_data[ctx.author.id]['economy']['money']['wallet'] -= item['price'] * amount

    @commands.command(name='sell', description='sell items from your inventory', usage='sell <item> [amount]')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sell(self, ctx, item: str, amount: int = 1):
        if user_data[ctx.author.id]['is_banned']:
            return

        item = item.lower().strip()

        if item not in constants.INVENTORY:
            await ctx.send('That\'s not a valid item!')
            return

        item_id = item
        item = constants.INVENTORY[item]

        if item_id == 'pickaxe':
            user_data[ctx.author.id]['economy']['inventory']['pickaxe']['has'] = False
            user_data[ctx.author.id]['economy']['money']['wallet'] += item['sell_price']
            await ctx.send(f'You have successfully sold your **{item["emoji"]} {item["name"]}**.')
            return

        if item_id not in user_data[ctx.author.id]['economy']['inventory']:
            await ctx.send('You don\'t have that item!')
            return
        if user_data[ctx.author.id]['economy']['inventory'][item_id] == 0:
            await ctx.send('You don\'t have that item!')
            return
        if user_data[ctx.author.id]['economy']['inventory'][item_id] < amount:
            await ctx.send('You don\'t have that many items!')
            return
        if not item['sellable']:
            await ctx.send(f'You can\'t sell {item["emoji"]} {item["name"]}!')
            return

        user_data[ctx.author.id]['economy']['inventory'][item_id] -= amount
        user_data[ctx.author.id]['economy']['money']['wallet'] += item['sell_price'] * amount




async def setup(client):
    await client.add_cog(Economy(client))