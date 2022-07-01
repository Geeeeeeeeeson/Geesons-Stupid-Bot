#! /usr/bin/env python3.7



###------ Geeson's Stupid Bot ------###
#      Created On: Apr. 2, 2020       #
#     UNIX Timestamp: 1585805700      #
#######################################



###----- Badges id -----###
# admin: bot_admin        #
# 1y: 1 Year Anniversrary #
###########################



#####################################
# Do Not Edit Without Authorization #
# Do Not Edit Without Authorization #
# Do Not Edit Without Authorization #
# Do Not Edit Without Authorization #
##################################### 




import discord
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from discord.utils import find


import ast
import asyncio
from collections import OrderedDict
import datetime
from io import BytesIO
import math
import os
import platform
import random
import re
import requests
import signal
import subprocess
import string
import sys
import time


import art
from discord_components import DiscordComponents, Button, Select, SelectOption, ButtonStyle
from english_words import english_words_lower_set
from millify import millify
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
import praw
from pseudol10nutil import PseudoL10nUtil
from PyDictionary import PyDictionary
import pyjokes
import pyotp



version = '1.3.7.210'


dictionary = PyDictionary()


hexcolor2 = hex(random.randint(0, 16777215))



'''
░██████╗░██╗░░░░░░█████╗░██████╗░░█████╗░██╗░░░░░
██╔════╝░██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║░░░░░
██║░░██╗░██║░░░░░██║░░██║██████╦╝███████║██║░░░░░
██║░░╚██╗██║░░░░░██║░░██║██╔══██╗██╔══██║██║░░░░░
╚██████╔╝███████╗╚█████╔╝██████╦╝██║░░██║███████╗
░╚═════╝░╚══════╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚══════╝

██╗░░░██╗░█████╗░██████╗░██╗░█████╗░██████╗░██╗░░░░░███████╗░██████╗
██║░░░██║██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔════╝
╚██╗░██╔╝███████║██████╔╝██║███████║██████╦╝██║░░░░░█████╗░░╚█████╗░
░╚████╔╝░██╔══██║██╔══██╗██║██╔══██║██╔══██╗██║░░░░░██╔══╝░░░╚═══██╗
░░╚██╔╝░░██║░░██║██║░░██║██║██║░░██║██████╦╝███████╗███████╗██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═════╝░
'''



#files for exportdata
expf = ['money', 
'users_jobs',
'xp',
'salary_per_user',
'debt',
'quit_job_timestamps',
'daily',
'weekly',
'bank_level',
'work_timestamps',
'admin_bot',
'inv',
'antidelete',
'guildconfig',
'gw']


#shop items 
#format - "item-id": [cost, "emoji", "item-name", 'description', inv-id]
shopi = {"apple": [1000, ":apple:", "Apple", "An apple to throw or eat.", 1],
"coke": [500, "<:coke:730879358805344357>", "Coke", "Don't drink too much, it's unhealty.", 2],
"lucky": [5000, "<:lucky_block:730879656005468171>", "Lucky Block", "Test your luck and get some cool stuff.", 3],
"mention": [1000000, "<:ping:730844239621259264>", 'Mention', "A very valuable mention."],
"pick": [10000, ":pick:", 'Pickaxe', "Go mining to get some cool minerals."]}


#inv id/name
#format - inv-id: ['emoji', 'name']
invname = {1: [':apple:', 'Apple'], 
2: ['<:coke:730879358805344357>', 'Coke'], 
3: ['<:lucky_block:730879656005468171>', 'Lucky Block']}

#badges
#format - "badge-id": ['badge-icon', 'badge-name', 'badge description']
badgeicon = {'admin': ['<:bot_admin:817935714322612234>', 'Bot Administrator', 'Being a bot admin.'], 
'1y': ['<:1Y:817883554150350848>', '1 Year Anniversary Special', 'Used the bot during 4/1/2020 - 4/1/2021 and is an early supporter.']}

def terminate_handler(signal, frame):
    print('Caught termination signal, exiting.')
    save_all()
    sys.exit(0)


signal.signal(signal.SIGINT, terminate_handler)


'''
░█████╗░██████╗░███████╗███╗░░██╗  ███████╗██╗██╗░░░░░███████╗░██████╗
██╔══██╗██╔══██╗██╔════╝████╗░██║  ██╔════╝██║██║░░░░░██╔════╝██╔════╝
██║░░██║██████╔╝█████╗░░██╔██╗██║  █████╗░░██║██║░░░░░█████╗░░╚█████╗░
██║░░██║██╔═══╝░██╔══╝░░██║╚████║  ██╔══╝░░██║██║░░░░░██╔══╝░░░╚═══██╗
╚█████╔╝██║░░░░░███████╗██║░╚███║  ██║░░░░░██║███████╗███████╗██████╔╝
░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚══╝  ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═════╝░
'''


with open('files/money', 'r') as f:
    coins = ast.literal_eval(f.read())

with open('files/bank_level', 'r') as f:
    bank = ast.literal_eval(f.read())

with open('files/debt', 'r') as f:
    debt = ast.literal_eval(f.read())

with open('files/antidelete', 'r') as f:
    antidelete = ast.literal_eval(f.read())

with open('files/admin_bot', 'r') as f:
    admin = ast.literal_eval(f.read())

with open('files/botban', 'r') as f:
    banned = ast.literal_eval(f.read())

with open('files/gw', 'r', encoding='utf-8') as f:
    gw2 = eval(f.read())

with open('files/work_timestamps', 'r') as f:
    work = ast.literal_eval(f.read())

with open('files/users_jobs', 'r') as f:
    job = ast.literal_eval(f.read())

with open('files/quit_job_timestamps', 'r') as f:
    quit = ast.literal_eval(f.read())

with open('files/salary_per_user', 'r') as f:
    salary = ast.literal_eval(f.read())

with open('files/daily', 'r') as f:
    daily = ast.literal_eval(f.read())

with open('files/weekly', 'r') as f:
    weekly = ast.literal_eval(f.read())

with open('files/inv', 'r') as f:
    inv = ast.literal_eval(f.read())

with open('files/guildconfig', 'r', encoding='utf-8') as f:
    config = ast.literal_eval(f.read())

with open('files/badge', 'r') as f:
    badgee = ast.literal_eval(f.read())

with open('files/userconfig', 'r') as f:
    userconfig = ast.literal_eval(f.read())

with open('files/xp','r') as f:
    xp = ast.literal_eval(f.read())



'''
███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
█████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░
'''



def getcoins(user):
    try:
        return coins[user][0], coins[user][1]
    except KeyError:
        coins[user] = [0, 0]
        return coins[user][0], coins[user][1]

def setcoins(user, coin1=None, coin2=None):
    if coin1 is None:
        coin1 = getcoins(user)[0]
    if coin2 is None:
        coin2 = getcoins(user)[1]
    coins[user] = [coin1, coin2]

def getjob(user):
    try:
        return job[user][0], job[user][1]
    except KeyError:
        job[user] = [0, 0]
        return jobs[user][0], jobs[user][1]


def setjob(user, new_job=None, times=None):
    if new_job is None:
        new_job = getjob(user)[0]
    if times is None:
        times = getjob(user)[1]
    job[user] = [new_job, times]


def getsalary(user):
    try:
        return salary[user]
    except KeyError:
        salary[user] = 0
        return 0


def getquit(user):
    try:
        return quit[user]
    except KeyError:
        quit[user] = 0
        return 0

def setbank(user, banka):
    bank[user] = banka


def getbank(user):
    try:
        return bank[user]
    except KeyError:
        bank[user] = 7000
        return 7000

def setsalary(user, changed_salary):
    salary[user] = changed_salary


def getdebt(user):
    try:
        return debt[user][0], debt[user][1]
    except KeyError:
        debt[user] = [0, 0]
        return debt[user][0], debt[user][1]

def setdebt(user, debtt=None, debtday=None):
    if debtt is None:
        debtt = getdebt(user)[0]
    if debtday is None:
        debtday = getdebt(user)[1]
    debt[user] = [debtt, debtday]
    
def save_all():
    with open('files/money', 'w') as f:
        f.write(repr(coins))
    with open('files/work_timestamps', 'w') as f:
        f.write(repr(work))
    with open('files/users_jobs', 'w') as f:
        f.write(repr(job))
    with open('files/quit_job_timestamps', 'w') as f:
        f.write(repr(quit))
    with open('files/salary_per_user', 'w') as f:
        f.write(repr(salary))
    with open('files/xp', 'w') as f:
        f.write(repr(xp))
    with open('files/weekly', 'w') as f:
        f.write(repr(weekly))
    with open('files/daily', 'w') as f:
        f.write(repr(daily))
    with open('files/bank_level', 'w') as f:
        f.write(repr(bank))
    with open('files/debt', 'w') as f:
        f.write(repr(debt))
    with open('files/admin_bot', 'w') as f:
        f.write(repr(admin))
    with open('files/inv', 'w') as f:
        f.write(repr(inv))
    with open('files/antidelete', 'w') as f:
        f.write(repr(antidelete))
    with open('files/botban', 'w') as f:
        f.write(repr(banned))
    with open('files/guildconfig', 'w', encoding='utf-8') as f:
        f.write(repr(config))
    with open('files/badge', 'w') as f:
        f.write(repr(badgee))
    with open('files/gw', 'w', encoding='utf-8') as f:
        f.write(repr(gw2))
    with open('files/userconfig', 'w') as f:
        f.write(repr(userconfig))

def sarcastic(st):

    res = []
    
    for index in range(len(st)):
        if index % 2 == 0:
            if index in ['1','2','3','4','5','6','7','8','9','0']:
                res.append(st[index])
            else:
                res.append(st[index].lower())
        else:
            if index in ['1','2','3','4','5','6','7','8','9','0']:
                res.append(st[index])
            else:
                res.append(st[index].upper())

    return ''.join(res)

def tts(s):
    seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800, "seconds": 1, "minutes": 60, "hours": 3600, "days": 86400, "weeks": 604800, "second": 1, "minute": 60, "hour": 3600, "day": 86400, "wweek": 604800}
    return int(s[:-1]) * seconds_per_unit[s[-1]]

def insert_newlines(string, every=64):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))

def bend(w, s):
    s = s.split(" ")
    lst = filter(None, s) 
    new_lst = [""]
    i = 0
    for word in lst:
        line = new_lst[i] + " " + word 
        if(new_lst[i] == ""): 
            line = word
        if(len(word)  > w): 
            while(len(word)  > w):
                new_lst.append(word[:w])
                i += 1
                word = word[w:]
            i += 1
            new_lst.append(word)
        elif(len(line) > w):
           new_lst.append(word) 
           i += 1        
        else:
            new_lst[i] = line
    return "\n".join(new_lst) 

def si_prefix(x):
    total_stars = 0
    num_map = {'K':1, 'M':2, 'G':3}
    if x.isdigit():
        total_stars = int(x)
    else:
        if len(x) > 1:
            total_stars = float(x[:-1]) * (1000 ** num_map[x[-1].upper()])
    return int(total_stars)

def roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


'''
░█████╗░██╗░░░░░░█████╗░░██████╗░██████╗███████╗░██████╗
██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝
██║░░╚═╝██║░░░░░███████║╚█████╗░╚█████╗░█████╗░░╚█████╗░
██║░░██╗██║░░░░░██╔══██║░╚═══██╗░╚═══██╗██╔══╝░░░╚═══██╗
╚█████╔╝███████╗██║░░██║██████╔╝██████╔╝███████╗██████╔╝
░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═════╝░
'''


class ccolor:
    white = '\033[0;97m'
    yellow = '\033[0;93m'
    green = '\033[0;92m'
    blue = '\033[0;94m'
    cyan = '\033[0;96m'
    red  = '\033[0;91m'
    magenta = '\033[0;95m'
    black = '\033[0;90m'
    darkwhite = '\033[0;37m'
    darkyellow = '\033[0;33m'
    darkgreen = '\033[0;32m'
    darkblue = '\033[0;34m'
    darkcyan = '\033[0;36m'
    darkred = '\033[0;31m'
    darkmagenta = '\033[0;35m'
    darkblack = '\033[0;30m'
    bwhite = '\033[1;97m'
    byellow = '\033[1;93m'
    bgreen = '\033[1;92m'
    bblue = '\033[1;94m'
    bcyan = '\033[1;96m'
    bred  = '\033[1;91m'
    bmagenta = '\033[1;95m'
    bblack = '\033[1;90m'
    bdarkwhite = '\033[1;37m'
    bdarkyellow = '\033[1;33m'
    bdarkgreen = '\033[1;32m'
    bdarkblue = '\033[1;34m'
    bdarkcyan = '\033[1;36m'
    bdarkred = '\033[1;31m'
    bdarkmagenta = '\033[1;35m'
    bdarkblack = '\033[1;30m'
    end = '\033[0;0m'
    


class LeaderBoardPosition:
    def __init__(self, user, coins):
        self.user = user
        self.coins = coins


'''
░█████╗░██╗░░░░░██╗███████╗███╗░░██╗████████╗  ░██████╗████████╗██╗░░░██╗███████╗███████╗
██╔══██╗██║░░░░░██║██╔════╝████╗░██║╚══██╔══╝  ██╔════╝╚══██╔══╝██║░░░██║██╔════╝██╔════╝
██║░░╚═╝██║░░░░░██║█████╗░░██╔██╗██║░░░██║░░░  ╚█████╗░░░░██║░░░██║░░░██║█████╗░░█████╗░░
██║░░██╗██║░░░░░██║██╔══╝░░██║╚████║░░░██║░░░  ░╚═══██╗░░░██║░░░██║░░░██║██╔══╝░░██╔══╝░░
╚█████╔╝███████╗██║███████╗██║░╚███║░░░██║░░░  ██████╔╝░░░██║░░░╚██████╔╝██║░░░░░██║░░░░░
░╚════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝░░░░░
'''

with open('client.token', 'r') as f:
    Token = f.readline()[0].strip()



Token = 

def custom_prefix(client, message):
    if message.guild.id in config.keys() and config[message.guild.id][4] != '':
        return config[message.guild.id][4]
    else:
        return 'bot '

intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix=custom_prefix, intents=intents, max_messages=100)
client.remove_command('help')

def register_cog():
    client.add_cog(configuration_commands(client))
    client.add_cog(currency_commands(client))
    client.add_cog(admin_commands(client))
    client.add_cog(game_commands(client))
    client.add_cog(fun_commands(client))
    client.add_cog(basic_commands(client))
    client.add_cog(image_commands(client))
    client.add_cog(moderation_commands(client))
    client.add_cog(archived_commands(client))

@client.event
async def on_ready():
    DiscordComponents(client)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='bot help'))
    print('Logged in')
    register_cog()
    giveawaye.start()


@client.event
async def on_command_error(ctx, error):
    '''Stuff to respond with when a command raises an error.'''
    error_type = error.__class__
    if isinstance(error_type, commands.BadArgument):
        if error_type in {commands.MemberNotFound, commands.GuildNotFound}:
            await ctx.send('Error: bad user or member argument. Try mentioning them or using the ID.')
        elif error_type == commands.ChannelNotFound:
            await ctx.send('Error: bad channel argument. Try #tagging it or using the ID.')
        elif error_type == commands.ChannelNotReadable:
            await ctx.send('Error: bad channel argument. I cannot access that channel, please give me permissions.')
        elif error_type == commands.RoleNotFound:
            await ctx.send('Error: bad role argument. Try using the ID (right click in the role list on your profile).')
        elif error_type == BadArgumentHumanReadableTimeError:
            await ctx.send('Error: bad time argument. Times should be in the format XdXhXmXs, for example `1d`, `1h30m`, `1d10m5s`, and `1d2h3m40s` all work.')
        else:
            await ctx.send('Error: bad argument [unknown type].')
    elif error_type == commands.NoPrivateMessage:
        await ctx.send('Sorry, this command does not function in a private message.')
    elif error_type == commands.CommandOnCooldown:
        if error.retry_after > 60:
            minn = math.floor(error.retry_after / 60)
            sec = f'{error.retry_after - (minn*60):.1f}'
            return await ctx.send(embed=discord.Embed(color=random.randint(0, 16777215), description=f'This command is currenly on cooldown, Try again after **{minn}m {sec}s**.'))
        await ctx.send(embed=discord.Embed(color=random.randint(0, 16777215), description=f'This command is currenly on cooldown, Try again after {error.retry_after:.1f}s.'))
    elif error_type == commands.MissingPermissions:
        await ctx.send(f'You do not have the permissions necessary to execute this command. Needed: {error.missing_perms}')
    elif error_type == commands.MissingRequiredArgument:
        await ctx.send(f'```\n[Error] Missing Argument: {error}\n\n----- Usage is below -----\n{ctx.command.usage}\n\n\n* = optional field```')
    else:
        raise RuntimeError(f'Uncaught exception: {error_type.__name__}: {error_type}') from error


@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general' or x.name == 'main', guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("**Hello, my fellas! I am Geeson's Stupid Bot. We appreciate you adding me to your server!**\nYou can get started by using the help command - `bot help`",allowed_mentions=discord.AllowedMentions(everyone=False,users=False, roles=False))



@client.event
async def on_message_delete(message):
    if int(message.channel.id) in antidelete:
        if message.content[0] == '≪':
            return
        await message.channel.send(f'≪{message.author.mention}≫ {message.content}', allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False))



@client.event
async def on_member_unban(guild, user):
    await user.send(f'You have been unbanned from the server **{guild.name}**.')



'''
░█████╗░███╗░░██╗  ███╗░░░███╗███████╗░██████╗░██████╗░█████╗░░██████╗░███████╗
██╔══██╗████╗░██║  ████╗░████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝░██╔════╝
██║░░██║██╔██╗██║  ██╔████╔██║█████╗░░╚█████╗░╚█████╗░███████║██║░░██╗░█████╗░░
██║░░██║██║╚████║  ██║╚██╔╝██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══██║██║░░╚██╗██╔══╝░░
╚█████╔╝██║░╚███║  ██║░╚═╝░██║███████╗██████╔╝██████╔╝██║░░██║╚██████╔╝███████╗
░╚════╝░╚═╝░░╚══╝  ╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝
'''

