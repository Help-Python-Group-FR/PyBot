"""
This file contain all the maths functions and command used in the bot.
"""

import random
import discord


def dice(roll_number: int, roll_max: int):
    """
    Cette fonction tire un certain nombre de dés et en resort des statistiques.

    roll_number -> Le nombre de foix où le dé est tiré. (Type : Numbre entier, Automatique : 1, Minimum : 1)
    roll_max -> Le nombre max obstensible. (Type : Numbre entier, Automatique : 6, Minimum : 1)
    """

    if roll_number < 1:
        roll_number = 1  # S'assure que roll_number saoit au moin égal à 1.
    if roll_max < 2:
        roll_max = 2  # S'assure que roll_max saoit au moin égal à 2.

    rolls = []
    for _ in range(roll_number):
        rolls.append(random.randint(1, roll_max))  # Simule tout les lancés de dés.

    result = discord.Embed(title=":tada: | Alea jacta est !",
                           description=f"{roll_number} dés ont été lancés avec des faces entre 1 et {roll_max}.",
                           color=discord.Color.pink())
    result.set_thumbnail(url='https://media.tenor.com/xrrd8RNhd0MAAAAj/dice-sticker.gif')

    result.add_field(name=":game_die: Les résultats sont respectivement :", value=f"{'; '.join(str(item) for item in rolls)}")
    result.add_field(name=":bar_chart: Statistiques :", value=f"Moyenne : {sum(rolls) / len(rolls)}\nTotal : {sum(rolls)}\n"
                                                              f"Plus grand chiffre obtenu : {sorted(rolls)[len(rolls) - 1]}\n"
                                                              f"Plus petit chiffre obtenu : {sorted(rolls)[0]}")

    result.set_footer(text="Command by Futuray")

    return result