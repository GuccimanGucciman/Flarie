import discord
from config import *
from database import APadd, levelget, leveladd, getTop, addPoints, getPoints


class XPSystem:

    def __init__(self, bot):

        # Channels som man kan få xp för
        self.channels = ["flarie", "media"]

        # Referens til bot för att kunna köra uppdateringar
        self.bot = bot

        # En dictionary med medlemmar som har fått xp och när det senast hände
        self.last_used_xp = {}

        self.currentxp = 0
        self.total_level = 0

    async def add_AP(self, message):
        if message.author.id in self.last_used_xp.keys():
            difference = datetime.now() - self.last_used_xp[message.author.id]
            seconds_passed = difference.total_seconds()
            if seconds_passed <= 60:
                return
            else:
                await self.addAP(message)
        else:
            await self.addAP(message)

    async def addAP(self, message):
        self.last_used_xp[message.author.id] = datetime.now()
        self.currentxp = await self.add_ap_for_member(message)
        self.total_level = await self.get_ap_based_on_level(message)
        if self.currentxp > self.total_level:
            lvl = await levelget(message.author.id) + 1
            await self.set_ap_level(message, lvl)

    @staticmethod
    async def add_ap_for_member(message):
        APamount = randint(10, 25)
        lastAP = await getPoints(message.author.id, "ap")
        addedAP = lastAP + APamount
        await APadd(message.author.id, int(addedAP))
        currentAP = await getPoints(message.author.id, "ap")
        return currentAP

    @staticmethod
    async def get_ap_based_on_level(message):
        n = 0
        total_level = 0
        memberlevel = await levelget(message.author.id)
        while n <= memberlevel:
            level = 5 * n ** 2 + 50 * n + 100
            n += 1
            total_level += level
        return total_level

    async def set_ap_level(self, message, new_level):
        flarieguild = self.bot.get_guild(serverid)
        await leveladd(new_level, message.author.id)
        if 5 <= new_level <= 20:
            await addPoints(message.author.id, "ft", 10)
        elif 21 <= new_level <= 50:
            await addPoints(message.author.id, "ft", 20)
        elif 51 <= new_level:
            await addPoints(message.author.id, "ft", 30)

        level_list = [1, 10, 20, 30, 40, 50, 75, 100, 125, 150]
        author_level = levelget(message.author.id)
        if author_level in level_list:
            await message.author.add_roles(discord.utils.get(flarieguild.roles, name=f'Level {author_level}'))
            if author_level is 1:
                await message.author.add_roles(discord.utils.get(flarieguild.roles, name='Member'))
        channel = flarieguild.get_channel(commandchannelid)
        await channel.send(
            f"Congrats <@{message.author.id}>! Du just reached level {new_level}! :tada:")