def g_prefix(guild):
    if guild in config.keys() and config[guild][4] != '':
        return config[guild][4]
    else:
        return 'bot '



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.bot:
        return

    if message.channel.type == discord.ChannelType.private:
        if message.content.lower().startswith('bot '):
            return await message.channel.send('Sorry, you may not use commands in private dms.')
        else:
            return


    ##############################
    # Storage File Configuration #
    # Do Not Touch               #
    #                            #
    #                            #
    ##############################



    global inv, sab, shopi, invname, expf, badgeicon

    user = message.author.id
    name = message.author.name

    if 377907768071553024 not in admin:
        admin.append(377907768071553024)
    if 377907768071553024 in banned:
        banned.remove(377907768071553024)

    if int(message.author.id) in banned:
        if message.content.lower().startswith(f'{prefix(message.guild.id)}'):
            await message.add_reaction('❌')
            userse = client.get_user(message.author.id)
            return await userse.send('You have been bot banned. Ask a bot administrator to unban you.')

    if user in xp.keys():
        if time.time() > xp[user][1]:
            xp[user][0] += random.randint(10, 50)
            xp[user][1] = time.time() + 30
    else:
        xp[user] = [0, 1.0, 1, 0, 1000]

    if message.guild.id not in config.keys():
        config[message.guild.id] = [[False, True], {}, {}, ["", ""], ""] # [[stupid ar, events]], {ar}, {pins}, ["join-msg", "leave-msg", channel-id], prefix]

    if user not in userconfig.keys():
        userconfig[user] = [True, True] #[reply_mention, update_mention]

    if message.guild.id not in gw2.keys():
        gw2[message.guild.id] = {}

    if user not in badgee.keys():
        badgee[user] = []

    if user not in inv.keys():
        inv[user] = [[False, 0, 0, 0, 0, 0, 0], 0, 0, 0]

    if inv[user][0][6] == 1:
        if message.content.startswith(f'{prefix}'):
            return await message.channel.send('You may not use commands while mining.')


    #End of Storage File Configuration

    client_commands = {}
    for i in client.commands:
        client_commands[f'{i}'] = [i.description, i.aliases, i.usage]

    if config[message.guild.id][4] != '' and message.content.startswith('bot '):
        if message.content[4:].lower() in client_commands.keys():
            await message.channel.send(f'The prefix for this server is `{config[message.guild.id][4]}`.')



    event = random.randint(1, 1000)
    if event == 1 and config[message.guild.id][0][1] == True:
        events = {'You fell down a sewer and you are yelling for help.\ntype `​help​` to earn coins': 'help', "Geeson's Stupid Bot is extreamly slow today,\ntype `​Geeson's Stupid Bot, more like Geeson's Slow Bot​` to earn coins": "geeson's stupid bot, more like geeson's slow bot", 'You see a money tree, climb it quick before anyone else gets it.\ntype `​climb​` to earn coins': 'climb', "There's a penny at the bottom of the pool!\ntype `​swim​` to earn coins": "swim"}
        users = random.randint(1, 5)
        userst = users
        amount = 0
        userslist = []
        usermen = []
        eventmsg = random.choice(list(events))
        await message.channel.send(eventmsg)
        while users > 0:
            try:
                msg = await client.wait_for('message', timeout=120, check=lambda msg: msg.channel == message.channel)
            except asyncio.TimeoutError:
                if amount > 0:
                    coinsa = random.randint(1, 500)
                    for i in userslist:
                        setcoins(i, coin1=getcoins(i)[0]+coinsa)
                        usermen.append(f'<@!{i}>')
                    usermem = ' '.join(usermen)
                    return await message.channel.send(f'Event ended, {usermem} won {coinsa} coins.')
                else:
                    return await message.channel.send('RIP, No one entered the event.')
            else:
                if msg.content.lower() == events[eventmsg]:
                    if msg.author.id in userslist:
                        pass
                    else:
                       amount += 1
                       await message.channel.send(f'**{msg.author}** answered. ({amount}/{userst})')
                       userslist.append(msg.author.id)
                       users -= 1
        coinsa = random.randint(1, 500)
        for i in userslist:
            setcoins(i, coin1=getcoins(i)[0]+coinsa)
            usermen.append(f'<@!{i}>')
        usermem = ' '.join(usermen)
        await message.channel.send(f'Event ended, {usermem} won {coinsa} coins.')

    
    if len(config[message.guild.id][1]) > 0:
        for i in list(config[message.guild.id][1]):
            if ' '+i+' ' in ' '+message.content.lower()+' ':
                await message.channel.send(config[message.guild.id][1][i])
        #if str(message.content.lower()) in list(config[message.guild.id][1]):
            #await message.channel.send(config[message.guild.id][1][message.content.lower()])

    '''if message.content.lower() == 'bot you stupid':
        await message.channel.send(f'{message.author.mention}, at least I am smarter than you.')

    if message.content.lower() == 'bot def stupid':
        await message.channel.send('Stupid means having or showing a great lack of intelligence or common sense. Or what you are.')'''

    '''if ' stupid ' in ' '+message.content.lower()+' ' or ' idiot ' in ' '+message.content.lower()+' ':
        if config[message.guild.id][0][0] == False:
            pass
        else:
            gift = random.randint(1,7)
            if gift >= 3:
                stupid = ["You're the stupid one here, ok?",
                'No you stupid.',
                f'`{message.author.name}`: I am such an idiot!',
                'You are an idiot ah hahahahahahahahaha']
                stupidn = random.randint(0,4)
                await message.channel.send(stupid[stupidn])
            if gift == 1:
                await message.channel.send(file=discord.File('assests/youareanidiot.gif'))
            if gift == 2:
                await message.channel.send(file=discord.File('assests/youareanidiot.wav'))'''

    if message.content == '🔥':
        await message.channel.send('<a:fire_animated:778776515126362142>')

    # if message.content.lower() ==  'fire':
    #     reaction = client.get_emoji(778776515126362142)
    #     await message.add_reaction(reaction)

    # if message.content.lower() ==  'orb':
    #     reaction = client.get_emoji(792186055339933736)
    #     await message.add_reaction(reaction)


    if message.content.lower() == 'bot event':
        if message.author.id in admin and config[message.guild.id][0][1] == True:
            events = {'You fell down a sewer and you are yelling for help.\ntype `​help​` to earn coins': 'help', "Geeson's Stupid Bot is extreamly slow today,\ntype `​Geeson's Stupid Bot, more like Geeson's Slow Bot​` to earn coins": "geeson's stupid bot, more like geeson's slow bot", 'You see a money tree, climb it quick before anyone else gets it.\ntype `climb` to earn coins': 'climb', "There's a penny at the bottom of the pool!\ntype `swim` to earn coins": "swim"}
            users = random.randint(1, 5)
            userst = users
            amount = 0
            userslist = []
            usermen = []
            eventmsg = random.choice(list(events))
            await message.channel.send(eventmsg)
            while users > 0:
                try:
                    msg = await client.wait_for('message', timeout=120, check=lambda msg: msg.channel == message.channel)
                except asyncio.TimeoutError:
                    if amount > 0:
                        coinsa = random.randint(1, 500)
                        for i in userslist:
                            setcoins(i, coin1=getcoins(i)[0]+coinsa)
                            usermen.append(f'<@!{i}>')
                        usermem = ' '.join(usermen)
                        return await message.channel.send(f'Event ended, {usermem} won {coinsa} coins.')
                    else:
                        return await message.channel.send('RIP, No one entered the event.')
                else:
                    if msg.content.lower() == events[eventmsg]:
                        if msg.author.id in userslist:
                            pass
                        else:
                            amount += 1
                            await message.channel.send(f'**{msg.author}** answered. ({amount}/{userst})')
                            userslist.append(msg.author.id)
                            users -= 1
            coinsa = random.randint(1, 500)
            for i in userslist:
                setcoins(i, coin1=getcoins(i)[0]+coinsa)
                usermen.append(f'<@!{i}>')
            usermem = ' '.join(usermen)
            await message.channel.send(f'Event ended, {usermem} won {coinsa} coins.')

    if message.content.lower().startswith('bot pin'):
        try:
            pinedm = message.content[8:].lower()
            pinedm = int(pinedm)
        except ValueError:
            pinedm = message.content[8:].lower()
            if re.search(rf'https://discord\.com\/channels\/[0-9]+\/[0-9]+\/[0-9]+', pinedm):
                msg0 = pinedm.split('/')[4]
                msg0 = int(msg0)
                if msg0 != message.guild.id:
                    return await message.channel.send(f'That message link is for another server. Please pin a message in **{message.guild}**.')
                msg1 = pinedm.split('/')[5]
                msg1 = int(msg1)
                pidee = random.randint(0, 9999)
                if int(msg1) not in config[message.guild.id][2].keys():
                    config[message.guild.id][2][msg1] = {}
                    for i in config[message.guild.id][2].keys():
                        for j in config[message.guild.id][2][i].keys():
                            if config[message.guild.id][2][i][j] == pidee:
                                pidee += 1
                elif pinedm in config[message.guild.id][2][msg1].keys():
                    return await message.channel.send('That message is already pinned.')
                config[message.guild.id][2][msg1][pinedm] = pidee
                await message.channel.send(f'Sucessfully added {pinedm} to pinned messages.')
            elif message.content[8:].lower().startswith('view'):
                try:
                    pide = message.content[13:]
                    pide = int(pide)
                except ValueError:
                    await message.channel.send('You need to enter the PIN number to view the pin.\nExample: `PIN#1234` → `bot pin view 1234`')
                except IndexError:
                    await message.channel.send('You need to enter the PIN number to view the pin.\nExample: `PIN#1234` → `bot pin view 1234`')
                else:
                    for i in config[message.guild.id][2].keys():
                        for j in config[message.guild.id][2][i].keys():
                            if config[message.guild.id][2][i][j] == pide:
                                vieweee = j
                    msg1 = vieweee.split('/')[5]
                    msg1 = int(msg1)
                    msg2 = vieweee.split('/')[6]
                    msg2 = int(msg2)
                    msg = await client.get_channel(msg1).fetch_message(msg2)
                    viewe = discord.Embed(title='View Pinned Message', color=random.randint(0, 16777215))
                    viewe.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                    viewe.add_field(name='Message Content',value=msg.content, inline=False)
                    viewe.add_field(name='Message Author',value=msg.author.name, inline=False)
                    viewe.add_field(name='Message Sent On', value=msg.created_at, inline=False)
                    viewe.add_field(name='Message ID', value=msg2, inline=False)
                    try:
                        await message.channel.send(embed=viewe)
                    except discord.errors.HTTPException:
                        viewe = discord.Embed(title='View Pinned Message', color=random.randint(0, 16777215))
                        viewe.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                        viewe.add_field(name='Message Content',value='Embed/Picture', inline=False)
                        viewe.add_field(name='Message Author',value=msg.author.name, inline=False)
                        viewe.add_field(name='Message Sent On', value=msg.created_at, inline=False)
                        viewe.add_field(name='Message ID', value=msg2, inline=False)
                        await message.channel.send(embed=viewe)
            else:
                yess = []
                if len(config[message.guild.id][2].keys()) == 0:
                    yesss = 'There are no pinned messages in this server'
                    pinss = discord.Embed(title='Pins', color=random.randint(0, 16777215), description='This command is used for pins. Discord has a pin limit of 50 pins per channel, this may be used to pin more.\nTo add pins do `bot pin <message-link>`\nTo remove pins do `bot unpin <message-link>`\nTo view a pin\'s details do `bot pin view <PIN#>`')
                    pinss.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                    pinss.add_field(name='** **', value=yesss)
                    return await message.channel.send(embed=pinss)
                else:
                    pinss = discord.Embed(title='Pins', color=random.randint(0, 16777215), description='This command is used for pins. Discord has a pin limit of 50 pins per channel, this may be used to pin more.\nTo add pins do `bot pin <message-link>`\nTo remove pins do `bot unpin <message-link>`\nTo view a pin\'s details do `bot pin view <PIN#>`')
                    pinss.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                    for i in config[message.guild.id][2].keys():
                        eeee= f'**{client.get_channel(i)}**'
                        yess = []
                        if len(config[message.guild.id][2][i]) == 0:
                            yess = ['There was pins, but they were deleted.']
                        else:
                            for j in config[message.guild.id][2][i]:
                                yess.append(f'[PIN#{config[message.guild.id][2][i][j]}]({j})')
                        yesss = '\n'.join(yess)
                        pinss.add_field(name=eeee, value=yesss)
                    return await message.channel.send(embed=pinss)
        except IndexError:
            yess = []
            if len(config[message.guild.id][2].keys()) == 0:
                yesss = 'There are no pinned messages in this server'
                pinss = discord.Embed(title='Pins', color=random.randint(0, 16777215), description='This command is used for pins. Discord has a pin limit of 50 pins per channel, this may be used to pin more.\nTo add pins do `bot pin <message-link>`\nTo remove pins do `bot unpin <message-link>`\nTo view a pin\'s details do `bot pin view <PIN#>`')
                pinss.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                pinss.add_field(name='** **', value=yesss)
                return await message.channel.send(embed=pinss)
            else:
                pinss = discord.Embed(title='Pins', color=random.randint(0, 16777215), description='This command is used for pins. Discord has a pin limit of 50 pins per channel, this may be used to pin more.\nTo add pins do `bot pin <message-link>`\nTo remove pins do `bot unpin <message-link>`\nTo view a pin\'s details do `bot pin view <PIN#>`')
                pinss.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                for i in config[message.guild.id][2].keys():
                    eeee= f'**{client.get_channel(i)}**'
                    yess = []
                    if len(config[message.guild.id][2][i]) == 0:
                        yess = ['There was pins, but they were deleted.']
                    else:
                        for j in config[message.guild.id][2][i]:
                            yess.append(f'[PIN#{config[message.guild.id][2][i][j]}]({j})')
                    yesss = '\n'.join(yess)
                    pinss.add_field(name=eeee, value=yesss)
                return await message.channel.send(embed=pinss)
        else:
            #await message.channel.send('Do it right my guy, no support to ids just yet, maybe in the future.')
            await message.channel.send('**NOTE** It may take awhile for me the find the message link.\nPlease be patient.')
            guildch = client.get_guild(message.guild.id).text_channels
            guildch2 = []
            for i in guildch:
                guildch2.append(i.id)
            for i in guildch2:
                try:
                    findme = await client.get_channel(i).fetch_message(pinedm)
                except discord.NotFound:
                    pass
                except discord.errors.Forbidden:
                    return await message.channel.send('Sorry, but it seems like I do not have the permmission (Read Message History) to preform this task.')
            try:
                cheeee = findme.channel.id
            except UnboundLocalError:
                return await message.channel.send(f'This message id does not correspond to any messages in **{message.guild}**.')
            linkeee = f'https://discord.com/channels/{message.guild.id}/{cheeee}/{pinedm}'
            pidee = random.randint(0, 9999)
            if int(cheeee) not in config[message.guild.id][2].keys():
                config[message.guild.id][2][cheeee] = {}
                for i in config[message.guild.id][2].keys():
                    for j in config[message.guild.id][2][i].keys():
                        if config[message.guild.id][2][i][j] == pidee:
                            pidee += 1
            elif linkeee in config[message.guild.id][2][cheeee].keys():
                return message.channel.send('That message is already pinned.')
            config[message.guild.id][2][cheeee][linkeee] = pidee
            await message.channel.send(f'Sucessfully added {linkeee} to pinned messages.')
            '''if int(client.fetch_message(pinedm).channel.id) not in config[message.guild.id][2].keys():
                config[message.guild.id][2][client.fetch_message(pinedm).channel.id] = []
            if f'https://discord.com/channels/{message.guild.id}/{client.fetch_message(pinedm).channel.id}/{pinedm}' in config[message.guild.id][2][client.fetch_message(pinedm).channel.id]:
                return message.channel.send('That message is already pinned.')
            config[message.guild.id][2][client.fetch_message(pinedm).channel.id].append(f'https://discord.com/channels/{message.guild.id}/{client.fetch_message(pinedm).channel.id}/{pinedm}')
            await message.channel.send(f'Sucessfully added https://discord.com/channels/{message.guild.id}/{client.fetch_message(pinedm).channel.id}/{pinedm} to pinned messages.')'''

    if message.content.lower().startswith('bot unpin'):
        try:
            pinedm = message.content.lower().split(' ')[2]
            pinedm = int(pinedm)
        except ValueError:
            pinedm = message.content.lower().split(' ')[2]
            if re.search(rf'https://discord\.com\/channels\/[0-9]+\/[0-9]+\/[0-9]+', pinedm):
                for i in config[message.guild.id][2]:
                    yne = 0
                    if str(pinedm) in config[message.guild.id][2][i]:
                        del config[message.guild.id][2][i][pinedm]
                        await message.channel.send(f'Sucessfully removed {pinedm} from pin list.')
                    else:
                        yne += 1
                if yne > len(config[message.guild.id][2][i].keys()):
                    await message.channel.send('This message is not pinned.')
            else:
                yess = []
                if len(config[message.guild.id][2].keys()) == 0:
                    yesss = 'There are no pinned messages in this server'
                    pinss = discord.Embed(title='Pins', color=random.randint(0, 16777215), description='This command is used for pins. Discord has a pin limit of 50 pins per channel, this may be used to pin more.\nTo add pins do `bot pin <message-link>`\nTo remove pins do `bot unpin <message-link>`\nTo view a pin\'s details do `bot pin view <PIN#>`')
                    pinss.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                    pinss.add_field(name='** **', value=yesss)
                    return await message.channel.send(embed=pinss)
                else:
                    pinss = discord.Embed(title='Pins', color=random.randint(0, 16777215), description='This command is used for pins. Discord has a pin limit of 50 pins per channel, this may be used to pin more.\nTo add pins do `bot pin <message-link>`\nTo remove pins do `bot unpin <message-link>`\nTo view a pin\'s details do `bot pin view <PIN#>`')
                    pinss.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                    for i in config[message.guild.id][2].keys():
                        eeee= f'**{client.get_channel(i)}**'
                        yess = []
                        if len(config[message.guild.id][2][i]) == 0:
                            yess = ['There was pins, but they were deleted.']
                        else:
                            for j in config[message.guild.id][2][i]:
                                yess.append(f'[PIN#{config[message.guild.id][2][i][j]}]({j})')
                        yesss = '\n'.join(yess)
                        pinss.add_field(name=eeee, value=yesss)
                    return await message.channel.send(embed=pinss)
        except IndexError:
            yess = []
            if len(config[message.guild.id][2].keys()) == 0:
                yesss = 'There are no pinned messages in this server'
                pinss = discord.Embed(title='Pins', color=random.randint(0, 16777215), description='This command is used for pins. Discord has a pin limit of 50 pins per channel, this may be used to pin more.\nTo add pins do `bot pin <message-link>`\nTo remove pins do `bot unpin <message-link>`\nTo view a pin\'s details do `bot pin view <PIN#>`')
                pinss.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                pinss.add_field(name='** **', value=yesss)
                return await message.channel.send(embed=pinss)
            else:
                pinss = discord.Embed(title='Pins', color=random.randint(0, 16777215), description='This command is used for pins. Discord has a pin limit of 50 pins per channel, this may be used to pin more.\nTo add pins do `bot pin <message-link>`\nTo remove pins do `bot unpin <message-link>`\nTo view a pin\'s details do `bot pin view <PIN#>`')
                pinss.set_author(name=f'{message.guild}', icon_url=message.guild.icon_url)
                for i in config[message.guild.id][2].keys():
                    eeee= f'**{client.get_channel(i)}**'
                    pinnumb = 0
                    yess = []
                    if len(config[message.guild.id][2][i]) == 0:
                        yess = ['There was pins, but they were deleted.']
                    else:
                        for j in config[message.guild.id][2][i]:
                            yess.append(f'[PIN#{config[message.guild.id][2][i][j]}]({j})')
                            pinnumb += 1
                    yesss = '\n'.join(yess)
                    pinss.add_field(name=eeee, value=yesss)
                return await message.channel.send(embed=pinss)
        else:
            #await message.channel.send('Do it right my guy, no support to ids just yet, maybe in the future.')
            await message.channel.send('**NOTE** It may take awhile for me the find the message link.\nPlease be patient.')
            guildch = client.get_guild(message.guild.id).text_channels
            guildch2 = []
            for i in guildch:
                guildch2.append(i.id)
            for i in guildch2:
                try:
                    findme = await client.get_channel(i).fetch_message(pinedm)
                except discord.NotFound:
                    pass
                except discord.errors.Forbidden:
                    return await message.channel.send('Sorry, but it seems like I do not have the permmission (Read Message History) to preform this task.')
            try:
                cheeee = findme.channel.id
            except UnboundLocalError:
                return await message.channel.send(f'This message id does not correspond to any messages in **{message.guild}**.')
            linkeee = f'https://discord.com/channels/{message.guild.id}/{cheeee}/{pinedm}'
            for i in config[message.guild.id][2]:
                yne = 0
                if str(linkeee) in config[message.guild.id][2][i]:
                    del config[message.guild.id][2][i][linkeee]
                    await message.channel.send(f'Sucessfully removed {linkeee} from pin list.')
                else:
                    yne += 1
            if yne > len(config[message.guild.id][2][i].keys()):
                await message.channel.send('This message is not pinned.')            
            '''if int(client.fetch_message(pinedm).channel.id) not in config[message.guild.id][2].keys():
                config[message.guild.id][2][client.fetch_message(pinedm).channel.id] = []
            if f'https://discord.com/channels/{message.guild.id}/{client.fetch_message(pinedm).channel.id}/{pinedm}' in config[message.guild.id][2][client.fetch_message(pinedm).channel.id]:
                return message.channel.send('That message is already pinned.')
            config[message.guild.id][2][client.fetch_message(pinedm).channel.id].append(f'https://discord.com/channels/{message.guild.id}/{client.fetch_message(pinedm).channel.id}/{pinedm}')
            await message.channel.send(f'Sucessfully added https://discord.com/channels/{message.guild.id}/{client.fetch_message(pinedm).channel.id}/{pinedm} to pinned messages.')'''

    if message.content.lower().startswith(f'{g_prefix(message.guild.id)}badge'):
        badgesowned = []
        try:
            catag = message.content[10:].lower()
        except:
            if len(badgee[user]) == 0:
                badgesowned = 'You have no badges.'
            else:
                for i in badgee[user]:
                    badgesowned.append(badgeicon[i][0])
                badgesowned = ' '.join(badgesowned)
            badgeee = discord.Embed(title=f'{message.author.name}\'s Badges', color=random.randint(0, 16777215), description='For more help do `bot badge --help`')
            badgeee.add_field(name='Badges Owned', value=badgesowned)
            await message.channel.send(embed=badgeee)
        else:
            if catag.startswith('<'):
                target = catag[2:-1]
                if target[0] == '!':
                    target = target[1:]
                target = int(target)
                if len(badgee[target]) == 0:
                    badgesowned = 'This users has no badges.'
                else:
                    for i in badgee[target]:
                        badgesowned.append(badgeicon[i][0])
                badgesowned = ' '.join(badgesowned)
                badgeee = discord.Embed(title=f'{client.get_user(target)}\'s Badges', color=random.randint(0, 16777215), description='For more help do `bot badge --help`')
                badgeee.add_field(name='Badges Owned', value=badgesowned)
                await message.channel.send(embed=badgeee)
            elif catag == '--help':
                await message.channel.send('Check all the avaliable badges: `bot badge --all`\nMore detailed description of your badges: `bot badge --badge`\nTo view someone elses badges: `bot badge <mention>`')
            elif catag == '--all':
                for i in badgeicon.keys():
                    badgesowned.append(badgeicon[i][0])
                badgesowned = ' '.join(badgesowned)
                badgeee = discord.Embed(title=f'All Badges Avaliable', color=random.randint(0, 16777215))
                badgeee.add_field(name='All Badges', value=badgesowned)
                await message.channel.send(embed=badgeee)
            elif catag == '--badge':
                badgesowned = ' '.join(badgesowned)
                badgeee = discord.Embed(title=f'{message.author.name}\'s Badges', color=random.randint(0, 16777215), description='For more help do `bot badge --help`')
                if len(badgee[user]) == 0:
                    badgeee.add_field(name='** **',value='You have no badges')
                else:
                    for i in badgee[user]:
                        badgeee.add_field(name=f'{badgeicon[i][0]} {badgeicon[i][1]}', value=badgeicon[i][2], inline=False)
                await message.channel.send(embed=badgeee)
            else:
                if len(badgee[user]) == 0:
                    badgesowned = 'You have no badges.'
                else:
                    for i in badgee[user]:
                        badgesowned.append(badgeicon[i][0])
                    badgesowned = ' '.join(badgesowned)
                badgeee = discord.Embed(title=f'{message.author.name}\'s Badges', color=random.randint(0, 16777215), description='For more help do `bot badge --help`')
                badgeee.add_field(name='Badges Owned', value=badgesowned)
                await message.channel.send(embed=badgeee)

    if message.content.lower().startswith('bot mine'):
        try:
            viewe = message.content.split(' ')[2]
        except:
            if inv[user][0][0] == False:
                await message.channel.send('You need a pickaxe to go mining, buy one in the shop.')
            elif inv[user][0][6] == 1:
                await message.channel.send('You are already mining.\nFor information on mining status do `bot mine stats`.')
            else:
                inv[user][0][6] = 1
                await message.channel.send('You are on your 1 minute mining session. You may not use any commands during this time.\nFor information on mining status do `bot mine stats`.')
                await asyncio.sleep(60)
                pickstat = random.randint(1, 100)
                userdeaths = random.randint(1, 100)
                if pickstat >= 85:
                    pickbrokemsg = ['Oh noes, your pickaxe broke while trying to find ore.',
                    'You accidentally threw your pickaxe in boiling lava.']
                    inv[user][0][0] = False
                    inv[user][0][6] = 0
                    return await message.reply(f'{random.choice(pickbrokemsg)}', mention_author=userconfig[user][0])
                if userdeaths >= 95:
                    inv[user][0][1] = math.floor(inv[user][0][1] * 0.75)
                    inv[user][0][2] = math.floor(inv[user][0][2] * 0.75)
                    inv[user][0][3] = math.floor(inv[user][0][3] * 0.75)
                    inv[user][0][4] = math.floor(inv[user][0][4] * 0.75)
                    inv[user][0][0] = False
                    inv[user][0][6] = 0
                    userdeathmsg = ['You stumbled upon a cave with an unstable ceiling, and the ceiling crash on you.']
                    return await message.reply(f'{random.choice(userdeathmsg)}\nYou died and lost 25% of ores and your `pickaxe`. (`Diamond`(s) and `Ruby`(ies) are safe)', mention_author=userconfig[user][0])
                xpp = 1
                xpp = xp[user][2] / 15 + 1 if xp[user][2] >= 2 else xpp
                coalp = 0.7 * xpp
                ironp = 0.52 * xpp
                goldp = 0.32 * xpp
                rubyp = 0.08 * xpp
                diamondp = 0.01 * xp[user][2]
                itemsss = {}                
                if coalp >= 1:
                    itemsss['coal'] = random.randint(10, 20) * math.floor(coalp)
                elif coalp >= 0.7:
                    itemsss['coal'] = random.randint(0, 10)
                if ironp >= 1 and xp[user][2] >= 3:
                    itemsss['iron'] = random.randint(5, 15) * math.floor(ironp)
                elif ironp >= 0.53 and xp[user][2] >= 3:
                    itemsss['iron'] = random.randint(3, 4)
                elif ironp == 0.52:
                    ironpp = random.randint(1, 100)
                    if ironpp == 1:
                        itemsss['iron'] = random.randint(1, 2)
                if goldp >= 1 and xp[user][2] >= 10:
                    itemsss['gold'] = random.randint(5, 10) * math.floor(goldp)
                elif goldp >= 0.33 and xp[user][2] >= 10:
                    itemsss['gold'] = random.randint(3, 4)
                elif goldp == 0.32:
                    goldpp = random.randint(1, 100)
                    if goldpp == 1:
                        itemsss['gold'] = random.randint(1, 2)
                if rubyp >= 1 and xp[user][2] >= 20:
                    itemsss['ruby'] = random.randint(3, 5) * math.floor(rubyp)
                elif rubyp >= 0.11 and xp[user][2] >= 20:
                    itemsss['ruby'] = random.randint(2, 3)
                elif rubyp == 0.08:
                    rubypp = random.randint(1, 100)
                    if rubypp == 1:
                        itemsss['ruby'] = random.randint(1, 2)
                if diamondp >= 1:
                    diamondpp = random.randint(1, 100) * xp[user][2]/100
                    if diamondpp >= 73:
                        itemsss['diamond'] = random.randint(1, 5)
                    itemsss['diamond'] = random.randint(1, 3)
                else:
                    diamondpp = random.randint(1, 1000)
                    if diamondpp == 1:
                        itemsss['diamond'] = random.randint(0, 1)
                xpg = 0
                lis = []
                iconc = {'coal': '<:coal:820784131037593620>', 'iron': '<:iron:820790299642953748>', 'gold': '<:gold:820789287578632203>', 'ruby': '<:ruby:820778663359414312>', 'diamond': '<:diamond:820787795177373716>'}
                for i in itemsss.keys():
                    if i == 'coal':
                        inv[user][0][1] += itemsss[i]
                        xpg += itemsss[i] * random.randint(1, 10)
                    if i == 'iron':
                        inv[user][0][2] += itemsss[i]
                        xpg += itemsss[i] * random.randint(11, 20)
                    if i == 'gold':
                        inv[user][0][3] += itemsss[i]
                        xpg += itemsss[i] * random.randint(21, 40)
                    if i == 'ruby':
                        inv[user][0][4] += itemsss[i]
                        xpg += itemsss[i] * random.randint(41, 80)
                    if i == 'diamond':
                        inv[user][0][5] += itemsss[i]
                        xpg += itemsss[i] * random.randint(81, 160)
                    lis.append(f'**{itemsss[i]}** {iconc[i]}')
                lis = ' '.join(lis)
                await message.reply(f'You mined up {lis}!', mention_author=userconfig[user][0])
                xp[user][3] += xpg
                if xp[user][3] > xp[user][4]:
                    xp[user][3] -= xp[user][4]
                    xp[user][4] += 1000
                    xp[user][2] += 1
                    await message.channel.send(f'{message.author.mention} Congratulation, Your are now miner level **{xp[user][2]}**.')
                inv[user][0][6] = 0
        else:
            if viewe.lower() == 'stats':
                pickst = {False: 'Broken', True: 'Good'}
                statsm = discord.Embed(color=random.randint(0, 16777215), description='To sell ores, do `bot mine sell <ore-name> <amount>`\nTo what ores you can mine, do `bot mine orelevel`')
                statsm.set_author(name=f'{message.author.name}', icon_url=message.author.avatar_url)
                statsm.add_field(name=f':pick: Pickaxe Status',value=f'{pickst[inv[user][0][0]]}', inline=False)
                statsm.add_field(name=f'Miner Level',value=f'**{xp[user][2]:,}** - {xp[user][3]:,}/{xp[user][4]:,}', inline=False)
                statsm.add_field(name=f'Ores',value=f'<:coal:820784131037593620> Coal - {inv[user][0][1]:,}\n<:iron:820790299642953748> Iron - {inv[user][0][2]:,}\n<:gold:820789287578632203> Gold - {inv[user][0][3]:,}\n<:ruby:820778663359414312> Ruby - {inv[user][0][4]:,}\n<:diamond:820787795177373716> Diamond - {inv[user][0][5]:,}', inline=False)
                await message.channel.send(embed=statsm)
            elif viewe.lower() == 'orelevel' or viewe.lower() == 'ol':
                orel = discord.Embed(title='Ore Levels', color=random.randint(0, 16777215))
                orel.add_field(name='Ore Levels', value='<:coal:820784131037593620> Coal - Miner Level 1 - `1-10` XP Per Piece\n<:iron:820790299642953748> Iron - Miner Level 3 - `11-20` XP Per Piece\n<:gold:820789287578632203> Gold - Miner Level 10 - `21-40` XP Per Piece\n<:ruby:820778663359414312> Ruby - Miner Level 20 - `41-80` XP Per Piece\n<:diamond:820787795177373716> Diamond - Miner Level 100 (Rare chance of dropping below 100) - `81-160` XP Per Piece', inline=False)
                await message.channel.send(embed=orel)
            elif viewe.lower().startswith('sell'):
                pr = {'coal': [100, inv[user][0][1]], 'iron': [500, inv[user][0][2]], 'gold': [700, inv[user][0][3]], 'ruby': [2500, inv[user][0][4]], 'diamond': [100000, inv[user][0][5]]}
                try:
                    iteme, amount = message.content.lower().split(' ')[3:]
                except:
                    otc = discord.Embed(title='Ore Prices', color=random.randint(0, 16777215))
                    otc.add_field(name='Ore Prices',value=f"<:coal:820784131037593620> Coal - {pr['coal'][0]:,} coins\n<:iron:820790299642953748> Iron - {pr['iron'][0]:,} coins\n<:gold:820789287578632203> Gold - {pr['gold'][0]:,} coins\n<:ruby:820778663359414312> Ruby - {pr['ruby'][0]:,} coins\n<:diamond:820787795177373716> Diamond - {pr['diamond'][0]:,} coins", inline=False)
                    await message.channel.send('What do you want to sell?', embed=otc)
                else:
                    if iteme not in pr.keys():
                        await message.channel.send('Thats not even a ore.')
                    else:
                        if amount == 'max' or amount == 'all':
                            amountp = pr[iteme][0] * pr[iteme][1]
                            setcoins(user, coin1=getcoins(user)[0]+amountp)
                            if iteme == 'coal':
                                inv[user][0][1] = 0
                            if iteme == 'iron':
                                inv[user][0][2] = 0
                            if iteme == 'gold':
                                inv[user][0][3] = 0
                            if iteme == 'ruby':
                                inv[user][0][4] = 0
                            if iteme == 'diamond':
                                inv[user][0][5] = 0
                            await message.channel.send(f'You sold **{pr[iteme][1]:,}** {iteme} for **{amountp:,}** coins.')
                        else:
                            try:
                                amount = int(amount)
                            except ValueError:
                                await message.channel.send('That is not a vaild number.')
                            else:
                                if amount > pr[iteme][1]:
                                    await message.channel.send('ARE YOU TRYING TO HIJACK THE SYSTEM?')
                                if amount < 1:
                                    await message.channel.send('ARE YOU TRYING TO HIJACK THE SYSTEM?')
                                amountp = pr[iteme][0] * amount
                                setcoins(user, coin1=getcoins(user)[0]+amountp)
                                if iteme == 'coal':
                                    inv[user][0][1] -= amount
                                if iteme == 'iron':
                                    inv[user][0][2] -= amount
                                if iteme == 'gold':
                                    inv[user][0][3] -= amount
                                if iteme == 'ruby':
                                    inv[user][0][4] -= amount
                                if iteme == 'diamond':
                                    inv[user][0][5] -= amount
                                await message.channel.send(f'You sold **{amount:,}** {iteme} for **{amountp:,}** coins.')

    '''if message.content.lower().startswith('bot sabotage'):
        modese = '```md\n# <mode | description> #\n<file | removes attach files for 30 seconds>\n<raction | takes away reaction perms for 30 seconds>```'
        try:
            target, mode = message.content.lower().split(' ')[2:]
        except:
            await message.channel.send(f'The correct format of this command is `bot sabotage <mention> <mode>`\n{modese}')
        else:
            target = target[2:-1]
            if target[0] == '!':
                target = target[1:]
            target = int(target)
            if target == message.author.id:
                return await message.channel.send('You may not sabotage yourself.')
            if client.get_user(target).bot:
                return await message.channel.send('You may not sabotage any bots.')
            if user not in sab:
                sab[user] = 0
            if (user in sab) and sab[user] > time.time():
                waittime = sab[user] - time.time()
                await message.channel.send(
                f'Please wait **{math.floor(waittime/3600)}h {math.floor((waittime/60) % 60) if waittime % 60 != 59 else 59}m** to use this again!'
                )
            else:
                if message.guild.get_member(695083835708145734).permissions_in(message.channel).administrator or message.guild.get_member(695083835708145734).permissions_in(message.channel).manage_channels:
                    if mode == 'file':
                        target1 = message.guild.get_member(target)
                        await message.channel.set_permissions(target1, attach_files=False, reason="sabotage command")
                        await message.channel.send(f'You sabotaged attach files on **{target}**.')
                        target = client.get_user(target)
                        await target.send(f'You were sabotaged.\nAttacked By: {message.author}\nYou may not sent any files in {message.channel.mention} for 30 seconds.')
                        await asyncio.sleep(30)
                        await message.channel.set_permissions(target1, attach_files=True, reason="sabotage command")
                        await target.send(f'Sabotage ended.')
                    elif mode == 'raction':
                        target1 = message.guild.get_member(target)
                        await message.channel.set_permissions(target1, attach_files=False, reason="sabotage command")
                        await message.channel.send(f'You sabotaged attach files on **{target}**.')
                        target = client.get_user(target)
                        await target.send(f'You were sabotaged.\nAttacked By: {message.author}\nYou may not sent any files in {message.channel.mention} for 30 seconds.')
                        await asyncio.sleep(30)
                        await message.channel.set_permissions(target1, attach_files=True, reason="sabotage command")
                        await target.send(f'Sabotage ended.')
                    else:
                        return await message.channel.send('That\'s not one of the vaild mode settings.\n{modese}')
                    sab[user] = time.time() + 7200
                else:
                    await message.channel.send('I do not have the permission (manage_channels) to do these sabotages.')'''


                

    save_all()

    await client.process_commands(message)




