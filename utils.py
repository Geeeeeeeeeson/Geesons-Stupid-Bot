"""Utilities"""


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
