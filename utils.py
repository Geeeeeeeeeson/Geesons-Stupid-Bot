"""Utilities"""

import time

import file_storage


def help_categories(ls: list):
    """Add code block to a list"""
    if not ls:
        return None
    val_string = '`, `'.join(ls)
    val_string = f'`{val_string}`'
    return val_string


def bend(w: int, s: str):
    """New Line after certain amount of characters"""
    s = s.split(' ')
    ls = filter(None, s)
    new = []
    i = 0
    for word in ls:
        line = new[i] + ' ' + word
        if not new[i]:
            line = word
        if len(word) > w:
            while len(word) > w:
                new.append(word[:w])
                i += 1
                word = word[w:]
            i += 1
            new.append(word)
        elif len(line) > w:
            new.append(word)
            i += 1
        else:
            new[i] = line
    return '\n'.join(new)


def add_xp(user_id: int, xp: int, cooldown: bool = True):
    """Add xp to user"""
    user = file_storage.user_data[user_id]
    user['xp'] += xp
    user['xp_cooldown'] = time.time() if cooldown else user['xp_cooldown']
    if user['xp'] >= user['next_level']:
        user['xp'] -= user['next_level']
        user['level'] += 1
        user['next_level'] = int((100 * (user['level'] ** 2)) / 2)
