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
    s = s.split(" ")
    lst = filter(None, s)
    new_lst = [""]
    i = 0
    for word in lst:
        line = new_lst[i] + " " + word
        if new_lst[i] == "":
            line = word
        if len(word) > w:
            while len(word) > w:
                new_lst.append(word[:w])
                i += 1
                word = word[w:]
            i += 1
            new_lst.append(word)
        elif len(line) > w:
            new_lst.append(word)
            i += 1
        else:
            new_lst[i] = line
    return "\n".join(new_lst)