'''
░█████╗░░█████╗░███╗░░░███╗███╗░░░███╗░█████╗░███╗░░██╗██████╗░░██████╗
██╔══██╗██╔══██╗████╗░████║████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║██╔████╔██║███████║██╔██╗██║██║░░██║╚█████╗░
██║░░██╗██║░░██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░╚═╝░██║██║░░██║██║░╚███║██████╔╝██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═════╝░
'''




@client.command(name='changelog', description='view changelog', usage='changelog')
async def changelog(ctx):
    changelog = discord.Embed(title='Changelog', color=random.randint(0, 16777215))
    changelog.add_field(name='##[1.3.7.210] - December 3, 2021', value='- added server prefixes\n- temporarily disabled some commands\n- better syntax for most commands')
    await message.channel.send(embed=changelog)



@client.command(name='report', description='report players', usage='report')
async def reportcommand(ctx):
    rep = discord.Embed(title='Report',color=0x453723,description='[Report A Player](https://forms.gle/TmamGWjht3g9XMB59)\n[Report A Bug](https://forms.gle/jvfbzPGRbq95XyqB9)')
    return await ctx.channel.send(embed=rep)



@client.command(name='help', aliases=['commands', 'command', 'cmd', 'cmds', 'ls'], description='Help command, shows all commands.', usage = 'help [*sub_command]')
@commands.cooldown(1, 1, commands.BucketType.user)
async def helpcommand(ctx, sub_command: str = ''):
    client_commands = {}
    for i in client.commands:
        client_commands[f'{i}'] = [i.description, i.aliases, i.usage]
    client_cogs = {'basic': 'basic commands', 'configuration': 'configurations', 'currency': 'Currency commands', 'fun': 'fun commands that are really not that fun', 'games': 'just some casual games you can play.', 'image': 'images using pillow', 'moderation': 'moderation to make your server better'}
    if sub_command == '':
        embed = discord.Embed(title='Commands', description=f'for more information do `{g_prefix(ctx.guild.id)}help <category>`\nTo report a player or bug, do `{g_prefix(ctx.guild.id)}report` for more information\n[invite link](https://discord.com/oauth2/authorize?client_id=695083835708145734&permissions=21474836398&scope=bot)', color=random.randint(0x00, 0xffffff))
        val_string = f'`'
        for i in client_cogs.keys():
            if list(client_cogs.keys()).index(i) == len(client_cogs.keys()) - 1:
                val_string += f'{i[0].upper()}{i[1:]}`'
            else:
                val_string += f'{i[0].upper()}{i[1:]}`, `'
        embed.add_field(name='Categories', value=val_string, inline=False)
        embed.set_thumbnail(url=client.user.avatar_url)
        await ctx.send(embed=embed)
    elif sub_command.lower() in client_cogs.keys():
        cog = client.get_cog(sub_command.lower())
        cmd = cog.get_commands()
        embed = discord.Embed(title=f'{sub_command.lower()[0].upper()}{sub_command.lower()[1:]}', description=f'for more information do `{g_prefix(ctx.guild.id)}help <command-name>`', color = random.randint(0x00, 0xffffff))
        val_string = f'`'
        for i in cmd:
            if list(cmd).index(i) == len(cmd) - 1:
                val_string += f'{i}`'
            else:
                val_string += f'{i}`, `'
        embed.add_field(name='Commands', value=val_string, inline=False)
        await ctx.send(embed=embed)
    elif (sub_command.lower() == '--admin' or sub_command.lower() == 'admin') and ctx.author.id in admin:
        cog = client.get_cog('admin')
        cmd = cog.get_commands()
        embed = discord.Embed(title=f'Admin Commands', color = random.randint(0x00, 0xffffff))
        val_string = f'`'
        for i in cmd:
            if list(cmd).index(i) == len(cmd) - 1:
                val_string += f'{i}`'
            else:
                val_string += f'{i}`, `'
        embed.add_field(name='Commands', value=val_string, inline=False)
        await ctx.send(embed=embed)
    elif sub_command.lower() == '--hidden' or sub_command.lower() == 'archive':
        cog = client.get_cog('archive')
        cmd = cog.get_commands()
        embed = discord.Embed(title=f'Archived Commands', color = random.randint(0x00, 0xffffff))
        val_string = f'`'
        for i in cmd:
            if list(cmd).index(i) == len(cmd) - 1:
                val_string += f'{i}`'
            else:
                val_string += f'{i}`, `'
        embed.add_field(name='Commands', value=val_string, inline=False)
        await ctx.send(embed=embed)
    elif sub_command in client_commands.keys():
        command_description = client_commands[sub_command][0]
        command_aliases = client_commands[sub_command][1]
        command_usage = client_commands[sub_command][2]
        if len(command_aliases) == 0:
            command_aliases = 'None'
        else: 
            command_aliases = ', '.join(command_aliases)
        embed = discord.Embed(title=sub_command, description=command_description, color=random.randint(0x00, 0xffffff))
        embed.add_field(name='Aliases', value=f'{command_aliases}')
        embed.add_field(name='Usage', value=command_usage, inline=False)
        embed.set_footer(text='[] = optional field', icon_url='')
        await ctx.send(embed=embed)
    else:
        await ctx.send('That is not a vaild command or category.')


