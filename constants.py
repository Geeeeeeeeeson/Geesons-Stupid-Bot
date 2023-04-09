"""Geeson's Stupid Bot Constants"""

import random

INVITE_LINK = 'https://discord.com/oauth2/authorize?client_id=695083835708145734&permissions=21474836398&scope=bot'

VERSION = '2.0.0-dev4'


class Color:
    bwhite = '\033[1;97m'
    no = '\033[9;91m'
    #
    white = '\033[0;97m'
    yellow = '\033[0;93m'
    green = '\033[0;92m'
    blue = '\033[0;94m'
    cyan = '\033[0;96m'
    red = '\033[0;91m'
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
    end = '\033[0;0m'


def random_color():
    return random.randint(0x00, 0xffffff)

BADGES = {'admin': '<:bot_admin:817935714322612234>',
          'one_year': '<:1Y:817883554150350848>', }

## format {item: {name: str, description: str, price: int, emoji: str, rarity: str, type: str, sellable: bool, sell_price: int, usable: bool}}

INVENTORY = {'pickaxe':
                 {'name': 'Pickaxe', 'description': 'A pickaxe for mining.', 'price': 1200,
                  'emoji': '\u26cf\ufe0f', 'rarity': 'common', 'type': 'tool',
                  'sellable': True, 'sell_price': 100, 'usable': True},
             'apple':
                 {'name': 'Apple', 'description': 'A delicious apple.', 'price': 100,
                  'emoji': '\U0001f34e', 'rarity': 'common', 'type': 'food',
                  'sellable': False, 'sell_price': 0, 'usable': True},}
