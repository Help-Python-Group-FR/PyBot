import discord
from discord import app_commands
import pickle

# Ici j'importe les fichiers où l'on a défini les commandes
import fun
import mod
import utils

# Je définis les variables essentiels du Bot ici :
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Ici j'ajoute les commandes définient dans les autres fichiers :
for command in fun.fun_commands:
    tree.command(name=command['name'], description=command['description'])(command['func'])
    print(f"Command {command['name']} has been set up with the func {command['func']} !")

for command in mod.mod_commands:
    tree.command(name=command['name'], description=command['description'])(command['func'])
    print(f"Command {command['name']} has been set up with the func {command['func']} !")

for command in utils.utils_commands:
    tree.command(name=command['name'], description=command['description'])(command['func'])
    print(f"Command {command['name']} has been set up with the func {command['func']} !")


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


@client.event
async def on_member_join(member: discord.Member):
    """
    Cette commande s'éxecute lorsqu'un membre rejoin le serveur :
        - Paramètre 'member' : Les informations du membre en question;
    """

    # Ici je récupère les données du fichier data/welcome_channel pour savoir où envoyer le message de bienvenue
    try:
        with open("data/welcome_channel", "rb") as file:
            welcome_channels = pickle.Unpickler(file).load()

        try:
            if welcome_channels[member.guild.id] is not None:
                welcome_embed = discord.Embed(title="**:tada: | Bienvenue !**",
                                              description=f"Bienvenue à {member.mention} sur"
                                                          f" **{member.guild.name}** ! Tu es le"
                                                          f" **{member.guild.member_count}**eme "
                                                          f"membre(s) !",
                                              color=discord.Color.red())

                welcome_embed.set_thumbnail(url='https://cdn3.emoji.gg/emojis/6286_tada_animated.gif')
                await client.get_channel(welcome_channels[member.guild.id]).send(embed=welcome_embed)

        except KeyError:
            pass

    except EOFError:
        pass

    try:
        with open("data/auto_roles", "rb") as file:
            auto_roles = pickle.Unpickler(file).load()

        for role_id in auto_roles[member.guild.id]:
            role = member.guild.get_role(role_id)
            await member.add_roles(role)

    except EOFError:
        pass


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

TOKEN = ""
print("Launch of the Client...")
client.run(TOKEN)
