import discord
from discord import app_commands


@app_commands.checks.has_permissions(administrator=True)
@app_commands.rename(channel="salon", title="titre", announcement="annonce", thumbnail="icone", color="couleur")
@app_commands.describe(channel="Le salon dans lequel tu veux faire ton annonce.",
                       title="Le titre que tu veux donner à ton annonce.",
                       announcement="Ton annonce.",
                       thumbnail="L'icône que tu veux donner à ton annonce.",
                       image="L'image que tu veux donner à ton annonce.",
                       color="La couleur que tu veux donner à ton annonce.",
                       ping="Rôle que tu veux mentionner pour ton annonce.")
@app_commands.choices(color=[
    app_commands.Choice(name="bleu", value=1),
    app_commands.Choice(name="vert", value=2),
    app_commands.Choice(name="rouge", value=3)
])
async def announcement_command(interaction: discord.Interaction, channel: discord.TextChannel, title: str,
                               announcement: str,  color: app_commands.Choice[int], thumbnail: discord.Attachment = None,
                               image: discord.Attachment = None, ping: discord.Role = None):
    """
    Cette commande permet à un administrateur de faire une annonce dans un salon spécifié :
        - Paramètre 'channel' : Le salon où l'on veut poster l'annonce;
        - Paramètre 'announcement' : L'annonce a faire;
        - Paramètre 'thumbnail' (facultatif) : Icône affichée en haut à droite du message de type Embed;
        - Paramètre 'image' (facultatif) : Image ajoutée à l'annonce;
        - Paramètre 'title' : Titre de l'annonce;
        - Paramètre 'ping' : (facultatif) Rôle à notifier;
    """
    if color.value == 1:
        color = discord.Color.blue()
    elif color.value == 2:
        color = discord.Color.green()
    elif color.value == 3:
        color = discord.Color.red()

    embed = discord.Embed(title=f"**{title}**", description=announcement, color=color)
    if thumbnail is not None:
        embed.set_thumbnail(url=thumbnail.url)

    if image is not None:
        embed.set_image(url=image.url)

    embed.set_footer(icon_url=interaction.user.avatar.url, text=f"Annonce faite par {interaction.user.name} !")
    await channel.send(embed=embed)

    if ping is not None:
        if ping == interaction.guild.default_role:
            msg = await channel.send(interaction.guild.default_role)

        else:
            msg = await channel.send(ping.mention)

        await msg.delete()

    validation_embed = discord.Embed(title=":white_check_mark: | Ton annonce à bien été envoyée !",
                                     color=discord.Color.green())
    validation_embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/2121-announcement-badge.png")
    await interaction.response.send_message(embed=validation_embed, ephemeral=True)


# Cette ligne doit se trouver à la fin du fichier !
utils_commands = [{'name': 'annonce',
                   'description': 'Cette commande permet de créer un message d\'annonce ! (Permission réquise : Administrateur)',
                   'func': announcement_command}]
# Elle sert à ajouter à "l'arbre" des commandes du Bot la commande crée :
#
# Pour cela il faut y mettre un nouveau dictionnaire et y mettre les clés suivantes avec ce qui leur correspond en paramètre :
#   - 'name' : Le nom de ta commande (Ex. say-goodbye)
#   - 'description' : La description de ta commande (Ex. Never Gonna Give You Up !)
#   - 'func' : la fonction qui contient ta commande (Ex. say_goodbye_command) PS. Ne pas mettre les parenthèses
#
# Ex. utils_commands = [{'name':'deuxième-test', 'description':'Hello World !', 'func':first_test},
#                     {'name':'salut', 'description':'Te dis salut !', 'func':hi_command}]

if __name__ == '__main__':
    import os
    os.system("python main.py")
