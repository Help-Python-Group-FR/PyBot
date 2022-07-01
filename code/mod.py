import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_components import * # évite de faire ça
from discord_slash.utils.manage_components import create_choice, create_option

from main.py import bot, slash, prefix, send_error, MyEmbed
from main.py import help_append as ha

def help_append(name, value):
  ha("mod", name, value)
