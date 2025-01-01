import discord
from discord.ext import commands


class DefaultCogName(commands.Cog, name="default_cog_name"):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(DefaultCogName(bot))
