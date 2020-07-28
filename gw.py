#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://discord.com/api/oauth2/authorize?client_id=736971898851950652&permissions=8&scope=bot

import discord
from config import *
from random import randint


class GiveAways(object):

    def __init__(self, robot):
        self.host = {}
        self.wonitem = {}
        self.wonitemtext = {}
        self.bot = robot

    async def giveaway(self, message):
        flarie = bot.get_guild(serverid)
        Bot = flarie.get_member(serverid)
        Memberrole = flarie.get_role(serverid)
        dm = message.channel
        is_dm = not message.guild
        hasattachment = message.attachments
        real_user = not message.author.bot
        scmsg = {}
        if is_dm and hasattachment and real_user and message.content:
            tid = datetime.utcnow()
            self.host[message.author.id, tid] = message.author
            scmsg[message.author.id, tid] = ""
            self.wonitem[message.author.id, tid] = message.attachments[0].url
            self.wonitemtext[message.author.id, tid] = message.content
            await dm.send(f"You have initiated a giveaway\nTo continue, please type how many Server Credits this "
                          f"code is worth (Only numbers)\nTo cancel the giveaway, type 'cancel'")

            def check(m):
                return m.channel == dm and not m.author.bot and m.content is not self.wonitemtext[message.author.id, tid]

            try:
                scmsg[message.author.id, tid] = await bot.wait_for('message', check=check, timeout=300)
            except TimeoutError:
                 await dm.send("You took longer than expected\n*Giveaway cancelled*")
                 return
            if scmsg[message.author.id, tid].content.lower() == "cancel":
                await dm.send("Alright, cancelling giveaway...")
                return
            elif not scmsg[message.author.id, tid].content.isdigit() and not scmsg[message.author.id, tid].content.lower() == 'cancel':
                await dm.send("Invalid input, cancelling giveaway")
                return
            elif scmsg[message.author.id, tid].content.isdigit():
                print("Giveawaycheck startning")
                scmsg[message.author.id, tid].content = int(scmsg[message.author.id, tid].content)
                await dm.send("Perfect! We will now process you request\n"
                              "This may take a while")
                gwstaffkanal = await flarie.create_text_channel(
                    name=f"{message.author.display_name}'s-gwrequest",
                    overwrites={
                        flarie.default_role: discord.PermissionOverwrite(
                            read_messages=False),
                        flarie.me: discord.PermissionOverwrite(
                            read_messages=True)},
                    category=self.bot.get_channel(736620865575321712),
                    position=1,
                    topic="Type only if you know what you're doing",
                    reason="Giveawaycheck starting")
                approvalmsg = await gwstaffkanal.send(
                    f"<@{message.author.id}> demands {scmsg[message.author.id, tid].content} Server Credit for "
                    f"{self.wonitemtext[message.author.id, tid]}:\n{self.wonitem[message.author.id, tid]} \nIs that okay? <@&507354790888472587>")
                await approvalmsg.add_reaction('👍')
                await approvalmsg.add_reaction('👎')

                def check(reaction, user):
                    return not user.bot

                reaction = await bot.wait_for('reaction_add', check=check)
                if reaction[0].emoji == '👍':
                    await gwstaffkanal.delete(reason="Giveaway approved")
                    time = datetime.utcnow()
                    minut = time.minute
                    if minut < 10:
                        minut = f"0{time.minute}"
                    embed = discord.Embed(title=f"{self.wonitemtext[message.author.id, tid]}!")
                    embed.add_field(
                        name=f"Ends: {time.hour}:{minut} - {time.day + 1}/{time.month} UTC",
                        value=f"*Host: {self.host[message.author.id, tid]}!*")
                    embed.color = discord.Color(15782199)
                    giveawaykanal = await flarie.create_text_channel(
                        name=f"{self.host[message.author.id, tid].display_name}'s giveaway", overwrites={
                            flarie.default_role: discord.PermissionOverwrite(read_messages=False),
                            Memberrole: discord.PermissionOverwrite(read_messages=True, send_messages=False,
                                                                    add_reactions=False)},
                        category=self.bot.get_channel(736620865730641957),
                        position=1,
                        topic="Join the current giveaway!",
                        reason="Giveaway starting")
                    votemsg = await giveawaykanal.send(embed=embed, content=":tada: Giveaway :tada:")
                    await votemsg.add_reaction('⬆️')
                    allman = self.bot.get_channel(736620865730641958)
                    allmanembed = discord.Embed(title="New giveaway", color=discord.Color(15782199))
                    allmanembed.add_field(name="Price", value=self.wonitemtext[message.author.id, tid])
                    allmanembed.add_field(name="Host", value=self.host[message.author.id, tid])
                    allmanembed.add_field(name="Click here!", value=f"<#{giveawaykanal.id}>")
                    await allman.send(embed=allmanembed)
                    await sleep(3600 * 24)
                    gwmsg = discord.utils.get(self.bot.cached_messages, id=votemsg.id)
                    reaktioner = await gwmsg.reactions[0].users().flatten()
                    reaktioner.remove(Bot)
                    if self.host[message.author.id, tid] in reaktioner:
                        reaktioner.remove(self.host[message.author.id, tid])
                    if len(reaktioner) > 0:
                        w = randint(0, len(reaktioner) - 1)
                        ww = reaktioner[w].id
                        await allman.send(
                            f'**The winner of {self.wonitemtext[message.author.id, tid]} is...**\n<@{ww}>!\n'
                            f':tada: Congrats to you! :tada:')
                        await giveawaykanal.delete(reason="Giveaway ended")
                        return ww
                    else:
                        await allman.send("Not enough reactions to end giveaway")
                        await giveawaykanal.delete(reason="Giveaway ended")
                elif reaction[0].emoji == '👎':
                    await dm.send("Your giveaway was not approved")
                    await gwstaffkanal.delete(reason="Giveaway not approved")
        return
