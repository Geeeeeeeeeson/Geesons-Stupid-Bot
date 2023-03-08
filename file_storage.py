"""File loading and saving"""

import ast

with open('./data/guild_data', 'r') as f:
    guild_data = ast.literal_eval(f.read())

with open('./data/user_data', 'r') as f:
    user_data = ast.literal_eval(f.read())


def save_all():
    with open('./data/guild_data', 'w') as f:
        f.write(repr(guild_data))
    with open('./data/user_data', 'w') as f:
        f.write(repr(user_data))


def guild_update_with_defaults(guild_id: int):
    if guild_id not in guild_data: ## initialize guild data
        guild_data[guild_id] = {'prefix': 'bot ',
                                'antidelete': [],
                                'log': []}
    ## allows for new keys to be added without breaking the bot
    if 'prefix' not in guild_data[guild_id]:
        guild_data[guild_id]['prefix'] = 'bot '
    if 'antidelete' not in guild_data[guild_id]:
        guild_data[guild_id]['antidelete'] = []
    if 'log' not in guild_data[guild_id]:
        guild_data[guild_id]['log'] = []


def user_update_with_defaults(user_id: int):
    if user_id not in user_data: ## initialize user data
        user_data[user_id] = {'economy':
                                      {'money':
                                           {'wallet': 0,
                                            'bank': 0,
                                            'level': 1, },
                                       'job':
                                           {'id': -1,
                                            'salary': 0,
                                            'last_worked': -1,
                                            'quit_time': -1, },
                                       'login': {'daily': -1,
                                                 'weekly': -1, },
                                       'inventory': {},
                                       },
                                  'xp': 0,
                                  'badge': [],
                                  'is_banned': False,
                                  'is_admin': False, }
    ## allows for new keys to be added without breaking the bot
    if 'xp' not in user_data[user_id]:
        user_data[user_id]['xp'] = 0
    if 'badge' not in user_data[user_id]:
        user_data[user_id]['badge'] = []
    if 'is_banned' not in user_data[user_id]:
        user_data[user_id]['is_banned'] = False
    if 'is_admin' not in user_data[user_id]:
        user_data[user_id]['is_admin'] = False
