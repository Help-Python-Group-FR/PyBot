import discord
from discord import app_commands

from tools import maths


@app_commands.describe(roll_number="Le nombre de dés à lancer (Max. 100)",
                       roll_max="Le nombre des faces des dés (Max. 50)")
@app_commands.rename(roll_number="dés-lancés", roll_max="faces")
async def dice_command(interaction: discord.Interaction, roll_number: int = 1, roll_max: int = 6):
    """
    Cette commande tire un certain nombre de dés et en resort des statistiques

    Syntaxe : /dice roll_number=... roll_max=...

    roll_number -> Le nombre de foix où le dé est tiré. (Type : Nombre entier, Automatique : 1, Minimum : 1)
    roll_max -> Le nombre max obstensible. (Type : Nombre entier, Automatique : 6, Minimum : 1)
    """
    if roll_number < 1: roll_number = 1
    if roll_max < 1: roll_max = 1
    if roll_number > 100: roll_number = 100
    if roll_max > 50: roll_max =50

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

if __name__ == '__main__':
    import os
    os.system("python main.py")
