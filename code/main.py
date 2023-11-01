import discord
from discord import app_commands

# Ici j'importe les fichiers où l'on a défini les commandes
import fun
import mod
import utils

# Je définis les variables essentiels du Bot ici :
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Ici j'ajoute les commandes définient dans les autres fichiers :
for command in fun.fun_commands:
    tree.command(name=command['name'], description=command['description'])(command['func'])

for command in mod.mod_commands:
    tree.command(name=command['name'], description=command['description'])(command['func'])

for command in utils.utils_commands:
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


@tree.error
async def on_command_error(interaction, error):
    """
    Cette commande s'éxecute lorsque le Bot reçoit une erreur :
        - Pour l'instant elle ne traite que les erreurs de permissions;
    """
    if isinstance(error, app_commands.MissingPermissions):
        embed = discord.Embed(title=":x: | Tu n'as pas la permission d'utiliser cette commande !", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    raise error

TOKEN = "OTIxMTQ1MzU1NTYxNzQyMzk2.GwXQOU.XkunSeQwwLGOoZOJLYwYDFd1Q91amN-ASxutDE"
print("Launch of the Client...")
client.run(TOKEN)
