"""File loading and saving"""

import ast


GUILD_DATA = {'prefix': 'bot ',
              'antidelete': [],
              'log': [], }


USER_DATA = {'economy':
                 {'money':
                      {'wallet': 0,
                       'bank': 0,
                       'level': 1,
                       'bank_limit': 5000, },
                  'job':
                      {'id': -1,
                       'salary': 0,
                       'last_worked': -1,
                       'quit_time': -1, },
                  'login': {'daily': -1,
                            'weekly': -1, },
                  'inventory':
                      {'pickaxe': {'has': False, 'level': 1}, }
                  },
             'xp': 0,
             'next_level': 100,
             'level': 1,
             'xp_cooldown': -1,
             'badge': [],
             'is_banned': False,
             'is_admin': False, }


with open('./data/guild_data', 'r') as f:
    guild_data = ast.literal_eval(f.read())

with open('./data/user_data', 'r') as f:
    user_data = ast.literal_eval(f.read())


def save_all():
    with open('./data/guild_data', 'w') as f:
        f.write(repr(guild_data))
    with open('./data/user_data', 'w') as f:
        f.write(repr(user_data))


def _update_with_defaults(data: dict, default: dict):
    for key, value in default.items():
        if isinstance(value, dict):
            if key not in data:
                data[key] = {}
            _update_with_defaults(data[key], value)
        if key not in data:
            data[key] = value


def guild_update_with_defaults(guild_id: int):
    if guild_id not in guild_data:
        guild_data[guild_id] = {}
    _update_with_defaults(guild_data[guild_id], GUILD_DATA)


def user_update_with_defaults(user_id: int):
    if user_id not in user_data:
        user_data[user_id] = {}
    _update_with_defaults(user_data[user_id], USER_DATA)
