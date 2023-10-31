"""
This file contain all the maths functions and command used in the bot.
"""

import random

def dice(roll_number: int, roll_max: int) :
    """
    Cette fonction tire un certain nombre de dés et en resort des statistiques.
    
    roll_number -> Le nombre de foix où le dé est tiré. (Type : Numbre entier, Automatique : 1, Minimum : 1)
    roll_max -> Le nombre max obstensible. (Type : Numbre entier, Automatique : 6, Minimum : 1)
    """
    
    if roll_number < 1 :
        roll_number = 1 # S'assure que roll_number saoit au moin égal à 1.
    if roll_max < 2 :
        roll_max = 2 # S'assure que roll_max saoit au moin égal à 2.
    
    rolls = []
    for _ in range(roll_number) :
        rolls.append(random.randint(1, roll_max)) # Simule tout les lancés de dés.
    
    result = f'''>>> Alea jacta est !
{roll_number} dés ont été lancés avec des faces entre 1 et {roll_max}.

:game_die: Les résultats sont respectivement :
{(";").join(str(item) for item in rolls)}

:bar_chart: Statistiques :
Moyenne : {sum(rolls) / len(rolls)}
Total : {sum(rolls)}
Plus grand chiffre obtenu : {sorted(rolls)[len(rolls)-1]}
Plus petit chiffre obtenu : {sorted(rolls)[0]}

`Commande ajouté par <@688090056799289482>`
'''
    
    return result
