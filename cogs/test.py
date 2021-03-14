import discord
from discord.ext import commands
import json
import random

with open('json/dipy.json', encoding="utf8") as bot_json:
    data = json.load(bot_json)


class TestCog(commands.Cog):
    """TestCog - список базовых задач, которые могут помочь понять основы взаимодействия ботов с командами"""

    def __init__(self, Dipy):
        self.Dipy = Dipy

    # создание функции test.
    @commands.command(name="тест")  # name="что-то" что-то является названием команды которую бот будет обрабатывать
    # !тест - команда для вызова этой функции
    # Что такое self - вы знаете, если нет - то просто примите, что оно должно тут стоять и глубоко не задумывайтесь.
    async def test(self, ctx):  # ctx - переменная несущая в себе всю информацию связанную с командой.
        """Базовая команда. Бот пишет в чат - Тест"""
        await ctx.send("Тест")  # ctx.send - отправка сообщения в чат из которого была вызвана команда

    @commands.command(pass_context=True, name='удали')  # pass_context=True - позволяет писать что-то после команды
    async def delme(self, ctx):
        """Удаление команды вызова"""
        await ctx.delete_message()

    @commands.command(name="сложи")  # можно написать команду с уведомлением бота "@Dipy сложи 123 55"
    async def summ(self, ctx, left: int, right: int):  # !сложи 123 15
        """Складывает 1 число со 2."""
        await ctx.send(left + right)

    @commands.command(name="выбери")
    async def choose(self, ctx, *choices: str):  # !выбери Петя Вася Даша Саша
        """Случайно выписывает слово из предложенных."""
        await ctx.send(random.choice(choices))

    @commands.command(name="повтори")
    async def repeat(self, ctx, times: int, content='повторение...'):  # !повтори 5 Привет друзья!
        """Повторяет сообщение заданное число раз."""
        for i in range(times):
            await ctx.send(content)

    @commands.command()
    async def joined(self, ctx, member: discord.Member):  # !joined @Админ
        """Говорит когда пользователь присоединился к серверу"""
        await ctx.send('{0.name} присоединился {0.joined_at}'.format(member))

    # Группированные команды
    @commands.group(pass_context=True, name='крутой')
    async def cool(self, ctx):
        """
            !крутой 'какой-то текст или обращение'
        """
        if ctx.invoked_subcommand is None:  # !крутой @Вася выдаст сообщение - Нет, @Вася не крутой
            await ctx.send('Нет, {0.subcommand_passed} не крутой'.format(ctx))

    # подкоманда бот
    @cool.command(name='бот')
    async def _bot(self, ctx):  # !крутой бот
        """Бот крутой?"""
        await ctx.send('Да, бот крутой.')


def setup(Dipy):
    Dipy.add_cog(TestCog(Dipy))
