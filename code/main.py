import discord
from discord.ext import commands

from time import sleep

prefix = ""
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
help_commands = {}


class MyEmbed:
	def __init__(self, ctx, title, description, color=discord.Color.dark_blue()):
		self.embed = discord.Embed(title=title, description=description, color=color)
		self.embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
		self.embed.set_footer(text="By this server :)")
		self.embed.set_image(url='https://cdn.discordapp.com/attachments/717821702180044862/729449197480181810/color_seperater_thingy.gif')

	def add_field(self, name, value, inline=False):
		self.embed.add_field(name=name, value=value, inline=inline)

	def set_thumbnail(self, url):
		self.embed.set_thumbnail(url=url)

	def set_footer(self, text, icon_url):
		self.embed.set_footer(text=text, icon_url=icon_url)

	def set_image(self, url):
		self.embed.set_image(url=url)


async def send_error(ctx, error):
	embed = discord.Embed(title=f":x: | {error}", color=discord.Color.dark_red())
	await ctx.message.delete()
	msg = await ctx.send(embed=embed)
	sleep(3)
	await msg.delete()


@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await send_error(ctx, "Commande inexistante !")


@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{prefix}help'))
	print("Ready !")

print("Launch of the client...")

token = ""
client.run(token)
