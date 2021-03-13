import discord
from discord.ext import commands
import json


with open('json/dipy.json', encoding="utf8") as discord_file:
    discord_json = json.load(discord_file)


def get_prefix(bot, message):
    """Настройка префиксов для бота"""

    prefixes = ["!", "бот ", "dipy "]

    if not message.guild:
        return "!"

    return commands.when_mentioned_or(*prefixes)(bot, message)


intents = discord.Intents.default()
intents.members = True

Dipy = commands.Bot(command_prefix=get_prefix, description=discord_json['description'], intents=intents)

# Список шестерёнок
initial_extensions = [
    "cogs.dipy"
]


@Dipy.event
async def on_ready():
    print('Бот загружен как')
    print('{} ({})'.format(Dipy.user.name, Dipy.user.id))
    print('------')
    await Dipy.change_presence(status=discord.Status.online, activity=discord.Game("!help"))

for extension in initial_extensions:
    try:
        Dipy.load_extension(extension)
        print('Загрузка шестерёнки {}'.format(extension))
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Ошибка загрузки шестерёнки {}\n{}'.format(extension, exc))


@Dipy.command()
@commands.is_owner()
async def stop(ctx):
    exit()


@Dipy.command()
@commands.is_owner()
async def cogs_load(ctx, extension_name: str):
    """Загрузка шестерёнки."""
    try:
        Dipy.load_extension(extension_name)
        await ctx.send("{} загружена.".format(extension_name))
        print("{1}, шестерёнка {0} загружена.".format(extension_name, ctx.author.name))
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return


@Dipy.command()
@commands.is_owner()
async def cogs_unload(ctx, extension_name: str):
    """Отключение шестерёнки."""
    Dipy.unload_extension(extension_name)
    await ctx.send("{} отключена.".format(extension_name))
    print("Шестерёнка {0} отключена. {1}".format(extension_name, ctx.author.name))

@Dipy.command()
@commands.is_owner()
async def cogs_reload(ctx, extension_name: str):
    """Перезагрузка шестерёнки."""
    try:
        Dipy.unload_extension(extension_name)
        Dipy.load_extension(extension_name)
        await ctx.send("{} перезагружена.".format(extension_name))
        print("Шестерёнка {0} перезагружена. {1}".format(extension_name, ctx.author.name))
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return

@Dipy.command()
@commands.is_owner()
async def reload(ctx):
    """Перезагрузка всех шестерёнок."""
    try:
        for extension in initial_extensions:
            Dipy.unload_extension(extension)
            Dipy.load_extension(extension)
        await ctx.send("Все шестерёнки перезагружены.")
        print("Все шестерёнки перезагружены. {}".format(ctx.author.name))
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return

#TOKEN - меняете на свой "абрака.дабра1234567890" - не забудте про кавычки
Dipy.run("TOKEN", reconnect=True)