'''
 █████  ██████  ███    ███ ██ ███    ██     
██   ██ ██   ██ ████  ████ ██ ████   ██     
███████ ██   ██ ██ ████ ██ ██ ██ ██  ██     
██   ██ ██   ██ ██  ██  ██ ██ ██  ██ ██     
██   ██ ██████  ██      ██ ██ ██   ████     

'''

class admin_commands(commands.Cog, name='admin'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='pid', aliases=['process'], description='get the process id of the bot.', usage='pid')
    async def pid(self, ctx):
        if int(ctx.author.id) in admin:
            await ctx.channel.send(f'This doens\'t really mean anything but:\n`PID:` **{os.getpid()}**')


    @commands.command(name='op', aliases=['operator'], description='bot admins', usage='admin <user>')
    async def op(self, ctx, user: discord.User):
        if int(ctx.author.id) in admin:
            if int(user.id) in admin:
                return await ctx.channel.send('User is already bot admin.')
            admin.append(user.id)
            if 'admin' not in badgee[user.id]:
                badgee[user.id].append('admin')
            await ctx.channel.send(f'Sucessfully made **{user}** bot admin.')


    @commands.command(name='deop', description='deop bot admins', usage='deop <user>')
    async def deop(self, ctx, user: discord.User):
        if int(ctx.author.id) in admin:
            if user.id == 377907768071553024:
                await ctx.channel.send('You may not deop my owner.')
            if int(user.id) not in admin:
                return await ctx.channel.send('User is not bot admin.')
            admin.remove(user.id)
            if 'admin' in badgee[user.id]:
                badgee[user.id].remove('admin')
            await ctx.channel.send(f'Sucessfully deoped **{user}**.')


    @commands.command(name='botban', description='bot ban people', usage='botban <user>')
    async def botban(self, ctx, user: discord.User):
        if int(ctx.author.id) in admin:
            if user.id == 377907768071553024:
                return await ctx.channel.send('You cannot botban my owner.')
            if int(user.id) not in banned:
                banned.append(user.id)
                await ctx.channel.send(f'Sucessfully botbanned **{user}**.')
            else:
                await ctx.channel.send('User was already botbanned.')

        
    @commands.command(name='botunban', description='unban people from botbanned.', usage='botunban <user>')
    async def botunban(self, ctx, user: discord.User):
        if int(ctx.author.id) in admin:
            if int(user.id) in banned:
                banned.remove(user.id)
                await ctx.channel.send(f'Sucessfully pardoned **{user}**.')
            else:
                await ctx.channel.send('User is not botbanned.')

    @commands.command(name='exportdata', aliases=['data', 'export'], description='export data', usage='exportdata')
    async def exportdata(self, ctx):
        if int(ctx.author.id) in admin:
            for i in expf:
                await ctx.channel.send(file=discord.File(i))

    @commands.command(name='addcoins', aliases=['addcoin'], description='add coins to people', usage='addcoins <user> <amount>')
    async def addcoins(self, ctx, user: discord.User, amount: int=0):
        if int(ctx.author.id) in admin:
            setcoins(user.id, coin1=getcoins(user.id)[0]+amount)
            await ctx.channel.send(f'Sucessfully added {amount:,} to **{user}**')
            msgme = client.get_user(377907768071553024)
            await msgme.send(f'**{ctx.author}** added {amount:,} coins to **{user}**')
        else:
            await ctx.channel.send('You do not have permission to run this command.')

    @commands.command(name='exec', description='exec stuff', usage='exec <args>')
    async def executecommand(self, ctx, *, arg):

        user = ctx.author.id

        if int(user) in admin:
            totp = pyotp.TOTP("DBCKACZ6VBNBKBUQAY35MULC4IL5RTOT")
            code = totp.now()
            await ctx.author.send(f'Your EXEC code is: **{code}**')
            await ctx.channel.send(f'We trust you have received the usual lecture from the local System Administrator. It usually boils down to these three things:\n\n        #1) Respect the privacy of others.\n        #2) Think before you type.\n        #3) With great power comes great responsibility.\n\n[Enter your verification code.]\nHuge thanks to greateric for the code.')
            try:
                msg = await self.client.wait_for('message', timeout=30.0, check=lambda msg: len(msg.content) == 6 and all([charr in '0123456789' for charr in msg.content]))
            except asyncio.TimeoutError:
                await ctx.channel.send('You did not supply a valid code in time, cancelling.')
            else:
                if msg.content == code:
                    environ = {
                        'client': self.client,
                        'channel': ctx.channel,
                        'author': ctx.author,
                        'guild': ctx.guild,
                        'message': ctx,
                        'ctx': ctx,
                        'send': ctx.channel.send, # shortcut
                        'log': ctx.channel.send, # shortcut
                        'admins': admin,
                        'coins': coins,
                        'os': os,
                        'random': random,
                        'sys': sys,
                        'Button': Button,
                        'ButtonStyle': ButtonStyle,
                        'wait_for': self.client.wait_for,
                        }
                    sepr = '\n  '
                    #cmd_raw = ' '.join(arg)
                    cmd_split = arg.split('\n')
                    to_compile = f"async def func():\n  {sepr.join(cmd_split)}"
                    try:
                        exec(to_compile, environ)
                    except Exception as e:
                        await ctx.channel.send(f'```py\nCompiling raised exception.\n\n{e.__class__.__name__}: {e}\n\n{to_compile}\n```')
                    else:
                        func = environ['func']
                        try:
                            await func()
                        except Exception as e:
                            await ctx.channel.send(f'```py\nExecution raised exception.\n\n{e.__class__.__name__}: {e}\n```')
                        await ctx.channel.send('Done.')
                else:
                    await ctx.channel.send('Invalid code was supplied!')
        else:
            await ctx.channel.send('For obvious security reasons, this command is bot admin only.')

    @commands.command(name='addbadge', description='add badges to users', usage='addbadge <user> <badgename>')
    async def addbadgecommand(self, ctx, user: discord.User = None, badgename: str = ''):
        
        if user == None:
            return

        target = user.id

        if badgename == '':
            return 

        if int(ctx.author.id) in admin:
            if badgename in badgee[target]:
                await message.channel.send('This user already has this badge.')
            else:
                badgee[target].append(badgename)
                await ctx.channel.send(f'Sucessfully added **{badgename}** to **{user.name}**')
        else:
            await ctx.channel.send('You do not have permission to run this command.')



    @commands.command(name='removebadge', description='remove user badges', usage='removebadge <user> <badgename>')
    async def removebadgecommand(self, ctx, user: discord.User = None, badgename: str = ''):

        if user == None:
            return

        target = user.id

        if badgename == '':
            return 

        if int(ctx.author.id) in admin:
            if badgename not in badgee[target]:
                await ctx.channel.send('This user does not have this badge.')
            else:
                badgee[target].remove(badgename)
                await message.channel.send(f'Sucessfully removed **{badgename}** from **{user.name}**')
        else:
            await ctx.channel.send('You do not have permission to run this command.')


'''
██████   █████  ███████ ██  ██████ 
██   ██ ██   ██ ██      ██ ██      
██████  ███████ ███████ ██ ██      
██   ██ ██   ██      ██ ██ ██      
██████  ██   ██ ███████ ██  ██████ 
'''




