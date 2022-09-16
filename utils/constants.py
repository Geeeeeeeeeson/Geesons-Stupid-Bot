import random

INVITE_LINK = 'https://discord.com/oauth2/authorize?client_id=695083835708145734&permissions=21474836398&scope=bot'

VERSION = '2.0.0-dev2'


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
