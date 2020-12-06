import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def M(ctx, arg):
    channel = bot.get_channel(769281367292510219)
    if( 15 >= len(arg) >= 7):
        await channel.send(arg)
    else:
        await ctx.send("Айди должно состоять от 7 до 15 цифр")


@bot.command()
async def H(ctx, arg):
    channel = bot.get_channel(769283150072250369)
    if (15 >= len(arg) >= 7):
        await channel.send(arg) 
    else:
        await ctx.send("Айди должно состоять от 7 до 15 цифр")

@bot.command()
async def L(ctx, arg):
    channel = bot.get_channel(769283137996980235)
    if (15 >= len(arg) >= 7):
        await channel.send(arg)
    else:
        await ctx.send("Айди должно состоять от 7 до 15 цифр")

@bot.command()
async def O(ctx, arg):
    channel = bot.get_channel(769281389459275786)
    if (15 >= len(arg) >= 7):
        await channel.send(arg)
    else:
        await ctx.send("Айди должно состоять от 7 до 15 цифр")

@bot.command()
async def P(ctx, arg):
    channel = bot.get_channel(774755812572790815)
    if (15 >= len(arg) >= 7):
        await channel.send(arg)
    else:
        await ctx.send("Айди должно состоять от 7 до 15 цифр")

@bot.command()
async def K(ctx, arg):
    channel = bot.get_channel(768609614459437126)
    if (15 >= len(arg) >= 7):
        await channel.send(arg)
    else:
        await ctx.send("Айди должно состоять от 7 до 15 цифр")

@bot.command()
async def info(ctx):
    await ctx.send("$M ID - мифическая мода \n $H ID - аккаунты между L и М \n $L ID - 1-2 прокачиваемых оружий до килчата \n $O ID - аккаунты с титулами  \n $P ID - нерусские \n $K ID - Корейка  \n")



bot.run('Nzc0NzA5Mjk2OTI2Njg3MzE0.X6buQQ.FIAXN9ZLpxtSLC8jVqDluT_wIts')
