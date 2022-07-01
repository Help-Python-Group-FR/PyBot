import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_components import * # évite de faire ça
from discord_slash.utils.manage_components import create_choice, create_option

from main import bot, slash, prefix, send_error, MyEmbed

help_commands = []

def help_append(name, value):
  help_commands.append([name, value])
