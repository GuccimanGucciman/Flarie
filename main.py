#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://discord.com/api/oauth2/authorize?client_id=736971898851950652&permissions=8&scope=bot

from gw import GiveAways
from config import *
from database import addMember

games = minigames(bot)
gws = GiveAways(bot)
memberhandler = MemberHandler(bot)


@bot.command(name="colour", help="Alias to color")
async def colour(message, colour):
    await memberhandler.set_member_role_color(message, colour)
    embed = discord.Embed(title=f"You now have the role {colour}")
    await message.send(embed=embed)
    await message.message.delete()


@colour.error
async def colour_error(message, error, commands):
    await memberhandler.error_handler(message, error, commands)


@bot.command(name="color", help="Gives you the color you specify")
async def color(message, color):
    await colour(message, color)


@color.error
async def color_error(message, error, commands):
    await memberhandler.error_handler(message, error, commands)


@bot.command(name="staff", help="Visar vilka medlemmar som jobbar på servern")
async def staffs(message):
    await memberhandler.get_staff(message)
    await message.message.delete()


@bot.command(name="profile", help="See your profile")
async def profile(message, member: discord.Member = ""):
    if str(message.channel) in commandchannels:
        await memberhandler.get_profile(message, member)
        await message.message.delete()


@bot.command(name="clear", help="Clear messages")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount + 1)


@bot.command(name="top", help="Shows the top of specified currency")
async def top(message, type):
    if str(message.channel) in commandchannels:
        await memberhandler.get_top(message, type)
        await message.message.delete()

@bot.command(name="buy", help="Buy coins")
@commands.cooldown(1, 86400, commands.BucketType.user)
async def buy(message, coins):
    await memberhandler.purchase_coins(message, coins)
    await message.message.delete()

@bot.event
async def on_message(message):
    await addMember(message.author.name, message.author.id)
    await gws.giveaway(message)
    await bot.process_commands(message)
    await games.handlewin(message)


bot.run(token)
