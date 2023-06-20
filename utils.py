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


def bend(text: str, count: int):
    """New Line after certain amount of characters"""
    if len(text) <= count:
        return text

    text_list = filter(None, text.split(' '))
    output = []
    line = 0
    for word in text_list:
        if len(output) == line:
            output.append(word)
        elif len(output[line]) + len(word) > count:
            line += 1
            output.append(word)
        else:
            output[line] += ' ' + word
    for i, j in enumerate(output):
        if len(j) > count:
            output[i] = j[:count]
            if i + 1 < len(output):
                output[i + 1] = j[count:] + output[i + 1]
            else:
                output.append(j[count:])
    return '\n'.join(output)


def add_xp(user_id: int, xp: int, cooldown: bool = True):
    """Add xp to user"""
    user = file_storage.user_data[user_id]
    user['xp'] += xp
    user['xp_cooldown'] = time.time() if cooldown else user['xp_cooldown']
    while user['xp'] >= user['next_level']:
        user['xp'] -= user['next_level']
        user['level'] += 1
        user['next_level'] = int((100 * (user['level'] ** 2)) / 2)
