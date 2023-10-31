import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    """
    Cette commande sert a démarré le bot :
        -Elle change son son statut + son activité;
        -Elle synchronise "l'arbre" des commandes;
    """
    await tree.sync()
    await client.change_presence(activity=discord.Game("/game"), status=discord.Status.online)
    print(f"We have logged in as {client.user}")

@tree.command(name="dice",
              description="Cette commande tire un certain nombre de dés et en resort des statistiques")
@app_commands.describe(roll_number="Le nombre de dés à lancer",
                       roll_max="La valeur maximale des feces du dé")
async def dice(ctx, roll_number: int, roll_max: int):
    """
    Cette commande tire un certain nombre de dés et en resort des statistiques
    
    Syntaxe : /dice roll_number=... roll_max=...
    
    roll_number -> Le nombre de foix où le dé est tiré. (Type : Numbre entier, Automatique : 1, Minimum : 1)
    roll_max -> Le nombre max obstensible. (Type : Numbre entier, Automatique : 6, Minimum : 1)
    """
    await ctx.response.send_message(maths.dice(roll_number, roll_max))

TOKEN = ""
print("Launch of the Client...")
client.run(TOKEN)
