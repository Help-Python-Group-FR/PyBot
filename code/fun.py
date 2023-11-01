import discord
from discord import app_commands

from tools import maths


@app_commands.describe(roll_number="Le nombre de dés à lancer",
                       roll_max="La valeur maximale des feces du dé")
async def dice_command(interaction: discord.Interaction, roll_number: int, roll_max: int):
    """
    Cette commande tire un certain nombre de dés et en resort des statistiques

    Syntaxe : /dice roll_number=... roll_max=...

    roll_number -> Le nombre de foix où le dé est tiré. (Type : Numbre entier, Automatique : 1, Minimum : 1)
    roll_max -> Le nombre max obstensible. (Type : Numbre entier, Automatique : 6, Minimum : 1)
    """
    await interaction.response.send_message(embed=maths.dice(roll_number, roll_max))

# Cette ligne doit se trouver à la fin du fichier !
fun_commands = [{'name':'dice', 'description':'Cette commande tire un certain nombre de dés et en resort des statistiques', 'func':dice_command}]
# Elle sert à ajouter à "l'arbre" des commandes du Bot la commande crée :
#
# Pour cela il faut y mettre un nouveau dictionnaire et y mettre les clés suivantes avec ce qui leur correspond en paramètre :
#   - 'name' : Le nom de ta commande (Ex. say-goodbye)
#   - 'description' : La description de ta commande (Ex. Never Gonna Give You Up !)
#   - 'func' : la fonction qui contient ta commande (Ex. say_goodbye_command) PS. Ne pas mettre les parenthèses
#
# Ex. fun_commands = [{'name':'deuxième-test', 'description':'Hello World !', 'func':first_test},
#                     {'name':'salut', 'description':'Te dis salut !', 'func':hi_command}]
