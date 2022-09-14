
def help_categories(ls: list):
    if not ls:
        return None
    val_string = '`, `'.join(ls)
    val_string = f'`{val_string}`'
    return val_string
