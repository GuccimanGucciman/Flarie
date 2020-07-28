import discord
from discord.ext import commands
from memberhandler import MemberHandler
from datetime import datetime
from asyncio import sleep
from random import randint, shuffle
from minigamesclass import minigames

# Control panel

minigamepris = 0  # Amount of points to give to winner by default

prefix = '!'
minigamescolour = discord.Color(15733703)
APcolour = discord.Color(65380)

# Constants

flarietoken = "<:Flarie_Token:736734202854113381>"
servercredit = "<:Server_Credit:736737185746649150>"
activepoint = "<:Active_Point:736732829177741352>"

bot = commands.Bot(command_prefix=prefix)

token = "NzM2OTcxODk4ODUxOTUwNjUy.Xx2kkA.Z-oTnyGt7sPCpFiUH16YFOv9oUs"
Admin = "<@&736620864509837351>"
Ruby = 736620864249790481
Emerald = 736620864249790482
FirstDonor = 736620864249790483
serverid = 736620864249790475
flariechannelid = 736620865730641958
commandchannelid = 736620865868791808
commandchannels = [
    'commands', 'adminchatt', 'modchat', 'kladd', 'log', 'updates', 'news'
]