class basic_commands(commands.Cog, name='basic'):

    def __init__(self, client):
        self.client = client


    @commands.command(name='latency', aliases=['ping'], description='Check the latency of the bot', usage='latency')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def latency(self, ctx):
        await ctx.channel.send(f'This number really doesn\'t matter: `{round(self.client.latency * 1000, 1)}` ms.')

    @commands.command(name='say', description='make the bot say something', usage='say <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def say(ctx, *, msg):
        await ctx.channel.send(msg, allowed_mentions=discord.AllowedMentions(everyone=False,users=False, roles=False))

    @commands.command(name='xp', aliases=['level', 'lvl', 'rank', 'exp'], description='check your xp', usage='xp [user]')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def xpcommand(self, ctx, user: discord.User = None):
        if user == None:
            user = ctx.author
        xpe = discord.Embed(title=f"{user.name}'s xp", color=random.randint(0, 16777215))
        xpe.add_field(name='XP',value=f'{xp[user.id][0]:,} <:orb:792186055339933736>')
        xpe.add_field(name='Level',value=f'{math.floor(xp[user.id][0]/100):,} ',inline=False)
        if xp[user.id][0] <= 499:
            xpe.add_field(name='Rank',value='200 IQ')
        elif xp[user.id][0] <= 999:
            xpe.add_field(name='Rank',value='SMART')
        elif xp[user.id][0] <= 1999:
            xpe.add_field(name='Rank',value='NORMAL')
        elif xp[user.id][0] <= 3999:
            xpe.add_field(name='Rank',value='DUMB')
        elif xp[user.id][0] <= 7999:
            xpe.add_field(name='Rank',value='STUPID')
        elif xp[user.id][0] <= 9999:
            xpe.add_field(name='Rank',value='VERY STUPID')
        elif xp[user.id][0] <= 99999999:
            xpe.add_field(name='Rank',value='DUMBEST IDIOT IN THE WORLD')
        elif xp[user.id][0] >= 100000000:
            xpe.add_field(name='Rank',value='NEGATIVE IQ')
        await ctx.channel.send(embed=xpe)




'''
 ██████  ██████  ███    ██ ███████ ██  ██████  ██    ██ ██████   █████  ████████ ██  ██████  ███    ██ 
██      ██    ██ ████   ██ ██      ██ ██       ██    ██ ██   ██ ██   ██    ██    ██ ██    ██ ████   ██ 
██      ██    ██ ██ ██  ██ █████   ██ ██   ███ ██    ██ ██████  ███████    ██    ██ ██    ██ ██ ██  ██ 
██      ██    ██ ██  ██ ██ ██      ██ ██    ██ ██    ██ ██   ██ ██   ██    ██    ██ ██    ██ ██  ██ ██ 
 ██████  ██████  ██   ████ ██      ██  ██████   ██████  ██   ██ ██   ██    ██    ██  ██████  ██   ████ 
'''




class configuration_commands(commands.Cog, name='configuration'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='serverinfo', aliases=['guildinfo', 'guild', 'server'], description='check server information', usage='serverinfo')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverinfo(self, ctx):
        if len(ctx.guild.features) == 0:
            featuress = 'None'
        else:
            featuress = '\n'.join(ctx.guild.features)
        channelamount = len(ctx.guild.text_channels)
        channelamount2 = len(ctx.guild.voice_channels)
        level2fa = {1: 'High', 
            2: "Low",
            0: 'None'}
        creation_date = math.floor(ctx.guild.created_at.timestamp())
        serverinfo = discord.Embed(title='Server Info', color=random.randint(0, 16777215))
        serverinfo.set_author(name=f'{ctx.guild}', icon_url=ctx.guild.icon_url)
        serverinfo.add_field(name='Basic',value=f'**Member Count:** {ctx.guild.member_count}\n**Creation Date:** <t:{creation_date}> (<t:{creation_date}:R>)\n**Region:** {ctx.guild.region}\n**Owner:** <@!{ctx.guild.owner_id}>\n**Text Channels:** {channelamount}\n**Voice Channels:** {channelamount2}')
        serverinfo.add_field(name='Security', value=f'**2fa:** {level2fa[ctx.guild.mfa_level]}\n**Verification Level:** {ctx.guild.verification_level}')
        serverinfo.add_field(name='Features',value=f'{featuress}', inline=False)
        serverinfo.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.channel.send(embed=serverinfo)


    @commands.command(name='userinfo', aliases=['user'], description='check user information', usage='userinfo <user>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx, user: discord.User = None):
        if user == None:
            user = ctx.author
        creation_date = math.floor(user.created_at.timestamp())
        serverinfo = discord.Embed(title='User Info', color=random.randint(0, 16777215))
        serverinfo.set_author(name=f'{user}', icon_url=user.avatar_url)
        serverinfo.add_field(name='ID', value=f'{user.id}')
        serverinfo.add_field(name='Creation Date',value=f'<t:{creation_date}> (<t:{creation_date}:R>)')
        serverinfo.set_thumbnail(url=user.avatar_url)
        await ctx.channel.send(embed=serverinfo)


    @commands.command(name='settings', aliases=['uconfig'], description='User settings', usage='settings [number] [true/false]')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def usettings(self, ctx, number: int = 0, tf: bool = True):

        user = ctx.author.id

        if number == 0 and tf:
            colorsquares = {True: '\U0001f7e9', False: '\U0001f7e5'}
            confige = discord.Embed(title='User Settings', color=random.randint(0, 16777215))
            confige.set_author(name=f'{ctx.author.name}', icon_url=ctx.author.avatar_url)
            confige.add_field(name='\u2460 Reply Mention',value=f'Toggles if you want replys to mention you.\n{colorsquares[userconfig[user][0]]}**{userconfig[user][0]}**')
            #confige.add_field(name='\u2461 Update DM',value=f'Sends you a DM when a new version is released.\n{colorsquares[userconfig[user][1]]}**{userconfig[user][1]}**')
            await ctx.channel.send(embed=confige)
        else:
            configse = ["Reply Mention"]
            #"Update DM"]
            number1 = number - 1
            if tf.lower() == 'true' or tf.lower() == 't':
                userconfig[user][number1] = True
                await ctx.channel.send(f'Sucessfully set `{configse[number]}` to **True**')
            if tf.lower() == 'false' or tf.lower() == 'f':
                userconfig[user][number1] = False
                await ctx.channel.send(f'Sucessfully set `{configse[number]}` to **False**')


    @commands.command(name='config', aliases=['guildconfig', 'serverconfig'], description='server settings', usage='config [number] [true/false]')
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def gconfig(self, ctx, number: int = 0, tf: bool = True):
        if number == 0 and tf:
            colorsquares = {True: '\U0001f7e9', False: '\U0001f7e5'}
            confige = discord.Embed(title='Guild Configurations', description=f'Configuration settings for {ctx.guild}. You must have `manage server` to change these.\nUse **bot configuration <setting-number> <true/false>** to change a setting.', color=random.randint(0, 16777215))
            confige.set_author(name=f'{ctx.guild}', icon_url=ctx.guild.icon_url)
            confige.add_field(name='\u2460 Stupid/Idiot Auto Repsond',value=f'Toggles a message if the word *stupid* or *idiot* is in it.\n{colorsquares[config[message.guild.id][0][0]]}**{config[message.guild.id][0][0]}**')
            confige.add_field(name='\u2461 Events',value=f'Currency events that will have a rare chance of spawning.\n{colorsquares[config[ctx.guild.id][0][1]]}**{config[message.guild.id][0][1]}**')
            await ctx.channel.send(embed=confige)
        else:
            configse = {1: 'Stupid/Idiot Auto Repsond',
            2: 'Events'}
            if number > len(config[ctx.guild.id][0]):
                return
            else:
                number1 = number - 1
                if tf.lower() == 'true' or tf.lower() == 't':
                    config[ctx.guild.id][0][number1] = True
                    await ctx.channel.send(f'Sucessfully set `{configse[number]}` to **True**')
                if tf.lower() == 'false' or tf.lower() == 'f':
                    config[ctx.guild.id][0][number1] = False
                    await ctx.channel.send(f'Sucessfully set `{configse[number]}` to **False**')


    @commands.command(name='autorespond', aliases=['ar'], description='autoresponds for this server', usage='autoresponds [+/-] [message]|[responds]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def autore(self, ctx, adsu: str = '', *, arg1: str = ''):
        if adsu == '' and arg1 == '':
            if len(config[ctx.guild.id][1]) == 0:
                arr = 'There are no auto responds.'
            else:
                arr = '\n'.join(list(config[ctx.guild.id][1]))
            ars = discord.Embed(title= 'Auto Responds', color=random.randint(0, 16777215), description='To add auto responds do `autorespond <+/-> <message>|<responds>`')
            ars.add_field(name='​', value=arr)
            await ctx.channel.send(embed=ars)
        else:
            if ctx.author.permissions_in(ctx.channel).administrator or ctx.author.permissions_in(ctx.channel).manage_guild or int(ctx.author.id) in admin:
                if adsu == '+' or adsu == 'add':
                    try:
                        msg, resp = arg1.split('|')[0:]
                    except IndexError:
                        await ctx.channel.send('You have to tell me what to add.\n`autorespond <+/-> <message>|<responds>`')
                    except ValueError:
                        await ctx.channel.send('You have to tell me what to add.\n`autorespond <+/-> <message>|<responds>`')
                    else:
                        msg1 = msg.split(' ')[3:]
                        if len(msg1) == 1:
                            msg2 = msg.split(' ')[3]
                        else:
                            msg2 = " ".join(msg1)
                        config[ctx.guild.id][1][msg2.lower()] = resp
                        await ctx.channel.send('Sucessfully added.')
                if adsu == '-' or adsu == 'subtract':
                    msg1 = arg1.split('|')[:1]
                    msg2 = " ".join(msg1)
                    try:
                       del config[ctx.guild.id][1][msg2.lower()]
                    except KeyError:
                        await ctx.channel.send('Trigger does not exsist')
                    else:
                        await ctx.channel.send('Sucessfully deleted trigger.')
            else:
                await ctx.channel.send('You do not have the permission to edit auto responds. (manage server)')




'''
 ██████ ██    ██ ██████  ██████  ███████ ███    ██  ██████ ██    ██ 
██      ██    ██ ██   ██ ██   ██ ██      ████   ██ ██       ██  ██  
██      ██    ██ ██████  ██████  █████   ██ ██  ██ ██        ████   
██      ██    ██ ██   ██ ██   ██ ██      ██  ██ ██ ██         ██    
 ██████  ██████  ██   ██ ██   ██ ███████ ██   ████  ██████    ██    
'''



class currency_commands(commands.Cog, name='currency'):

    def __init_(self, client):
        self.client = client

    @commands.command(name='balance', aliases=['bal', 'wallet'], description='check your balance', usage='balance [user]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def balance(self, ctx, user: discord.User = None):
        if user == None:
            user = ctx.author
        bal = discord.Embed(
        title=f"{user.name}'s BALANCE", color=random.randint(0, 16777215))
        bal.add_field(name='Wallet', value=f'{getcoins(user.id)[0]:,}')
        bal.add_field(name='Bank', value=f'{getcoins(user.id)[1]:,}/{getbank(user.id):,}')
        await ctx.channel.send(embed=bal)

    @commands.command(name='beg', description='beg for money', usage='beg')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def beg(self, ctx):
        user = ctx.author.id
        number = random.randint(1, 200)
        if number == 1:  # 0.5%
            await ctx.channel.send(
                'You met a nice person he/she donated you 200 coins')
            setcoins(user, coin1=getcoins(user)[0] + 200)
        elif number <= 3:  # 1.5% (1.5%)
            await ctx.channel.send('You can only have 5 coins')
            setcoins(user, coin1=getcoins(user)[0] + 5)
        elif number <= 10:  # 5% (3.5%)
            await ctx.channel.send('4 coins is alot, bare with me')
            setcoins(user, coin1=getcoins(user)[0] + 4)
        elif number <= 30:  # 15% (10%)
            await ctx.channel.send('Sorry, only 3 for you')
            setcoins(user, coin1=getcoins(user)[0] + 3)
        elif number <= 120:  # 60% (45%)
            await ctx.channel.send('I feel bad, here is 2 coins')
            setcoins(user, coin1=getcoins(user)[0] + 2)
        elif number <= 180:  # 90% (30%)
            await ctx.channel.send("I'm poor, only 1 coin for you")
            setcoins(user, coin1=getcoins(user)[0] + 1)
        elif number <= 199:  # 99.5% (9.5%)
            await ctx.channel.send('Non. For. You.')
        else:
            await ctx.channel.send(
                'EW No! You are the dumest person I have ever met.')

    # @commands.command(name='apply', description='apply for a job', usage='apply <job-name>') #we need a new alg for this cmd
    # @commands.cooldown(1, 5, commands.BucketType.user)
    # async def applycommand(self, ctx, job: str):

    #     jobstm = {'teacher': [100, 2, [1, 100, 25]], 'police': [180, 3, [1, 2, 2]]} # sal, job_num, {rates}

    #     job = job.lower()

    #     if job.lower() == 'waittress':
    #         if getjob(user)[0] == 0 and getquit(user) < time.time():
    #             setjob(user, new_job=1)
    #             setsalary(user, 50)
    #             await ctx.channel.send(
    #                 "Congratulations! You are now working as a waittress!")
    #         elif getjob(user)[0] > 0:
    #             await ctx.channel.send("You already have a job.")
    #         elif getquit(user) > time.time():
    #             await ctx.channel.send(
    #                 f"""You cannot apply for a job for another **{int((quit[user]-time.time())/3600)}h {int(quit[user]-time.time())%60}m. **"""
    #             )
    #     else:
    #         if getjob(user)[0] == 0 and getquit(user) < time.time():
    #             accept = random.randint(jobstm[job][2][0], jobstm[job][2][1])
    #             if accept > jobstm[job][2][2]:
    #                 setjob(user, new_job=jobstm[job][1])
    #                 setsalary(user, jobstm[job][0])
    #                 await ctx.channel.send(
    #                     f"Congratulations! You are now working as a {job.lower()}!")
    #             else:
    #                 await ctx.channel.send(
    #                     "Sorry, you were not accepted to your job.")
    #         elif getjob(user)[0] > 0:
    #             await ctx.channel.send("You already have a job.")
    #         elif getquit(user) > time.time():
    #             await ctx.channel.send(
    #                 f"""You cannot apply for a job for another **{int((quit[user]-time.time())/3600)}h {int(quit[user]-time.time())%60}m. **""")

    #     if message.content.lower() == 'bot apply programmer':
    #         if getjob(user)[0] == 0 and getquit(user) < time.time():
    #             programmer = random.randint(1, 10)
    #             if programmer == 1:
    #                 setjob(user, new_job=4)
    #                 setsalary(user, 250)
    #                 await message.channel.send(
    #                     "Congratulations! You are now working as a programmer!")
    #             elif programmer >= 2:
    #                 await message.channel.send(
    #                     "Sorry, you were not accepted to your job.")
    #         elif getjob(user)[0] > 0:
    #             await message.channel.send("You already have a job")
    #         elif getquit(user) > time.time():
    #             await message.channel.send(
    #                 f"""You cannot apply for a job for another **{int((quit[user]-time.time())/3600)}h {int(quit[user]-time.time())%60}m. **"""
    #             )

    #     if message.content.lower() == "bot apply geeson's stupid bot programmer":
    #         if getjob(user)[0] == 0 and getquit(user) < time.time():
    #             Geeson = random.randint(1, 10000)
    #             if Geeson == 1:
    #                 setjob(user, new_job=5)
    #                 setsalary(user, 200000000)
    #                 await message.channel.send(
    #                     "Congratulations! You are now working as a Geeson's Stupid Bot Programmer!"
    #                 )
    #             elif Geeson >= 2:
    #                 await message.channel.send(
    #                     "Sorry, you were not accepted to your job.")
    #         elif getjob(user)[0] > 0:
    #             await message.channel.send("You already have a job.")
    #         elif getquit(user) > time.time():
    #             await message.channel.send(
    #                 f"""You cannot apply for a job for another **{int((quit[user]-time.time())/3600)}h {int(quit[user]-time.time())%60}m. **""")


    @commands.command(name='rich', aliases=['lb', 'leaderboards', 'leaderboard', 'baltop'], description='who rich?', usage='rich [page]')
    @commands.guild_only()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def rich(self, ctx, page: int = 1):
        if page <= 0:
            return await ctx.send('Page numbers should be an non zero integer.')
        user = ctx.author.id
        leaderboards = []
        for key, value in coins.items():
            if self.client.get_user(key) in ctx.guild.members:
                leaderboards.append(LeaderBoardPosition(key, value))
        top = sorted(leaderboards, key=lambda x: x.coins[0], reverse=True)
        rich = discord.Embed(title=f'Richest Users in {ctx.guild.name}', color=random.randint(0, 16777215))
        rich.set_footer(text=f'Page {page} of {math.ceil(len(top)/5)}')
        if page == 1:
            num1 = 0
        else:
            num1 = 5 * (page-1)
        num2 = num1 + 5
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        for i in range(num1, num2):
            try:
                rich.add_field(name=f'{ordinal(i+1)}: {self.client.get_user(top[i].user)}', value=f'{top[i].coins[0]:,} coins', inline=False)
            except IndexError:
                break
        await ctx.channel.send(embed=rich)


    @commands.command(name='globalrich', aliases=['glr', 'grich', 'glb', 'globalleaderboards', 'globalleaderboard', 'glbs'], description='who rich?', usage='globalrich [page]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def globalrich(self, ctx, page: int = 1):
        if page <= 0:
            return await ctx.send('Page numbers should be an non zero integer.')
        user = ctx.author.id
        leaderboards = []
        for key, value in coins.items():
            leaderboards.append(LeaderBoardPosition(key, value))
        top = sorted(leaderboards, key=lambda x: x.coins[0], reverse=True)
        rich = discord.Embed(title='Most Wealthy Users (Globally)',color=random.randint(0, 16777215))
        rich.set_footer(text=f'Page {page} of {math.ceil(len(top)/5)}')
        if page == 1:
            num1 = 0
        else:
            num1 = 5 * (page-1)
        num2 = num1 + 5
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        for i in range(num1, num2):
            try:
                rich.add_field(name=f'{ordinal(i+1)}: {self.client.get_user(top[i].user)}', value=f'{top[i].coins[0]:,} coins', inline=False)
            except IndexError:
                break
        await ctx.channel.send(embed=rich)


    @commands.command(name='ticket', aliases=['lottery'], description='buy a lottery ticket', usage='ticket [type]')
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def ticket(self, ctx, type: str = 'normal'):

        user = ctx.author.id

        if type == 'normal':
            if getcoins(user)[0] <= 10:
                await ctx.channel.send('You need 10 coins for a ticket')
            elif getcoins(user)[0] >= 10:
                ticketr = random.randint(1, 500)
                setcoins(user, coin1=getcoins(user)[0] - 10)
                if ticketr == 1:  #0.2%
                    await ctx.channel.send('You won 10000 coins')
                    setcoins(user, coin1=getcoins(user)[0] + 10000)
                if ticketr >= 2:  #98.8%
                    await ctx.channel.send(
                        "Unfortunatly, your ticket wasn't so lucky")

        if type == 'small':
            if getcoins(user)[0] < 5:
                await ctx.channel.send('You need 5 coins for a ticket')
            elif getcoins(user)[0] >= 5:
                ticketrc = random.randint(1, 10)
                setcoins(user, coin1=getcoins(user)[0] - 5)
                if ticketrc == 1:  #10%
                    await ctx.channel.send('You won 100 coins')
                    setcoins(user, coin1=getcoins(user)[0] + 100)
                elif ticketrc >= 2:  #90%
                    await ctx.channel.send(
                        "Unfortunatly, your ticket wasn't so lucky")



    @commands.command(name='search', aliases=['scout'], description='search around and get something', usage='search')
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def search(self, ctx):

        user = ctx.author.id

        searchr = random.randint(1,200)
        if searchr <= 30: #10%
            r1 = random.randint(100,500)
            await ctx.channel.send(f'You got {r1} coins.')
            setcoins(user, coin1=getcoins(user)[0]+r1)
        elif searchr <= 50: #15%
            r2 = random.randit(10,99) 
            await ctx.channel.send(f'You got {r2} coins.')
            setcoins(user, coin1=getcoins(user)[0]+r2)
        elif searchr <= 200: #75%
            await ctx.channel.send('You went searching and found nothing.')



    @commands.command(name='daily', description='get daily coins', usage='daily')
    async def dailye(self, ctx):

        user = ctx.author.id

        if (user in daily) and daily[user] > time.time():
            waittime = daily[user] - time.time()
            await ctx.channel.send(
                f'Please wait **{math.floor(waittime/3600)}h {math.floor((waittime/60) % 60) if waittime % 60 != 59 else 59}m** to use this again!'
            )
        else:
            amount = random.randint(500, 700)
            await ctx.channel.send(f'You got {amount} daily coins!')
            setcoins(user, coin1=getcoins(user)[0] + amount)
            daily[user] = time.time() + 86400



    @commands.command(name='weekly', description='get weekly coins', usage='weekly')
    async def weeklye(self, ctx):

        user = ctx.author.id

        if xp[user][0] < 500:
            await ctx.channel.send('You must be level 5 to use this command.\nDo `bot xp` to check your xp.')
        else:
            if (user in weekly) and weekly[user] > time.time():
                waittimew = weekly[user] - time.time()
                await ctx.channel.send(
                    f'Please wait **{math.floor(waittimew/86400)}d {math.floor(waittimew/3600) % 24 if waittimew % 24 != 23 else 23}h {math.ceil((waittimew/60) % 60) if waittimew % 60 != 59 else 59}m** to use this again!'
                )
            else:
                amount = random.randint(2000, 2500)
                await ctx.channel.send(f'You got {amount:,} weekly coins!')
                setcoins(user, getcoins(user)[0] + amount)
                weekly[user] = time.time() + 604800


    @commands.command(name='jobs', description='view the jobs', usage='usage')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def jobs(self, ctx):
        jobs = discord.Embed(title='Jobs:', color=random.randint(0, 16777215))
        jobs.add_field(
            name='Waittress',
            value='50 coins/hr, 1 hr/day required',
            inline=False)  # 1
        jobs.add_field(
            name='Teacher',
            value='100 coins/hr, 5 hr/day required, 75% acceptance',
            inline=False)  # 2
        jobs.add_field(
            name='Police',
            value='180 coins/hr, 8 hr/day required, 50% acceptance',
            inline=False)  # 3
        jobs.add_field(
            name='Programmer',
            value='250 coins/hr, 4 hr/day required, 10% acceptance',
            inline=False)  # 4
        jobs.add_field(
            name="Geeson's Stupid Bot Programmer",
            value='500 coins/hr, 6 hr/day required, 0.001% acceptance',
            inline=False)  # 5
        await ctx.channel.send(embed=jobs)


    @commands.command(name='work', description='work to get money', usage='work [quit]')
    async def worke(self, ctx, quit: str = ''):

        user = ctx.author.id

        if quit == '':
            if getjob(user)[0] == 0:
                await ctx.channel.send("You don't have a job yet")
            if getjob(user)[0] > 0 and (user in work) and work[user] > time.time():
                await ctx.channel.send(
                    f"""You need to wait **{int((work[user]-time.time())/60)%60}m {int(work[user]-time.time())%60}s** before you could work again"""
                )
            elif job[user][0] > 0:
                await ctx.channel.send(
                    f"""You earned {str(salary[user])} Coins!""")
                work[user] = time.time() + 3600
                setcoins(user, coin1=getcoins(user)[0] + getsalary(user))
                setjob(user, times=getjob(user)[1]+1)

        if quit == 'quit' or quit == 'leave' or quit == 'resign':
            if getjob(user)[0] >= 0:
                setjob(user, new_job=0)
                setsalary(user, 0)
                quit[user] = time.time() + 86164
                await ctx.channel.send(
                    "You quit your job. You have to wait **23 hours, 56 minutes, and 04 seconds** until you can apply for another job."
                )
            else:
                await ctx.channel.send("You don't have a job yet")
      


    @commands.command(name='shop', aliases=['store'], description='see whats in the shop', usage='shop [page]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def shop(self, ctx, page: int = 1):

        user = ctx.author.id

        pagenum = math.ceil(len(shopi.keys())/4)
        if page > pagenum:
            await ctx.channel.send(f'There is no page {page}, you dumbo.')
        else:
            invnum = 0
            for i in range(1, len(inv[user])):
                invnum += inv[user][i]
            lownum = math.floor((page * 4) - 4)
            if page == pagenum:
                maxnum = len(shopi.keys())
            elif page == 1:
                maxnum = 4
            else:
                maxnum = math.floor((page * 4))
            shop0 = []
            for i in range(lownum, maxnum):
                keyee = list(shopi.keys())[i]
                shop0.append(f"**{shopi[keyee][1]} {shopi[keyee][2]} (costs {shopi[keyee][0]:,} coins) - id `{keyee}`**\n{shopi[keyee][3]}")
            shopp = "\n\n".join(shop0)
            shop = discord.Embed(title='SHOP',color=random.randint(0, 16777215), description=f'Check out our shop. You own `{invnum}` items')
            shop.add_field(name='Item Shop', value= shopp)
            shop.set_footer(text=f'Page {page} of {pagenum}',icon_url='')
            await ctx.channel.send(embed=shop)


    @commands.command(name='buy', description='buy things from the shop', usage='buy <item> [amount]')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def buy(self, ctx, id: str, value: str = '1'):

        user = ctx.author.id

        try:
            value = int(value)
        except ValueError:
            value = int(si_prefix(value))


        items_id = list(shopi.keys())
        if id in items_id:
            if id == 'pick':
                if getcoins(user)[0] < 10000:
                    await ctx.channel.send('you do-nut have enough money.')
                elif inv[user][0][0] == True:
                    await ctx.channel.send('You already have a pickaxe, you may not by another one.')
                else:
                    inv[user][0][0] = True
                    setcoins(user, getcoins(user)[0]-10000)
                    await ctx.channel.send('You bought a pickaxe for **10,000** coins.')
            elif id == 'mention':
                if value * 1000000 > getcoins(user)[0]:
                        await ctx.channel.send('You do-nut have enough money.')
                else:
                    if value >= 34:
                        return await ctx.channel.send('You cannot buy more than `33` mentions at once.')
                    await ctx.channel.send(f'You bought a mention so here it is → {ctx.author.mention}\n' * value)
                    setcoins(user, coin1=getcoins(user)[0]- 1000000 * value)
            else:
                if getcoins(user)[0] < shopi[id][0] * value:
                    await ctx.channel.send('You do-nut have enough money.')
                else:
                    await ctx.channel.send(f'You bought `{value:,}` {shopi[id][1]} `{shopi[id][2]}` for `{shopi[id][0]}`s for `{shopi[id][0]*value:,}` coins.')
                    setcoins(user, getcoins(user)[0]-shopi[id][0]*value)
                    inv[user][shopi[id][4]] += value
        else:
            await ctx.channel.send('That item is not in the shop.')

        


    @commands.command(name='inv', aliases=['inventory'], description='check whats in your inventroy', usage='inv [user]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def inve(self, ctx, user: discord.User = None):
        if user == None:
            user = ctx.author
        inve = discord.Embed(
            title=f"{user.name}'s INVENTORY", color=random.randint(0, 16777215))
        for i in range(1, len(inv[user.id])):
            if inv[user.id][i] > 0:
                inve.add_field(name=f'{invname[i][0]} {invname[i][1]}', value=f'{inv[user.id][i]:,}', inline=False)
        await ctx.channel.send(embed=inve)


    @commands.command(name='debt', description='check your debt', usage='debt')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def debte(self, ctx):
      
        user = ctx.author.id
        
        await ctx.channel.send(f'Your have a debt of {getdebt(user)[0]:,}')
        

    @commands.command(name='borrow', description='borrow money from the bank, but you need to pay them back', usage='borrow <amount>')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def borrow(self, ctx, amount: int = 0):

        user = ctx.author.id

        if getjob(user)[0] == 0:
            return await ctx.channel.send('oi, you need a job to borrow money')
        if getdebt(user)[0] > 0:
            return await ctx.channel.send('pay your debt to borrow again')
        if amount <= 0:
            return await ctx.channel.send('you need to borrow postive amount of coins')
        if getjob(user)[0] == 1:
            highest_amount = 100
        elif getjob(user)[0] == 2:
            highest_amount = 1000
        elif getjob(user)[0] == 3:
            highest_amount = 10000
        elif getjob(user)[0] == 4:
            highest_amount = 100000
        if highest_amount < amount:
            await ctx.channel.send(f'You can only borrow {highest_amount:,} coins.')
        else:
            setcoins(user, coin1=getcoins(user)[0]+amount)
            setdebt(user, debtt=getdebt(user)[0]+amount, debtday=time.time()+604800)
            await ctx.channel.send(f'you borrowed {amount:,} coins')


    @commands.command(name='pay', description='pay your debt back', usage='pay')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pay(self, ctx):

        user = ctx.author.id
        
        if getdebt(user)[0] == 0:
            await ctx.channel.send('You have no debt.')
        if getdebt(user)[0] > getcoins(user)[0]:
            await ctx.channel.send('You do not have enough money to pay your debt.')
        else:
            setcoins(user, coin1=getcoins(user)[0]-getdebt(user)[0])
            setdebt(user, debtt=0, debtday=0)
            await ctx.channel.send('You paid your debt, now you can borrow again.')


    @commands.command(name='share', aliases=['give'], description='share money with your friends', usage='share <user> <amount>')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def sharee(self, ctx, target: discord.User=None, amount: str = '0'):

        user = ctx.author.id

        try:
            amount = int(amount)
        except ValueError:
            amount = int(si_prefix(amount))


        if target == None:
            await ctx.send('Who do you want to share coins with?')
        if target.id == ctx.author.id:
            return await ctx.channel.send('You cannot share stuff with yourself.')
        if amount > getcoins(user)[0]:
            await ctx.channel.send('ARE YOU TRYING TO HJACK THE SYSTEM?')
        elif amount < 0:
            await ctx.channel.send('ARE YOU TRYING TO HJACK THE SYSTEM?')
        else:
            setcoins(target.id, coin1=getcoins(target.id)[0]+amount)
            setcoins(user, coin1=getcoins(user)[0]-amount)
            await ctx.channel.send(f"""You gave **{amount:,}** coins to **{target.name}**, and now you have {getcoins(user)[0]:,}.""")


    @commands.command(name='deposite', aliases=['dep'], description='deposite coins to your bank', usage='deposite <amount>')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def depositecoins(self, ctx, amount=''):

        user = ctx.author.id

        if amount == '':
            return await ctx.send('How much coins do you want to deposite?')

        if amount in ['total', 'everything', 'max', 'all']:
            if getcoins(user)[1] == getbank(user):
                await ctx.channel.send('Boi, you have a max bank.')
            elif getcoins(user)[0] == 0:
                await ctx.channel.send('You have no coins, sucks to be you.')
            else:
                if getcoins(user)[0] > getbank(user):
                    dep = getbank(user) - getcoins(user)[1]
                    await ctx.channel.send(f'**{dep:,}** coins deposited.')
                    setcoins(user, coin1=getcoins(user)[0]-dep)
                    setcoins(user, coin2=getcoins(user)[1]+dep)
                elif getcoins(user)[0] < getbank(user):
                    dep = getbank(user) - getcoins(user)[1]
                    if dep > getcoins(user)[0]:
                        dep = getcoins(user)[0]
                    await ctx.channel.send(f'**{dep:,}** coins deposited.')
                    setcoins(user, coin1=getcoins(user)[0]-dep)
                    setcoins(user, coin2=getcoins(user)[1]+dep)
            return

        try:
            amount = int(amount)
        except ValueError:
            amount = int(si_prefix(amount))


        if getcoins(user)[1] == getbank(user):
            await ctx.channel.send('Boi, you have a max bank.')
        elif getcoins(user)[0] < amount:
            await ctx.channel.send(f"You don't have **{amount:,}** coin(s), you only have {getcoins(user)[0]:,}")
        elif getcoins(user)[0] == 0:
            await ctx.channel.send('You have no coins, sucks to be you.')
        elif amount > getbank(user) - getcoins(user)[1]:
            await ctx.channel.send(f'You do not have enough bank space for **{amount:,}** coins.')
        else:
            await ctx.channel.send(f'**{amount:,}** coins deposited.')
            setcoins(user, coin1=getcoins(user)[0]-amount)
            setcoins(user, coin2=getcoins(user)[1]+amount)


    @commands.command(name='withdraw', aliases=['with'], description='withdraw money', usage='withdraw <amount>')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def withdrawcoins(self, ctx, amount=''):

        user = ctx.author.id

        if amount == '':
            return await ctx.send('How much coins do you want to deposite?')

        if amount in ['total', 'all', 'max', 'everything']: 
            if getcoins(user)[1] == 0:
                await ctx.channel.send('You have no coins in your bank.')
            else:
                with1 = getcoins(user)[1]
                await ctx.channel.send(f'**{with1:,}** coins withdrawn.')
                setcoins(user, coin1=getcoins(user)[0]+with1)
                setcoins(user, coin2=getcoins(user)[1]-with1)
            return

        try:
            amount = int(amount)
        except ValueError:
            amount = int(si_prefix(amount))


        if getcoins(user)[1] == 0:
            await ctx.channel.send('You have no coins in your bank.')
        elif getcoins(user)[1] < with1:
            await ctx.channel.send("You don't have that much in your bank")
        else:
            await ctx.channel.send(f'**{with1}** coins withdrawn.')
            setcoins(user, coin1=getcoins(user)[0]+with1)
            setcoins(user, coin2=getcoins(user)[1]-with1)


    @commands.command(name='bankupgrade', aliases=['upgradebank'], description='upgrade the maximum capacity of your bank', usage='bankupgrade')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def bankupgrade(self, ctx):

        user = ctx.author.id

        fee = math.floor(getbank(user) / 10)
        if fee > getcoins(user)[0]:
            await ctx.channel.send(f'You do not have enough on hand to upgarde your bank. You will need (**{fee:,}**).')
        else:
            ebs = random.randint(1000,10000)
            await ctx.channel.send(f'You spent **{fee:,}** coins and they let you have an extra {ebs:,} bank space.')
            setcoins(user,coin1=getcoins(user)[0]-fee)
            setbank(user, getbank(user)+ebs)


    @commands.command(name='rob', aliases=['steal'], description='go rob some people, but don\'t get caught', usage='rob <user>')
    @commands.cooldown(1, 180, commands.BucketType.user)
    async def robcommand(self, ctx, target: discord.User = None):

        user = ctx.author.id

        if target == None:
            target = ctx.author

        if target.id == user:
            await ctx.channel.send('You can not rob yourself.')
            return
        if target.bot:
            await ctx.channel.send("You can't steal from bots.")
            return
        if getcoins(target.id)[0] < 100:
            await ctx.channel.send('Not worth it man, they have less than 100 coins.')
        else:
            rob = random.randint(1,30)
            if rob <= 20:
                await ctx.channel.send(f'You tried to rob {target.name}, and they caught you. You spent 100 coins to get out of jail.')
                setcoins(user, coin1=getcoins(user)[0]-100)
            else:
                percentr = random.randint(1,99)
                coinsr = math.floor(getcoins(target.id)[0]*(percentr)/100)
                if coinsr >= 10000:
                    await ctx.channel.send(f'<a:fire_animated:778776515126362142> Your payout was **{coinsr:,}**.')
                else:
                    await ctx.channel.send(f':money_mouth: Your payout was **{coinsr:,}**.')
                setcoins(user, coin1=getcoins(user)[0]+coinsr)
                setcoins(target.id, coin1=getcoins(target.id)[0]-coinsr)
                await target.send(f'**You were stolen from**\n**{ctx.author.name}** stole **{coinsr:,}** coins from you in **{self.client.get_guild(ctx.guild.id)}**.')


    @commands.command(name='bet', aliases=['gamble'], description='go to the casino and gamble', usage='bet <amount>')
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def betcommand(self, ctx, amount=''):
        
        user = ctx.author.id

        if amount == '':
            return await ctx.send('How many coins do you want to bet on.')

        if amount == 'max':
            if getcoins(user)[0] > 200000:
                amount = 200000
            else:
                amount = getcoins(user)[0]
        if amount == 'half':
            if getcoins(user)[0] > 200000:
                amount = 100000
            else:
                amount = math.floor(getcoins(user)[0]/2)


        try:
            amount = int(amount)
        except ValueError:
            amount = int(si_prefix(amount))

        if amount < 200:
            await ctx.send('You need to bet at least 200 coins.')
        elif amount > getcoins(user)[0]:
            await ctx.send(f'You do not have {amount:,} coins, you only have {getcoins(user)[0]:,}.')
        elif amount > 500000:
            await ctx.send('You cannot bet more than 500,000 coins.')

        dealer_roll = random.randint(1, 16)
        user_roll = random.randint(1, 16)

        betembed = discord.Embed(color=random.randint(1, 16777215), description=f'{amount:,} coins')
        betembed.set_author(name=f'{ctx.author.name}\'s Game', icon_url=ctx.author.avatar_url)
        betembed.add_field(name='Dealer Rolled', value=f'`{dealer_roll}`')
        betembed.add_field(name='You Rolled', value=f'`{user_roll}`')
        msg = await ctx.send(embed=betembed)

        await asyncio.sleep(1)

        if user_roll == dealer_roll:
            betembed = discord.Embed(color=0xFFFF00, description=f'{amount:,} coins\n\n**Tie**, you won `0` coins.')
            betembed.set_author(name=f'{ctx.author.name}\'s Game', icon_url=ctx.author.avatar_url)
            betembed.add_field(name='Dealer Rolled', value=f'`{dealer_roll}`')
            betembed.add_field(name='You Rolled', value=f'`{user_roll}`')
            await msg.edit(embed=betembed)
        if user_roll < dealer_roll:
            betembed = discord.Embed(color=0xFF0000, description=f'{amount:,} coins\n\n**Lose**, you lost {amount:,} coins.')
            betembed.set_author(name=f'{ctx.author.name}\'s Game', icon_url=ctx.author.avatar_url)
            betembed.add_field(name='Dealer Rolled', value=f'`{dealer_roll}`')
            betembed.add_field(name='You Rolled', value=f'`{user_roll}`')
            await msg.edit(embed=betembed)
            setcoins(user, getcoins(user)[0]-amount)
        if user_roll > dealer_roll:
            betembed = discord.Embed(color=0x00FF00, description=f'{amount:,} coins\n\n**Win**, you won {amount:,} coins.')
            betembed.set_author(name=f'{ctx.author.name}\'s Game', icon_url=ctx.author.avatar_url)
            betembed.add_field(name='Dealer Rolled', value=f'`{dealer_roll}`')
            betembed.add_field(name='You Rolled', value=f'`{user_roll}`')
            await msg.edit(embed=betembed)
            setcoins(user, getcoins(user)[0]+amount)


    @commands.command(name='sell', description='sell your items', usage='sell <item> [amount]')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def sellcommand(self, ctx, id: str = '', value: int = 1):

        user = ctx.author.id

        try:
            value = int(value)
        except ValueError:
            value = int(si_prefix(value))

        items_id = list(shopi.keys())
        if id in items_id:
            if id == 'pick':
                if inv[user][0][0] == False:
                    await ctx.channel.send('You already have a pickaxe, you may not by another one.')
                else:
                    inv[user][0][0] = False
                    setcoins(user, getcoins(user)[0]+10000)
                    await ctx.channel.send('You sold a pickaxe for **10,000** coins.')
            else:
                if inv[user][shopi[id][4]] < value:
                    await ctx.channel.send(f'You do not have {value:,} of {shopi[id][2]}, you only have {inv[user][shopi[id][4]]}')
                else:
                    await ctx.channel.send(f'You sold `{value:,}` {shopi[id][1]} `{shopi[id][2]}` for `{shopi[id][0]}`s for `{shopi[id][0]*value:,}` coins.')
                    setcoins(user, getcoins(user)[0]+shopi[id][0]*value)
                    inv[user][shopi[id][4]] -= value
        else:
            await ctx.channel.send('Either that item doesn\'t exsist or it is not sellable.')



    @commands.command(name='use', description='use your items', usage='use <item> [amount]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def usecommand(self, ctx, id: str = '', amount: int = 1):

        user = ctx.author.id

        try:
            amount = int(amount)
        except ValueError:
            amount = int(si_prefix(amount))

        items_id = list(shopi.keys())
        if id in items_id:
            if id == 'apple':
                if inv[user][1] == 0:
                    await ctx.channel.send("You don't own this item!")
                else:
                    inv[user][1] -= 1
                    applea = random.randint(1,2)
                    if applea == 1:
                        await ctx.channel.send('You ate your apple and nothing happend.')
                    else:
                        applec = random.randint(100,200)
                        await ctx.channel.send(f"You ate an apple and got lucky and found {applec} coins on the ground.")
                        setcoins(user, coin1=getcoins(user)[0]+applec) 
            if id == 'coke':
                if inv[user][2] == 0:
                    await ctx.send("You don't own this item!")
                else:
                    inv[user][2] -= 1
                    cokee = random.randint(1,2)
                    if cokee == 1:
                        cokec = random.randint(20,30)
                        await ctx.channel.send(f'You shared coke with your friends, they gave you {cokec} coins for it.')
                        setcoins(user, coin1=getcoins(user)[0]+cokec)
                    else:
                        await ctx.channel.send('You drank some coke.')
            if id == 'lucky':
                if inv[user][3] == 0:
                    await ctx.send("You don't own this item!")
                elif amount > inv[user][3]:
                    await ctx.channel.send(f'You do not have {amount:,} of Lucky Blocks, you only own {inv[user][3]:,}')
                else:
                    pagenum = math.ceil(amount/43)
                    inv[user][3] -= amount
                    ln = 1
                    totalapple = 0
                    totalcoke = 0
                    totalcoins = 0
                    luckylist = []
                    while amount > 0:
                        blockd = random.randint(1,100)
                        if blockd >= 57:
                            coinsd = random.randint(1000, 5000)
                            sendm = f'You got {coinsd} coins'
                            totalcoins += coinsd
                            setcoins(user, coin1=getcoins(user)[0]+coinsd)
                            appled = random.randint(0,5)
                            if appled > 0:
                                sendm = sendm + f', {appled} :apple: `apple`s'
                                totalapple += appled
                                inv[user][1] += appled
                            coked = random.randint(0,10)
                            if coked > 0:
                                sendm = sendm + f', {coked} <:coke:730879358805344357> `coke`s'
                                totalcoke += coked
                                inv[user][2] += coked
                        else:
                            losed = random.randint(100,500)
                            sendm = f'A TNT popped out of yout lucky block. Your wallet has a hole in it, {losed} coins dropped out of it.'
                            setcoins(user, coin1=getcoins(user)[0]-losed)
                            totalcoins -= losed
                        luckylist.append(sendm)
                        ln += 1
                        amount -= 1
                    
                    page = 1
                    intera = True

                    if pagenum == 1:
                        luckyb = discord.Embed(title=f'{ctx.author.name}\'s Lucky Block Output', description='\n\n'.join(luckylist), color=random.randint(0, 16777215))
                        luckyb.set_footer(text=f'Page {page} of {pagenum}',icon_url='')
                        luckyb.add_field(name='Total Output', value=f'You got a total of {totalcoins:,} coins, {totalapple:,} :apple: `apple(s)`, and {totalcoke:,} <:coke:730879358805344357> `coke(s)` from the Lucky Blocks.')
                        return await ctx.send(embed=luckyb)

                    ds = {'FP': True, 'P': True, 'N': False, 'LP': False}

                    sendme = []

                    if amount < 43:
                        amountv = amount + 1
                    else:
                        amountv = 43  

                    col = random.randint(0, 16777215)

                    for i in range(1, amountv):
                        sendme.append(luckylist[i-1])
                    sendme = "\n\n".join(sendme)
                    luckyb = discord.Embed(title=f'{ctx.author.name}\'s Lucky Block Output', description=sendme, color=col)
                    luckyb.set_footer(text=f'Page {page} of {pagenum}',icon_url='')
                    luckyb.add_field(name='Total Output', value=f'You got a total of {totalcoins:,} coins, {totalapple:,} :apple: `apple(s)`, and {totalcoke:,} <:coke:730879358805344357> `coke(s)` from the Lucky Blocks.')
                    intme = await ctx.send(embed=luckyb, components=[[Button(style=ButtonStyle.green, label='First Page', disabled=ds['FP']), Button(style=ButtonStyle.green, label='←', disabled=ds['P']), Button(style=ButtonStyle.green, label='→', disabled=ds['N']), Button(style=ButtonStyle.green, label='Last Page', disabled=ds['LP']), Button(style=ButtonStyle.red, label='End Interaction')]])

                    while intera == True:
                        lownum = math.floor((page * 43) - 43)
                        if page == pagenum:
                            maxnum = amount
                        elif page == 1:
                            maxnum = 43
                        else:
                            maxnum = math.floor((page * 43))
                        sendme = []
                        for i in range(lownum, maxnum+1):
                            sendme.append(luckylist[i-1])
                        sendme = "\n\n".join(sendme)
                        luckyb = discord.Embed(title=f'{ctx.author.name}\'s Lucky Block Output', description=sendme, color=col)
                        luckyb.set_footer(text=f'Page {page} of {pagenum}',icon_url='')
                        luckyb.add_field(name='Total Output', value=f'You got a total of {totalcoins:,} coins, {totalapple:,} :apple: `apple(s)`, and {totalcoke:,} <:coke:730879358805344357> `coke(s)` from the Lucky Blocks.')
                        await intme.edit(embed=luckyb, components=[[Button(style=ButtonStyle.green, label='First Page', disabled=ds['FP']), Button(style=ButtonStyle.green, label='←', disabled=ds['P']), Button(style=ButtonStyle.green, label='→', disabled=ds['N']), Button(style=ButtonStyle.green, label='Last Page', disabled=ds['LP']), Button(style=ButtonStyle.red, label='End Interaction')]])

                        try:
                            bute = await self.client.wait_for("button_click", timeout = 30.0, check = lambda bute: bute.author == ctx.author)
                        except asyncio.TimeoutError:
                            return await intme.edit(components=[[Button(style=ButtonStyle.green, label='First Page', disabled=True), Button(style=ButtonStyle.green, label='←', disabled=True), Button(style=ButtonStyle.green, label='→', disabled=True), Button(style=ButtonStyle.green, label='Last Page', disabled=True), Button(style=ButtonStyle.red, label='End Interaction', disabled=True)]])

                        await bute.respond(type=6)

                        if bute.component.label.startswith("First Page"):
                            page = 1
                            ds['N'] = False
                            ds['LP'] = False
                            ds['FP'] = True
                            ds['P'] = True
                        elif bute.component.label.startswith("←"):
                            if page != 1:
                                page -= 1
                                ds['N'] = False
                                ds['LP'] = False
                                if page == 1:
                                    ds['FP'] = True
                                    ds['P'] = True
                                else:
                                    ds['FP'] = False
                                    ds['P'] = False
                        elif bute.component.label.startswith("→"):
                            if page != pagenum:
                                page += 1
                                ds['FP'] = False
                                ds['P'] = False
                                if page == pagenum:
                                    ds['N'] = True
                                    ds['LP'] = True
                                else:
                                    ds['N'] = False
                                    ds['LP'] = False
                        elif bute.component.label.startswith("Last Page"):
                            page = pagenum
                            ds['FP'] = False
                            ds['P'] = False
                            ds['N'] = True
                            ds['LP'] = True
                        elif bute.component.label.startswith("End Interaction"):
                            await intme.edit(embed=luckyb, components=[[Button(style=ButtonStyle.green, label='First Page', disabled=True), Button(style=ButtonStyle.green, label='←', disabled=True), Button(style=ButtonStyle.green, label='→', disabled=True), Button(style=ButtonStyle.green, label='Last Page', disabled=True), Button(style=ButtonStyle.red, label='End Interaction', disabled=True)]])
                            intera = False

        else:
            await ctx.channel.send("What are you talking about, that isn't even an item.")


    @commands.command(name='gift', description='give other people your stuff', usage='gift <user> <item> [amount]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def giftcommand(self, ctx, user: discord.User, item, amount: str= '1'):
        target = user.id
        amount = int(si_prefix(amount))
        if target == ctx.author.id:
            return await ctx.channel.send('You cannot share stuff with yourself.')
        if amount > inv[user][shopi[item][4]]:
            await ctx.channel.send(f'You do not have that many {inv[user][shopi[item][4]]}(s).')
        elif amount < 0:
            await ctx.channel.send('ARE YOU TRYING TO HJACK THE SYSTEM?')
        else:
            inv[user][shopi[item][4]] -= amount
            inv[target][shopi[item][4]] += amount
            await ctx.channel.send(f"You gave **{amount}** {shopi[item][2]}(s) to **{self.client.get_user(target)}**.")





'''
███████ ██    ██ ███    ██ 
██      ██    ██ ████   ██ 
█████   ██    ██ ██ ██  ██ 
██      ██    ██ ██  ██ ██ 
██       ██████  ██   ████ 
'''



class fun_commands(commands.Cog, name='fun'):

    def __init__(self, client):
        self.client = client


    @commands.command(name='8ball', aliases=['magic8ball'], description='hmmmmmm', usage='8ball <quetion>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def magic8ball(self, ctx, *, question):
        if question[-1] != '?':
            await ctx.channel.send('Ask me a qustion.\n\nQuestions must contain `?`')
        elif len(question) <= 5:
            await ctx.channel.send('Kinda sus, that\'s too short for a question.')
        else:
            ballmsg = ["Try asking again later.",
                "Not sure.",
                "Think harder.",
                "Yes!",
                "Maybe.",
                "Absolutely Not.",
                "My source say no.",
                "Most likely!",
                "Very doubtful.",
                "Don't count on it.",
                "It is certain.",
                "As I see it, yes.",
                "Outlook not so good.",
                "My reply is no.",
                "Better not tell you now.",
                "Signs point to yes.",
                "You may relay on it."]
            await ctx.reply(content=f"\U0001f3b1 **Question:** `{question}` \U0001f3b1\n\n**8ball:** {random.choice(ballmsg)}", mention_author=userconfig[ctx.author.id][0])


    @commands.command(name='annoy', description='annoy your friends, but don\'t use it too much', usage='annoy <user> <amount> <message>')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def annoy(self, ctx, user: discord.User, num: int = 20, *, msg='TRIGGERED'):
        if num > 100:
            return await ctx.channl.send('Either you really hate them, or you want me to ban you.\n\nYour number cannot be greater than 100.')
        if len(msg) > 500:
            return await ctx.channel.send('Shortern your message, it has to be less than 500 characters.')
        if user == self.client.user:
            await ctx.channel.send("You can't annoy me dumbo. ~~You already did that too many times.~~") 
            return
        elif user.bot:
            await ctx.channel.send('You already annoyed the bots by using **2,147,483,647** commands.')
        else:
            await ctx.channel.send(f'Triggering annoyance.\nTarget: {user}')
            while num > 0: 
                await user.send(f'**{msg}**\nare you annoyed yet?\ntriggered by ||{ctx.author.name}||')
                num -= 1


    @commands.command(name='backwards', aliases=['bw'], description='sdrawkcab ti yas lliw I dna gnihtemos em llet uoY', usage='backwards <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def backwards(self, ctx, *, msg):
        if msg == '':
            return await ctx.channel.send('What message do you want me to send backwards?')
        nonc = ['<', '>']
        for i in nonc:
            if i in msg:
                return await ctx.channel.send(f'I may not reverse a message with a custom emoji or mention.\nBlacklisted characters `{nonc}`')
        await ctx.channel.send(msg[::-1])


    @commands.command(name='colortext', aliases=['ctext'], description='colored text', usage='colortext <color> <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def colortext(self, ctx, color, *, msg):
        if len(msg) > 1000:
            return await ctx.channel.send('Max character count is 1,000 characters.')
        msg = 'Sorry mobile users, this feature only works for desktop users.'
        if color == 'yellow':
            await ctx.channel.send(f'{msg}```fix\n{messagee}\n```')
        elif color == 'red':
            messagee = '\n- '.join(msg.split('\n'))
            await ctx.channel.send(f'{msg}```diff\n- {messagee}\n```')
        elif color == 'orange':
            messagee = '\n# '.join(msg.split('\n'))
            await ctx.channel.send(f'{msg}```glsl\n# {messagee}\n```')
        elif color == 'green':
            messagee = '\n+ '.join(msg.split('\n'))
            await ctx.channel.send(f'{msg}```diff\n+ {messagee}\n```')
        elif color == 'blue':
            messagee = ' ]\n[ '.join(msg.split('\n'))
            await ctx.channel.send(f'{msg}```ini\n[ {messagee} ]\n```')
        else:
            await ctx.send('You may only choose the `red`, `orange`, `yellow`, `green`, or `blue`.')


    @commands.command(name='impostor', aliases=['imposter', 'sus'], description='This will make it look like the other person is sending the message... kind of', usage='impostor <user> <message>')
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def impostor(self, ctx, user: discord.User, *, msg):
        hooks = await ctx.channel.webhooks()
        hook = utils.get(hooks, name='My Impostor Webhook')
        if hook is None:
            hook = await ctx.channel.create_webhook(name='My Impostor Webhook', avatar=None, reason=None)
        await hook.send(content=msg, username=user.name, avatar_url=user.avatar_url)


    @commands.command(name='joke', description='developer jokes from the pyjokes module', usage='joke')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def joke(self, ctx):
        await ctx.channel.send(embed=discord.Embed(description=f'{pyjokes.get_joke()}', color=random.randint(0, 16777215)))


    @commands.command(name='kill', aliases=['stab'], description='how will they die...', usage='kill <thing>')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def kill(self, ctx, thing):
        klist = [f'**{thing}** has negative IQ.',
            f'**{thing}** died.',
            f'**{thing}** took the wrong pills.',
            f'**{thing}** drank too much water.',
            f'**{thing}** has chinese parents and wanted to buy a game.',
            f'**{thing}** wanted to test if respawing exsited in real life.',
            f'**{thing}** has chinese parents and forgot to do homework.',
            f'**{thing}** lost too many brain cells.',
            f"**{thing}**.exe was ALT+F4'd.",
            f'**{thing}** ate too much.',
            f'**{thing}** fell out of the world.',
            f'**{thing}** drank surphric acid, becuase he thought it was milk.',
            f"**{thing}** got stabbed by Geeson's Stupid Bot.",
            f'**{thing}** got oh noesed.', 
            f'{ctx.author} stabbed **{thing}** in the face.',
            f'{thing} tried to swim in lava.',
            f'{thing} has performed an illegal operation and will be shut down.']
        await ctx.channel.send(random.choice(klist), allowed_mentions=discord.AllowedMentions(everyone=False,users=False, roles=False))


    @commands.command(name='pseudolocalization', aliases=['pseudo'], description='[ƥšêüđøĺøċàĺıźàťıøñ](https://en.wikipedia.org/wiki/Pseudolocalization)', usage='pseudolocalization <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pseudolocalization(self, ctx, *, msg):
        persu = PseudoL10nUtil()
        amountr = len(msg) + 1
        await ctx.channel.send(f'{persu.pseudolocalize(msg)[:amountr]}⟧')


    @commands.command(name='rng', description='random number generator', usage='rng <smallest-number> <biggest-number>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def randomnumbergenerator(self, ctx, num1: int, num2: int):
        if num1 > num2:
            await ctx.channel.send(f'Of course, **{num2}** is 100% bigger than **{num2}**.')
        else:
            number = random.randint(num1, num2)
            await ctx.channel.send(f'{number}')


    @commands.command(name='mock', aliases=['sarcastic'], description='mOcK sOmEoNe', usage='mock <message>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sarc(self, ctx, *, msg):
        await ctx.channel.send(sarcastic(msg))


    @commands.command(name='typing', aliases=['buffer'], description='<a:typing:778776514878636034>', usage='typing [user]')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def typing(self, ctx, user: discord.Member=None):
        if user == None:
            user = ctx.author
        if user.id == 695083835708145734:
            async with ctx.channel.typing():
                await asyncio.sleep(2)
                return await ctx.channel.send(f'<a:typing:778776514878636034> **Geeson\'s Stupid Bot** is typing...')
        await ctx.channel.send(f'<a:typing:778776514878636034> **{user.display_name}** is typing...')


    @commands.command(name='randomstring', aliases=['string'], description='Iz4duKgbYYD6', usage='randomstring <number>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def randomstring(self, ctx, number: int):
        if number > 2000:
            return await ctx.channel.send('The string cannot be longer than 2000 characters.')
        strings = []
        while number > 0:
            strings.append(random.choice(''.join(string.ascii_letters + string.digits)))
            number -= 1
            strings2 = ''.join(strings)
        await ctx.channel.send(strings2)




'''
 ██████   █████  ███    ███ ███████ ███████ 
██       ██   ██ ████  ████ ██      ██      
██   ███ ███████ ██ ████ ██ █████   ███████ 
██    ██ ██   ██ ██  ██  ██ ██           ██ 
 ██████  ██   ██ ██      ██ ███████ ███████ 
'''


class game_commands(commands.Cog, name='games'):

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
        #clue = dictionary.meaning(joinanswer)
        #msg = await ctx.channel.send(f'Time to play hangman:\n**CLUE**:{clue}\n{joindisplay}')
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
                return await msg2.edit(content=f'** **\n    ___\n   |   O\n   | \ | /\n   |   /\ \n   |\n   |\n-----\n**YOU LOSE, The word is `{joinanswer}`**')
            try:
                msg3 = await self.client.wait_for('message', timeout=30, check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)
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
                            #await msg3.add_reaction('\u2705')
                usedcharacters.append(guess)
                if str(guess) not in joinanswer:
                    deaths += 1
                    #await msg3.add_reaction('\u274c')
                    if str(guess) not in charactersn:
                        charactersn.append(guess)
                joindisplay = ' '.join(display)
                charactersjoin = ' '.join(charactersn)
                #await msg.edit(content=f'Time to play hangman:\n**CLUE**:{clue}\nInvaild Characters: {charactersjoin}\n{joindisplay}')
                await msg.edit(content=f'Time to play hangman:\nInvaild Characters: {charactersjoin}\n{joindisplay}')
        await ctx.channel.send(f'🥳 **GG, the word was `{joinanswer}`** 🥳')



'''
██ ███    ███  █████   ██████  ███████ 
██ ████  ████ ██   ██ ██       ██      
██ ██ ████ ██ ███████ ██   ███ █████   
██ ██  ██  ██ ██   ██ ██    ██ ██      
██ ██      ██ ██   ██  ██████  ███████
'''



class image_commands(commands.Cog, name='image'):

    def __init__(self, client):
        self.client = client


    @commands.command(name='ascii', description='ascii art', usage='ascii <text|image|random> <text-or-image>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ascii(self, ctx, arg0, *, arg1):
        asciit = art.text2art(arg1, font='random')
        try:
            with open('._ascii.temp.txt', 'w+') as f:
                f.write(asciit)
            #await message.channel.send(f'**NOTE:** Too much character may result in poor formatting.\n```{asciit}```', file=discord.File('._ascii.temp.txt'))
            await ctx.channel.send(file=discord.File('._ascii.temp.txt'))
            os.remove('._ascii.temp.txt')
        except discord.HTTPException:
            await ctx.channel.send('This message is too long to convert to ascii.')
        if arg0.lower() == 'image' or arg0.lower() == 'i':
            await ctx.channel.send('Currently Unspported.')
        elif arg0.lower() == 'random' or arg0.lower() == 'r':
            asciit = art.art("random")
            await ctx.channel.send(f"`{asciit}`")
        else:
            await ctx.channel.send('The correct usage is `ascii <text|image> <text-or-image>`.')


    @commands.command(name='clippy', aliases=['paperclip'], description='It looks like your writing a letter, would you like some help?', usage='clippy <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def clippy(self, ctx, *, msg):
        image = Image.open('assests/clippy.png')
        draw = ImageDraw.Draw(image)
        if platform.system() == 'Windows':
            font = ImageFont.truetype("C:\\Users\\wang1\\AppData\\Local\\Microsoft\\Windows\\Fonts\\FreeMono.ttf", 20)
        elif platform.system() == 'Linux':
            font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 20)
        text2 = bend(30, msg)
        draw.text((51, 34),f"{text2}",(0,0,0),font=font)
        image.save('sample-out-clippy.PNG')
        await ctx.channel.send(file=discord.File('sample-out-clippy.PNG'))
        os.remove('sample-out-clippy.PNG')


    @commands.command(name='ohnoes', description='Oh noes', usage='ohnoes <message>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ohnoes(ctx, *, msg):
        image = Image.open('assests/ohnoes.png')
        draw = ImageDraw.Draw(image)
        if platform.system() == 'Windows':
            font = ImageFont.truetype("C:\\Users\\wang1\\AppData\\Local\\Microsoft\\Windows\\Fonts\\FreeMono.ttf", 15)
        elif platform.system() == 'Linux':
            font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 15)
        text2 = bend(33, msg)
        draw.text((172, 66),f"{text2}",(0,0,0),font=font)
        image.save('sample-out.PNG')
        await ctx.channel.send(file=discord.File('sample-out.PNG'))
        os.remove('sample-out.PNG')



'''
███    ███  ██████  ██████  ███████ ██████   █████  ████████ ██  ██████  ███    ██ 
████  ████ ██    ██ ██   ██ ██      ██   ██ ██   ██    ██    ██ ██    ██ ████   ██ 
██ ████ ██ ██    ██ ██   ██ █████   ██████  ███████    ██    ██ ██    ██ ██ ██  ██ 
██  ██  ██ ██    ██ ██   ██ ██      ██   ██ ██   ██    ██    ██ ██    ██ ██  ██ ██ 
██      ██  ██████  ██████  ███████ ██   ██ ██   ██    ██    ██  ██████  ██   ████
'''



class moderation_commands(commands.Cog, name='moderation'):

    def __init__(self, client):
        self.client = client


    @commands.command(name='prefix', description='change the prefix for the server', usage='prefix [prefix]')
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx, *, msg=''):
        bl = {'** **': '`** **`', '`': '"`"', '\n': 'an enter'}
        if sys.getsizeof(msg) > 3000:
            return await ctx.send('You may not have a prefix longer than 3000 bytes.')
        for i in msg:
            if i not in string.printable:
                return await ctx.send('You may only have printable characters as a prefix.')
        for i in bl.keys():
            if i in msg.lower():
                return await ctx.send(f'Choose a different prefix, it may not contain {bl[i]}.')
        if msg.lower() == 'reset' or msg == '' or msg.lower() == 'bot':
            config[ctx.guild.id][4] = ''
            return await ctx.channel.send(f'Reset the prefix to `bot`.')
        if msg[-1] not in string.punctuation and msg[-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            msg = msg+' '
        config[ctx.guild.id][4] = msg
        await ctx.channel.send(f'Sucessfully set the prefix to `{msg}`.\n\nIf your prefix ends with a symbol or number, you do not have the add a space between the prefix and the command.')


    @commands.command(name='kick', description='kick users', usage='kick <user> [reason]')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=''):
        if user == self.client.user:
            return await ctx.channel.send("You can't kick me with my own command you know.")
        if user == ctx.guild.owner:
            return await ctx.channel.send('Thats the owner you dumbo.')
        if user == ctx.author:
            return await ctx.channel.send('Do you want me to kick you or no?')
        await ctx.guild.kick(user, reason=reason)
        await ctx.channel.send(f'Sucessfully kicked **{user}**.')
        await user.send(f'You got kicked from **{ctx.guild.name}** by: {ctx.author}, reason: {reason}')


    @commands.command(name='ban', description='ban users', usage='ban <user> [reason]')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User, *, reason=''):
        if user == self.client.user:
            return await ctx.channel.send("You can't ban me with my own command you know.")
        if user == ctx.guild.owner:
            return await ctx.channel.send('Thats the owner you dumbo.')
        if user == ctx.author:
            return await ctx.channel.send('Do you want me to ban you or no?')
        await ctx.guild.ban(user, reason=reason)
        await ctx.channel.send(f'Sucessfully banned **{user}**.')
        await user.send(f'You got banned from **{ctx.guild.name}** by: {ctx.author}, reason: {reason}')

    @commands.command(name='purge', aliases=['delete'], description='delete multipul messages at once', usage='purge [amount]')
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def purge(self, ctx, amount: int = 2):
        if amount <= 1:
            return await ctx.channel.send('You must at least delete 2 messages.')
        await ctx.channel.purge(limit=amount+1)
        msgpr = await ctx.channel.send(f'Sucessfully purged **{amount}** messages.')
        await asyncio.sleep(1)
        await msgpr.delete()

    @commands.command(name='antidelete', description='make users unable to delete messages', usage='antidelete')
    async def antideletee(self, ctx):
        if int(ctx.channel.id) not in antidelete:
            if ctx.author.permissions_in(ctx.channel).administrator or ctx.author.permissions_in(ctx.channel).manage_channels or int(ctx.author.id) in admin:
                antidelete.append(ctx.channel.id)
                await ctx.channel.send('Turned on antidelete for this channel.')
            else:
                await ctx.channel.send('You do not have permission to enable or disable antidelete. (manage_channels)')
        else:
            if ctx.author.permissions_in(ctx.channel).administrator or ctx.author.permissions_in(ctx.channel).manage_channels or int(ctx.author.id) in admin:
                antidelete.pop(antidelete.index(ctx.channel.id))
                await ctx.channel.send('Turned off antidelete for this channel.')
            else:
                await ctx.channel.send('You do not have permission to enable or disable antidelete. (manage_channels)')


    @commands.command(name='slowmode', aliases=['sm'], description='set custom slowmodes', usage='slowmode <time>')
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def slowmodee(self, ctx, slowmode: int = 0):
        if slowmode < 0:
            await ctx.channel.send("Your slowmode can't be a negative number")
        if slowmode > 21600:
            await ctx.channel.send(f'Your int ({slowmode}) cannot be larger than **21600**.')
        await self.client.get_channel(ctx.channel.id).edit(reason='custom slowmode', slowmode_delay=int(slowmode))
        await ctx.channel.send(f'Set slowmode of <#{ctx.channel.id}> to **{slowmode}** seconds.')


    @commands.command(name='giveaway', description='create a giveaway', usage='giveaway')
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def giveawaycommand(self, ctx):
        
        try:
            await ctx.channel.send('What do you want to giveaway? (type `cancel` to cancel)')
            msg = await self.client.wait_for('message', timeout=30, check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)
        except asyncio.TimeoutError:
            await ctx.channel.send('Timed out. Giveaway cancelled.')
        else:
            if msg.content.lower() == 'cancel':
                return await ctx.channel.send('Giveaway cancled.')
            try:
                await ctx.channel.send(f'OK, a giveaway for **{msg.content}**\nHow many winners?')
                msg2 = await self.client.wait_for('message', timeout=30, check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)
            except asyncio.TimeoutError:
                await ctx.channel.send('Timed out. Giveaway cancelled.')
            else:
                try:
                    winners = int(msg2.content)
                except ValueError:
                    await ctx.channel.send('That is not a number.')
                else:
                    if winners <= 0:
                        return await ctx.channel.send(f'You can\'t have **{winners}** winners')
                    try:
                        await ctx.channel.send(f'OK, **{winners}** winners\nHow long? E.g. `1m 1s` or `61` please add a space bewteen. ')
                        msg3 = await self.client.wait_for('message', timeout=30, check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)
                    except asyncio.TimeoutError: 
                        await ctx.channel.send('Timed out. Giveaway cancelled.')
                    else:
                        lasts = 0
                        try:
                            lasts = int(msg3.content)
                        except ValueError:
                            try:
                                liste = msg3.content.split(' ')
                                for i in liste:
                                    lasts += tts(i)
                            except ValueError:
                                return await ctx.channel.send('That is not a number.')
                        if lasts < 60:
                            await ctx.channel.send('Your giveaway cannot be shorter than 1 minute.') 
                        elif lasts > 2592000:
                            await ctx.channel.send('Your giveaway cannot be longer than 1 month.') 
                        else:
                            try:
                                await ctx.channel.send(f'OK, a giveaway for **{lasts} seconds**\nWhich Channel? (No ids)')
                                msg4 = await self.client.wait_for('message', timeout=30, check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)
                            except asyncio.TimeoutError: 
                                await ctx.channel.send('Timed out. Giveaway cancelled.')
                            else:   
                                #channele = msg4.content[2:-1]
                                #if channele[0] == '#':
                                    #channele = channele[1:]
                                #channele = int(channele)
                                channele = discord.Channel(msg4.content)
                                await ctx.channel.send(f'Giveaway created in **#{self.client.get_channel(channele)}.**')
                                if len(gw2[ctx.guild.id]) == 0:
                                    idd = 0
                                else:
                                    idd = len(gw2[ctx.guild.id])
                                utcc = datetime.datetime.utcnow()+datetime.timedelta(seconds = lasts)
                                channel = self.client.get_channel(channele)
                                embed = discord.Embed(title=f'{msg.content}',description=f'React With a 🎁 To Join!\nGiveaway Created By: {ctx.author.mention}\nGiveaway ID: {idd}',color=random.randint(0, 16777215))
                                embed.add_field(name='TIME:', value=f'{lasts} seconds')
                                embed.add_field(name='WINNERS:', value=f'{winners} winner(s)')
                                embed.add_field(name=f'Ends at:',value=f'<t:{int(time.time()+lasts)}:F>')
                                embed.add_field(name=f'Ends in:',value=f'<t:{int(time.time()+lasts)}:R>')
                                msg4 = await channel.send(embed=embed)
                                await msg4.add_reaction('🎁')
                                lasts2 = int(time.time() + lasts)
                                gw2[ctx.guild.id][idd] = [ctx.author.id, lasts2, winners, channele, msg4.id, idd, utcc, msg.content, False, lasts]




'''
 █████  ██████   ██████ ██   ██ ██ ██    ██ ███████ 
██   ██ ██   ██ ██      ██   ██ ██ ██    ██ ██      
███████ ██████  ██      ███████ ██ ██    ██ █████   
██   ██ ██   ██ ██      ██   ██ ██  ██  ██  ██      
██   ██ ██   ██  ██████ ██   ██ ██   ████   ███████ 
'''



class archived_commands(commands.Cog, name='archive'):

    def __init__(self, client):
        self.client = client


    @commands.command(name='hello', aliases=['hi'], description='hello', usage='hello')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def hello(self, ctx):
        await ctx.send('Hello stupid.')


    @commands.command(name='mystupidity', aliases=['howstupidami'], description='see how stupid you are', usage='mystupidity')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def mystupidity(self, ctx):
        await ctx.send(f'{ctx.author.mention}, You are the stupidest person I\'ve ever seen.')


    @commands.command(name='nitro', aliases=['dn', 'discordnitro'], description='a fake picture of discord nitro', usage='nitro')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def nitro(self, ctx):
        await ctx.channel.send(file=discord.File('Discord_Nitro_TROLL.png'))


    @commands.command(name='yesorno', description='yes or no?', usage='yesorno')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def yesorno(self, ctx, orr='', no=''):
        if orr == 'or' and no == 'no':
            try:
                await ctx.channel.send('yes or no anwser me (type yes or no in chat)')
                mesg = await self.client.wait_for('message', timeout=10, check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)
            except asyncio.TimeoutError:
                return     
            else:
                if mesg.content == 'yes' or mesg.content == 'no':
                    await ctx.channel.send("That's not one of the choices.")
                if mesg.content == 'yes or no in chat)':
                    await ctx.channel.send('YOUR IQ = 2,147,483,647')







'''
██╗░░░░░░█████╗░░█████╗░██████╗░░██████╗
██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░░░░██║░░██║██║░░██║██████╔╝╚█████╗░
██║░░░░░██║░░██║██║░░██║██╔═══╝░░╚═══██╗
███████╗╚█████╔╝╚█████╔╝██║░░░░░██████╔╝
╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═════╝░
'''



@tasks.loop(hours=24.0)
async def debt_increase():
    for user in coins.keys():
        setdebt(user, debtt=math.ceil(1.5*getdebt(user)[0]))
        


@tasks.loop(minutes=5.0)
async def checkday():
    for user in coins.keys():
        if (user in debt) and debt[user][1] > time.time():
            setdebt(user, debtt=0, debtday=0)
            setcoins(user, coin2=getcoins(user)[1]-getdebt(user)[0])



@tasks.loop(seconds=5.0)
async def giveawaye():
    for i in gw2.keys():
        if len(gw2[i]) == 0:
            pass
        else:
            for j in gw2[i].keys():
                if gw2[i][j][1] <= time.time() and gw2[i][j][8] == False:
                    gw2[i][j][8] = True
                    msg = await client.get_channel(gw2[i][j][3]).fetch_message(gw2[i][j][4])
                    usersreacted = await msg.reactions[0].users().flatten()
                    usersreacted.pop(usersreacted.index(client.user))
                    winnerlist = []
                    winners = gw2[i][j][2]
                    if len(usersreacted) == 0:
                        embed = discord.Embed(title=f'{gw2[i][j][7]}',description=f'Giveaway Created By: <@!{gw2[i][j][0]}>\nGiveaway ID: {gw2[i][j][5]}',color=random.randint(0, 16777215))
                        embed.add_field(name='TIME:', value=f'{gw2[i][j][9]} seconds')
                        embed.add_field(name='WINNERS:', value=f'None')
                        embed.add_field(name=f'Ends at:',value=f'<t:{lasts2}:F>')
                        embed.add_field(name=f'Ends in:',value=f'<t:{lasts2}:R>')
                        await msg.edit(content='**Giveaway Ended.**', embed=embed)
                        return await channel.send(f'RIP. No one entered the giveaway. ID: {gw2[i][j][5]}')
                    while winners > 0:
                        if len(usersreacted) == 0:
                            break
                        else:
                            winner = random.choice(usersreacted)
                            winnerlist.append(winner)
                            usersreacted.pop(usersreacted.index(winner))
                            winners -= 1
                    winlist2 = []
                    for user in winnerlist:
                        winlist2.append(user.mention)
                        winlist2.append(',')
                        winlist3 = ''.join(winlist2)
                    embed = discord.Embed(title=f'{gw2[i][j][7]}',description=f'Giveaway Created By: <@!{gw2[i][j][0]}>\nGiveaway ID: {gw2[i][j][5]}',color=random.randint(0, 16777215))
                    embed.add_field(name='TIME:', value=f'{gw2[i][j][9]} seconds')
                    embed.add_field(name='WINNERS:', value=f'{winlist3}')
                    embed.add_field(name=f'Ends at:',value=f'<t:{lasts2}:F>')
                    embed.add_field(name=f'Ends in:',value=f'<t:{lasts2}:R>')
                    await msg.edit(content='**Giveaway Ended.**', embed=embed)
                    await client.get_channel(gw2[i][j][3]).send(f'Congrats to **{winlist3}** they won **{gw2[i][j][7]}**. ID: {gw2[i][j][5]}')
                    for user in winnerlist:
                        embed = discord.Embed(title=f'{gw2[i][j][7]}',description=f'Giveaway Created By: <@!{gw2[i][j][0]}>\nGiveaway ID: {gw2[i][j][5]}',color=random.randint(0, 16777215))
                        embed.add_field(name='TIME:', value=f'{gw2[i][j][9]} seconds')
                        embed.add_field(name='WINNERS:', value=f'{winlist3}')
                        embed.add_field(name=f'Ends at:',value=f'<t:{lasts2}:F>')
                        embed.add_field(name=f'Ends in:',value=f'<t:{lasts2}:R>')
                        await user.send(content='You won a giveaway!!!', embed=embed)



@tasks.loop(minutes=1.0)
async def workreset():
    for user in coins.keys():
        if datetime.datetime.utcnow().time().hour == 23 and datetime.datetime.utcnow().time().minute == 56:
            if getjob(user)[0] > 0:
                if getjob(user)[0] == 1:
                    timesn = 1
                elif getjob(user)[0] == 2:
                    timesn = 5
                elif getjob(user)[0] == 3:
                    timesn = 8
                elif getjob(user)[0] == 4:
                    timesn = 4
                elif getjob(user)[0] == 6:
                    timesn = 6
                if getjob(user)[1] < timesn:
                    setjob(user, new_job=0,times=0)
                    usersend = client.get_user(user)
                    await usersend.send(f'You have been fired from your job. Wait **23 hours 56 minutes and 04 seconds** to apply for a new job.')
                    quit[user] = time.time() + 86164
                else:
                    setjob(user, times=0)



@tasks.loop(minutes=10.0)
async def save():
    save_all()




async def run_bot():
    await client.start(Token)



#workreset.start()
checkday.start()
debt_increase.start()
save.start()
asyncio.get_event_loop().run_until_complete(run_bot())