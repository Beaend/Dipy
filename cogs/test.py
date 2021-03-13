import discord
from discord.ext import commands
import json

with open('json/dipy.json', encoding="utf8") as bot_json:
    data = json.load(bot_json)


class TestCog(commands.Cog):
    """TestCog - список базовых задач, которые могут помочь понять основы взаимодействия ботов с командами"""

    def __init__(self, Dipy):
        self.Dipy = Dipy

    @commands.command(name="тест")  # name="что-то" что-то является названием команды которую бот будет обрабатывать
    # создание функции test.
    # Что такое self - вы знаете, если нет - то просто примите, что оно должно тут стоять и глубоко не задумывайтесь.
    async def test(self, ctx):  # ctx - переменная несущая в себе всю информацию связанную с командой.
        """Базовая команда. Бот пишет в чат - Тест"""
        await ctx.send("Тест")  # ctx.send - отправка сообщения в чат из которого была вызвана команда


def setup(Dipy):
    Dipy.add_cog(TestCog(Dipy))
