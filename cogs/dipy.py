import discord
from discord.ext import commands
import json

# Чтение данных из json файла и добавление в переменную data
with open('json/dipy.json', encoding="utf8") as bot_json:
    data = json.load(bot_json)


class BotCog(commands.Cog):
    """BotCog - команды относящиеся к самому боту"""

    def __init__(self, Dipy):
        self.Dipy = Dipy

    @commands.command(name="инфо")
    async def info(self, ctx):
        """Вывод в чат описание бота"""
        await ctx.send(data["description"])

    @commands.command(name="команды")
    async def commands_list(self, ctx):
        """Вывод в чат списка команд бота"""
        command_list = "```"
        for com in data["commands-list"]:  # сам список берётся из json файла
            command_list = command_list + com + '\n'
        command_list = command_list + "```"
        await ctx.send(command_list)

    @commands.command()
    async def git(self, ctx):
        """Ссылка на репозиторий с исходниками бота"""
        await ctx.send('<@!{}> https://github.com/beaend/Dipy'.format(ctx.author.id))


def setup(Dipy):
    Dipy.add_cog(BotCog(Dipy))
