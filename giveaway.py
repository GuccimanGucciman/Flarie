from datetime import datetime
from config import *
import discord
from asyncio import sleep
import random
from enum import Enum


class GWState(Enum):
    NotActive = 0  # State mellan giveaways (ongoinggw är False)
    Started = 1  # Första meddelandet har mottagits
    Active = 2  # GW är i gång, godkänts av mods
    Rejected = 3  # GW blev rejectad av mods, städa upp
    Finished = 4  # GW är klart och vinnare korats, nästa steg är att meddela och avsluta
    StaffCheck = 5  # GW är skickat till staff för granskning
    Starting = 6  # GW håller på att starta upp
    GetValue = 7  # Användare skickar värdet på GW via DM


class GiveAways(object):

    def __init__(self, bot):

        # Om vi har ett pågående giveaway
        self.ongoinggw = False

        # Om en användare har ett giveaway aktivt så kommer dens användarenamn ha en entry med True som värde
        # i detta dictionarit
        self.msp = {}
        self.vinsthost = {}

        # Author för giveaway (message author)
        self.ma = {}

        # Antalet serverpoäng som begärs läggs in med användarid som nyckel i denna (message content)
        self.mc = {}

        # Räknare som räknar antalet giveaways
        self.nmac = 1

        self.cnmac = {}
        self.vinst = ""
        self.vinsttext = ""
        self.vinsthost = {}
        self.maid = {}
        self.bot = bot
        self._gwstate: GWState = GWState.NotActive

        # The message that starts an active gw, initiera med ett tomt objekt
        self.activegwmessage: discord.Message = None

    @property
    def gwstate(self):
        return self._gwstate

    @gwstate.setter
    def gwstate(self, value: GWState):
        print(f'{datetime.now()} gwstate is {value}')
        self._gwstate = value

    async def gwstatemachine(self, message: discord.Message):
        gwstaffkanaler = ["gwstaff"]
        is_dm = not message.guild
        hasattachment = message.attachments
        no_attachment = not message.attachments
        real_user = not message.author.bot

        if hasattachment and is_dm and message.content:
            # Försök att starta en giveaway på kanalen
            if self.ongoinggw:
                channel = await message.author.create_dm()
                await channel.send("Only one giveaway can be active, try again tomorrow!")
            else:
                # Status är att vi startar upp GW
                self.gwstate = GWState.Starting

                # Spara undan meddelandet som användes för att starta
                self.activegwmessage = message

                # Spara undan attachment för att kunna granska dessa
                # message.attachments.save(f'giveaway_{message.id}_{message.attachments.filename}')

                # Starta giveaway
                await self.startgiveaway(message)

                # Nu är GW startat, vi kommer nu vänta på input från användare
                self.gwstate = GWState.Started

        if is_dm and real_user and self.msp[message.author.id] and no_attachment and self.ongoinggw:
            # State är nu att användare har skickat in ett värde, och vi skall skicka det till granskning
            self.gwstate = GWState.GetValue
            await self.checkgiveaway(message)

            # State är nu att värde är skickat till staff för att kollas
            self.gwstate = GWState.StaffCheck

        if (str(message.channel) in gwstaffkanaler) and self.ongoinggw and real_user:
            # Kolla om staff godkänner giveaway
            if await self.staff_check_giveaway(message):

                # Giveaway är godkänt, annonsera att det finns och starta. Returnera id på vinnare när det är klart
                self.gwstate = GWState.Active
                vinnarnsid = await self.announce_giveaway(message, self.vinsttext, self.vinsthost[self.ma[self.nmac]])

                # Vi är klara, get id på vinnare och skicka meddelande inkluderat vinst
                self.gwstate = GWState.Finished
                vinnarn = message.guild.get_member(vinnarnsid)
                vinnardm = await vinnarn.create_dm()
                await vinnardm.send(f"Congratulations, you won a {self.vinsttext}: {self.vinst}")

                # Vinnare är annonserat och vinst är utdelat, så giveaway är avslutat
                self.gwstate = GWState.NotActive
            else:
                # Giveaway blev inte godkänt av staff, state är rejectad
                self.gwstate = GWState.Rejected
                self.activegwmessage = None
                ogiltiggw = await self.ma[self.nmac].create_dm()
                await ogiltiggw.send(
                    "You have sent in a giveway that has been rejected "
                    "and you will therefor not recieve your <:Server_Credit:736760116707328021>")
                self.ongoinggw = False

                # Vi har nu hanterat städning efter att giveaway var rejectad, så sätt state tillbaka till not active
                self.gwstate = GWState.NotActive

    async def startgiveaway(self, message):
        self.ongoinggw = True
        channel = await message.author.create_dm()
        await channel.send(
            f"**You have started a giveaway**\nIt will en in 24 hours\n"
            f"*If you didn't intend to start a giveaway, contact <@151657008465051648> asap*"
        )
        self.msp[message.author.id] = True
        await channel.send(
            "**How many <:Server_Credit:736760116707328021> was you product worth?**\n*Only numbers!*\n"
            "Staff can see how much you demand, so be truthful! It makes everyones day easier")
        self.vinst = message.attachments[0].url
        self.vinsthost[message.author] = message.author.id
        self.vinsttext = message.content

    async def checkgiveaway(self, message):
        # Generera id för denna gw
        self.nmac += 1

        # Spara undan vem som startat och innehåll
        self.ma[self.nmac] = message.author
        self.mc[self.nmac] = message.content

        # Vi har inte startat än, men ange author som False i giveaway-matrisen
        self.msp[message.author.id] = False

        # Skicka DM till den som startat gw
        channel = await message.author.create_dm()
        await channel.send(
            f"If this is a legit giveaway you will soon receive {message.content} <Server_Credit:736760116707328021>, "
            f"otherwise you will be informed that your giveaway was not accepted")

        # Skicka meddelande till staff och be om godkännande
        guild = self.bot.get_guild(736620864249790475)
        log = guild.get_channel(736620865575321716)
        await log.send(f"{message.author} tried to donate:\n{self.vinst}")
        self.gwstaffkanal = await guild.create_text_channel(name="gwstaff", overwrites={
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)},
                                                            category=categorystaff,
                                                            position=1,
                                                            topic="Do only type here if you know what you're doing",
                                                            reason="Giveawaycheck starting")
        await self.gwstaffkanal.send(f"{message.author} demands {message.content} Server Credit for "
                                     f"{self.vinsttext}:\n{self.vinst} \nIs that okay?")
        await self.gwstaffkanal.send(f"{Admin}\n**Answer with:** y / n")

    async def staff_check_giveaway(self, message):
        status = False
        flarieguild = self.bot.get_guild(736620864249790475)

        flariemember = discord.Guild.get_member(flarieguild, self.ma[self.nmac].id)
        if message.content.upper() == 'Y' and self.ongoinggw:
            await self.serverpts.add_all_members(message)
            await self.serverpts.addserverpoints(message, flariemember, self.mc[self.nmac])
            status = True
        elif message.content.upper() == 'N' and self.ongoinggw:
            None
        else:
            await self.gwstaffkanal.send("ERRRH, wrong! Please try again...")
            status = await self.staff_check_giveaway(message)
        await self.gwstaffkanal.delete(reason="Giveawaycheck ending")
        return status

    def cancel_giveaway(self):
        self.ongoinggw = False
        self.gwstate = GWState.NotActive
        self.msp[self.activegwmessage.author.id] = False
        self.activegwmessage = None
        self.vinsttext = ""

    async def announce_giveaway(self, message, pris, host):
        flarieguild = self.bot.get_guild(736620864249790475)
        hostare = discord.Guild.get_member(flarieguild, host)
        embed = discord.Embed(title=f"{pris}!")
        embed.add_field(name=f"Ends: {datetime.utcnow()} - {datetime.utcnow().day + 1}/{datetime.utcnow().month} UTC",
                        value=f"*Host: {hostare}!*")
        embed.color = discord.Color(15782199)
        guild = self.bot.get_guild(736620864249790475)
        memberroll = guild.get_role(736620864505905153)
        self.giveawaykanal = await guild.create_text_channel(name="giveaway", overwrites={
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            memberroll: discord.PermissionOverwrite(read_messages=True, send_messages=False, add_reactions=False)},
                                                             category=self.bot.get_channel(736620865730641957),
                                                             position=1,
                                                             topic="Join the current giveaway!",
                                                             reason="Giveaway starting")
        votemsg = await self.giveawaykanal.send(embed=embed, content=":tada: Giveaway :tada:")
        await votemsg.add_reaction('⬆️')
        allman = self.bot.get_channel(736620865730641958)
        allmanembed = discord.Embed(title="New giveaway", color=discord.Color(15782199))
        allmanembed.add_field(name="Price", value=pris)
        allmanembed.add_field(name="Host", value=hostare)
        allmanembed.add_field(name="Click here!", value=f"<#{self.giveawaykanal.id}>")
        await allman.send(embed=allmanembed)
        await sleep(3600 * 24)
        Botreaktion = message.guild.get_member(592464637396647957)
        gwmsg = discord.utils.get(self.bot.cached_messages, id=votemsg.id)
        reaktioner = await gwmsg.reactions[0].users().flatten()
        reaktioner.remove(Botreaktion)
        if hostare in reaktioner:
            reaktioner.remove(hostare)
        if len(reaktioner) > 0:
            w = random.randint(0, len(reaktioner) - 1)
            ww = reaktioner[w].id
            if self.ongoinggw:
                await allman.send(
                    f'**The winner of {pris} is...**\n<@{ww}>!\n:tada: Congrats to you! :tada:')
                await self.giveawaykanal.delete(reason="Giveaway ended")
                return ww
        else:
            await allman.send("Not enough reactions to end giveaway")
            await self.giveawaykanal.delete(reason="Giveaway ended")


if __name__ == "__main__":
    pass
