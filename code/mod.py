import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_components import * # évite de faire ça
from discord_slash.utils.manage_components import create_choice, create_option

prefix = "/"
bot = commands.Bot(command_prefix=prefix)

