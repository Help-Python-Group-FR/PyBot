import discord
from discord import app_commands
import fun

# Je définis les variables essentiels du Bot ici :
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Ici j'ajoute les commandes définient dans les autres fichiers :
for command in fun.fun_commands:
    tree.command(name=command['name'], description=command['description'])(command['func'])


@client.event
async def on_ready():
    """
    Cette commande s'éxecute lorsque le bot a démarré :
        - Elle change son son statut + son activité;
        - Elle synchronise "l'arbre" des commandes;
    """
    await tree.sync()
    await client.change_presence(activity=discord.Game("/game"), status=discord.Status.online)
    print(f"We have logged in as {client.user}")

TOKEN = "OTIxMTQ1MzU1NTYxNzQyMzk2.GygPpQ.O30WxZlYFqXG7W-SVKZiBreQS1CSsERP2VYUOY"
print("Launch of the Client...")
client.run(TOKEN)
