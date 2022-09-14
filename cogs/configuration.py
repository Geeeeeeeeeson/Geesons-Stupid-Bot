from discord.ext import commands


class configuration(commands.Cog, name='configuration'):

    def __init__(self, client):
        self.client = client


async def setup(client):
    await client.add_cog(configuration(client))