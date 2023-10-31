import discord
from discord import app_commands

async def first_test(interaction : discord.Interaction):
    await interaction.response.send_message("Hello World !")

fun_commands = [{'type':'default', 'name':'deuxième-test', 'description':'Hello World !', 'func':first_test}]
