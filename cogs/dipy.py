import discord
from discord.ext import commands
import json

with open('json/dipy.json', encoding="utf8") as discord_file:
    discord_json = json.load(discord_file)


class BotCog(commands.Cog):
    """BotCog - команды относящиеся к самому боту"""

    def __init__(self, Dipy):
        self.Dipy = Dipy

    @commands.command()
    async def git(self, ctx):
        """Ссылка на репозиторий с исходниками бота"""
        await ctx.send('@{} https://github.com/beaend/Dipy'.format(ctx.author))


def setup(Dipy):
    Dipy.add_cog(BotCog(Dipy))
