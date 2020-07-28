from asyncio import sleep
from database import getInfo, getWarnings, levelget, getTop, getPoints, addPoints
import config
from config import *
from datetime import datetime


class MemberHandler(object):
    """
    Här håller vi koll på alla medlemmar som finns på servern

    Typiska funktioner är lägga till, ta bort och varna medlemmar, men också att ge info till medlemmar och
    ge nya roller.
    """

    def __init__(self, bot):
        self.bot = bot
        self.log = bot.get_channel(736620865575321716)
        self.flarie = bot.get_guild(736620864249790475)

    async def warn(self, ctx, varnadmedlem: discord.Member, anledning=""):
        muterole = discord.utils.get(ctx.guild.roles, name="Muted")
        await varnadmedlem.add_roles(muterole)
        mutetid = datetime.utcnow().hour + 5
        mutemin = datetime.utcnow().minute
        if mutetid > 23:
            mutetid = mutetid - 24
        warns = getWarnings(varnadmedlem.id)
        embed = discord.Embed(title=f"{varnadmedlem} warned", description=f"Muted until: {mutetid}:{mutemin}",
                              color=discord.Color(16711680))
        embed.add_field(name="Warnings", value=warns)
        if not anledning == "":
            embed.add_field(name="Reason", value=anledning)
        await ctx.send(embed=embed)
        channel = self.bot.get_channel(613820987183464529)
        embed = discord.Embed(title=f'{varnadmedlem} warned', description=f"**Reason:** {anledning}")
        embed.color = discord.Color(16711680)
        embed.set_thumbnail(url=f'{varnadmedlem.avatar_url}')
        await channel.send(embed=embed)
        dmembed = discord.Embed(title="You just got warned", description="Mute - 5 hours",
                                color=discord.Color(16711680))
        channel = varnadmedlem.create_dm()
        await channel.send(embed=dmembed)
        await sleep(18000)
        await varnadmedlem.remove_roles(muterole)

    async def remove_member(self, member):
        """
        Event som körs när en användare lämnar servern

        :param member: Vilken användare som tas bort
        :return: Meddelade om att användaren lämnade server
        """
        embed = discord.Embed(title=f'**{member.display_name}**',
                              description=f' :outbox_tray: {member} left the server')
        embed.set_footer(text=f'ID: {member.id}')
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.color = discord.Color(16711680)
        await self.log.send(embed=embed)

    async def member_joined(self, member):
        embed = discord.Embed(title=f'**{member.display_name}**',
                              description=f':inbox_tray: {member} joined the server')
        embed.set_footer(text=f'ID: {member.id}')
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.color = discord.Color(2344560)
        await self.log.send(embed=embed)
        content = ('''**Välkommen!**
                    Välkommen till Flaries officiella discordserver! För att börja skriva med alla på servern 
                    måste du ha ett telefonnummer registrerat på ditt discordkonto! 

                    Om du har problem med detta kontakta en server admin, till exempel <@151657008465051648> 
                    via direktmeddelande  :relaxed:

                    *Läs i informationskanalerna för att se vad du kan göra på servern, hur du vinner 
                    Flariecoins bland annat!*''')
        channel = await member.create_dm()
        await channel.send(content)

    async def get_member_info(self, message, member: discord.Member):
        infon = getInfo(member.id)
        await message.send(f"{member.display_name}'s info: {', '.join(infon)}")

    async def set_member_role_color(self, message, colour):
        if message.guild.get_role(736620864249790481) in message.author.roles:
            rolenames = ['Red', 'Green', 'Blue']
        elif message.guild.get_role(736620864249790482) in message.author.roles:
            rolenames = ['Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Pink', 'Light Pink',
                         'White']
        roles = {}
        for role in rolenames:
            roles[role.lower()] = discord.utils.get(self.bot.get_guild(736620864249790475).roles, name=role)
        nmr = 0
        for i in range(len(roles.values())):
            await message.author.remove_roles(list(roles.values())[nmr])
            nmr += 1
        await message.author.add_roles(roles[colour.lower()])

    async def get_staff(self, message):
        admin = message.guild.get_role(736620864509837351)
        mod = message.guild.get_role(736620864509837348)
        hos = message.guild.get_role(736620864509837352)
        bb = [member.display_name for member in admin.members]
        cc = [member.display_name for member in mod.members]
        dd = [member.display_name for member in hos.members]
        embed = discord.Embed(title="Staff", color=discord.Color(5945328))
        embed.add_field(name=f"**{hos.name}**", value="\n".join(dd), inline=False)
        embed.add_field(name=f"**{admin.name}**", value="\n".join(bb), inline=False)
        embed.add_field(name=f"**{mod.name}**", value="\n".join(cc), inline=False)
        await message.send(embed=embed)

    async def get_profile(self, message, member):
        if member is "":
            person = message.author
        else:
            person = member
        FT = await getPoints(person.id, "ft")
        SC = await getPoints(person.id, "sc")
        AP = await getPoints(person.id, "ap")
        n = 0
        totalAP = 0
        memberlevel = await levelget(message.author.id)
        while n <= memberlevel:
            level = 5 * n ** 2 + 50 * n + 100
            n += 1
            totalAP += level
        Level = await levelget(person.id)
        embed = discord.Embed(description=f"Status: {person.status}")
        embed.add_field(name="**Flarie Tokens**", value=f"{FT}")
        embed.color = discord.Color(5945328)
        embed.add_field(name="**Server Credit**", value=f"{SC}")
        embed.add_field(name="**AP Level**", value=f"Level: {Level}\nAP: {AP}/{totalAP}")
        embed.add_field(name="**Highest rank**", value=person.top_role)
        embed.set_footer(text=f"Member joined: {person.joined_at.__format__('%a, %d %b %Y %H:%M')}\n"
                              f"Account created: {person.created_at.__format__('%a, %d %b %Y %H:%M')}")
        embed.set_author(name=f"{person.display_name}'s profile", icon_url=person.avatar_url)
        await message.send(embed=embed)

    async def error_handler(self, message, error, commands):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await message.send("Specify what colour you'd like to apply for in the same message")
        elif isinstance(error, commands.errors.BadArgument):
            await message.send("That colour does not exist")
        elif isinstance(error, commands.errors.MissingAnyRole):
            await message.send("You don't have the required role for this command")

    async def get_top(self, message, type):
        if type.lower() == "servercredit" or type.lower() == "servercredits":
            type = "SC"
        elif type.lower() == "flarietoken" or type.lower() == "flarietokens":
            type = "FT"
        elif type.lower() == "activepoint" or type.lower() == "activepoints":
            type = "ap"
        if type.lower() == "ap":
            type = "Level"
        top = await getTop(type)
        if type.lower() == "sc":
            name = "Server Credits"
        elif type.lower() == "ft":
            name = "Flarie Tokens"
        elif type.lower() == "level":
            name = "Levels"
        else:
            name = ""
        levelembed = discord.Embed(title=":trophy: Top 10 :trophy:", description=type.upper(), color=discord.Color(15782199))
        levelembed.add_field(name=f"{1}: {top[0][0]}", value=f"{top[0][1]} {name}", inline=False)
        levelembed.add_field(name=f"{2}: {top[1][0]}", value=f"{top[1][1]} {name}", inline=False)
        levelembed.add_field(name=f"{3}: {top[2][0]}", value=f"{top[2][1]} {name}", inline=False)
        levelembed.add_field(name=f"{4}: {top[3][0]}", value=f"{top[3][1]} {name}", inline=False)
        levelembed.add_field(name=f"{5}: {top[4][0]}", value=f"{top[4][1]} {name}", inline=False)
        levelembed.add_field(name=f"{6}: {top[5][0]}", value=f"{top[5][1]} {name}", inline=False)
        levelembed.add_field(name=f"{7}: {top[6][0]}", value=f"{top[6][1]} {name}", inline=False)
        levelembed.add_field(name=f"{8}: {top[7][0]}", value=f"{top[7][1]} {name}", inline=False)
        levelembed.add_field(name=f"{9}: {top[8][0]}", value=f"{top[8][1]} {name}", inline=False)
        levelembed.add_field(name=f"{10}: {top[9][0]}", value=f"{top[9][1]} {name}", inline=False)
        await message.send(embed=levelembed)

    async def purchase_coins(self, message, coins):
        info = await getInfo(message.author.id)
        lst = [100, 300, 500]
        if int(coins) in lst and (info[0] is not None or info[1] is not None):
            c = await getPoints(message.author.id, "ft")
            vinnaruppgifter_channel = self.bot.get_channel(688745668155670684)
            if int(coins) == 100 and c >= 50:
                await message.send(f"Bought {coins} coins!")
                await vinnaruppgifter_channel.send(
                    f"**{coins} coins**\n<@{message.author.id}>\nEmail: {info[0]}\nPhonenumber: {info[1]}\n-----")
                await addPoints(message.author.id, "ft", -50)
            elif int(coins) == 300 and c >= 100:
                await message.send(f"Bought {coins} coins!")
                await vinnaruppgifter_channel.send(
                    f"**{coins} coins**\n<@{message.author.id}>\nEmail: {info[0]}\nPhonenumber: {info[1]}\n-----")
                await addPoints(message.author.id, "ft", -100)
            elif int(coins) == 500 and c >= 150:
                await message.send(f"Bought {coins} coins!")
                await vinnaruppgifter_channel.send(
                    f"**{coins} coins**\n<@{message.author.id}>\nEmail: {info[0]}\nPhonenumber: {info[1]}\n-----")
                await addPoints(message.author.id, "ft", -150)
            else:
                await message.send(f"You don't have enough Flarie Tokens to buy {coins} coins!")
        else:
            if str(message.channel) in config.commandchannels:
                await message.send(
                    f"You can buy either 100, 300 or 500 coins in <#{commandchannelid}>"
                    f"\n*Usage: {prefix}buy 100/300/500*"
                )