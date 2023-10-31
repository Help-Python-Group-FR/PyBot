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

TOKEN = ""
print("Launch of the Client...")
client.run(TOKEN)
