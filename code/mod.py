import discord
from discord import app_commands
import pickle


@app_commands.checks.has_permissions(administrator=True)
@app_commands.rename(channel="salon")
@app_commands.describe(channel="Le salon dans lequel tu veux que les messages de bienvenue s'affichent."
                               " (Laisser vide pour désactiver)")
async def welcome_command(interaction: discord.Interaction, channel: discord.TextChannel = None):
    """
    Cette commande permet de définir un salon pour envoyer un mesage de bienvenue dans un salon donné :
        - Paramètre 'channel' : Le salon où l'on veut envoyer les messages de bienvenues;
    """

    # Ici je récupère les informations contenues dans le fichier data/welcome_channel
    try:
        with open("data/welcome_channel", "rb") as file:
            welcome_channels = pickle.Unpickler(file).load()

    except EOFError:
        welcome_channels = {}

    if channel is not None:
        welcome_channels[interaction.guild_id] = channel.id

    else:
        welcome_channels[interaction.guild_id] = None

    # Ici j'enregistre les modifications
    with open("data/welcome_channel", "wb") as file:
        pickle.Pickler(file).dump(welcome_channels)

    if channel is not None:
        embed = discord.Embed(title="**:wave: | Bienvenue**",
                              description=f"Le salon de bienvenue est désormais {channel.mention} !",
                              color=discord.Color.green())

    else:
        embed = discord.Embed(title=":wave: | Bienvenue", description="Il n'y a désormais plus de salon de bienvenue !",
                              color=discord.Color.green())

    embed.set_thumbnail(url='https://cdn3.emoji.gg/emojis/6286_tada_animated.gif')
    await interaction.response.send_message(embed=embed, ephemeral=True)


# Cette ligne doit se trouver à la fin du fichier !
mod_commands = [{'name': 'salon-bienvenue', 'description': 'Cette commande définit un salon pour envoyer'
                                                           ' des messages de bienvenue !', 'func': welcome_command}]
# Elle sert à ajouter à "l'arbre" des commandes du Bot la commande crée :
# Pour cela il faut y mettre un nouveau dictionnaire et y mettre les clés suivantes avec ce qui leur correspond en paramètre :
#   - 'name' : Le nom de ta commande (Ex. say-goodbye)
#   - 'description' : La description de ta commande (Ex. Never Gonna Give You Up !)
#   - 'func' : la fonction qui contient ta commande (Ex. say_goodbye_command) PS. Ne pas mettre les parenthèses
#
# Ex. mod_commands = [{'name':'deuxième-test', 'description':'Hello World !', 'func':first_test},
#                     {'name':'salut', 'description':'Te dis salut !', 'func':hi_command}]

if __name__ == '__main__':
    import os
    os.system("python main.py")
