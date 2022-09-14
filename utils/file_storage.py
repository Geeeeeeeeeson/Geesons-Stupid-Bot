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
