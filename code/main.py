from asyncio import sleep

from mod import help_commands as help_mod
from use import help_commands as help_use
from fun import help_commands as help_fun

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_components import create_choice, create_option

prefix = "."
bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefixes=prefix))
bot.remove_command('help')
slash = SlashCommand(bot, sync_commands=True)
help_commands = {"mod":help_mod, "fun":help_fun, "use":help_use}

def help_append(type: str, name: str, value: str):
	"""
	This function will add a command to the Help Message.
	
	Use it like that : help_append(type, name, value)
	
	type -> from wich category is the command (mod/fun/use)
	name -> the name of your command
	value -> The description of your command
	"""
	help_commands[type].append([name, value])


class MyEmbed:
	"""
	This class has the principals discord.Embed functions and more things :
		- It say on the top of the Embed who executed the command;
		- It put a rainbow bar at the end and say the credits
	"""
	
	def __init__(self, ctx: commands.Context, title: str, description: str, color=discord.Color.dark_blue()):
		self.ctx = ctx
		self.title = title
		self.description = description
		self.color = color
		self.embed = discord.Embed(title=title, description=description, color=color)
		self.embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
		self.embed.set_footer(text="By this server :)")
		self.embed.set_image(url='https://cdn.discordapp.com/attachments/717821702180044862/729449197480181810/color_seperater_thingy.gif')
	
	def __str__(self):
		return f'<discord.Embed: [ctx: {self.ctx} | title: {self.title} | descrtiption: {self.description} | color: {self.color}]>'

	def add_field(self, name, value, inline=False):
		self.embed.add_field(name=name, value=value, inline=inline)

	def set_thumbnail(self, url):
		self.embed.set_thumbnail(url=url)

	def set_footer(self, text, icon_url):
		self.embed.set_footer(text=text, icon_url=icon_url)

	def set_image(self, url):
		self.embed.set_image(url=url)

		
async def send_error(ctx: commands.Context, error: commands.errors):
	"""
	This function is used for send formated error messages !
	
	Use it like that : await send_error(ctx, error)
	
	ctx -> The context;
	error -> Your error (Ex. This player isn't on this server !)
	
	It will delete by his self in 3 seconds.
	"""
	embed = discord.Embed(title=f":x: | {error}", color=discord.Color.dark_red())
	await ctx.message.delete()
	msg = await ctx.send(embed=embed)
	sleep(3)
	await msg.delete()

@bot.event
async def on_ready():
	"""
	This function say Ready ! In the terminal when it's loaded and make the Bot status to Online.
	"""
	await bot.change_presence(status=discord.Status.online, activity=discord.Game(f'{prefix}help'))
	print("Ready !")
	print("Launch of the client...")
	
help_append('use', 'help', 'The help command.')
@bot.group() # by Artic
async def help(ctx: commands.Context):
	"""
	The help command. (all)
	"""
	embed = discord.Embed(title=f'Help [all] ({len(help_mod) + len(help_use) + len(help_fun)})', description=f'`{bot.command_prefix}help <class>`', color=discord.Color.blue())
	embed.add_field(name=':shield: Moderation', value=f'`{bot.command_prefix}help moderation`')
	embed.add_field(name=':books: Utility', value=f'`{bot.command_prefix}help utility`')
	embed.add_field(name=':joy: Fun', value=f'`{bot.command_prefix}help fun`')
	embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_footer(text="By this server :)")
	embed.set_image(url='https://cdn.discordapp.com/attachments/717821702180044862/729449197480181810/color_seperater_thingy.gif')
	return await ctx.reply(embed=embed)

@help.command() # by Artic
async def moderation(ctx: commands.Context):
	"""
	The help command. (moderation)
	"""
	embed = discord.Embed(title=f'Help [moderation] ({len(help_mod)})', description=f'`{bot.command_prefix}help moderation`', color=discord.Color.blue())
	for _command in help_mod:
		embed.add_field(name=f'{bot.command_prefix}{_command[0]}', value=_command[1])
	embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_footer(text="By this server :)")
	embed.set_image(url='https://cdn.discordapp.com/attachments/717821702180044862/729449197480181810/color_seperater_thingy.gif')
	return await ctx.reply(embed=embed)

@help.command() # by Artic
async def utility(ctx: commands.Context):
	"""
	The help command. (utility)
	"""
	embed = discord.Embed(title=f'Help [utility] ({len(help_use)})', description=f'`{bot.command_prefix}help utility`', color=discord.Color.blue())
	for _command in help_use:
		embed.add_field(name=f'{bot.command_prefix}{_command[0]}', value=_command[1])
	embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_footer(text="By this server :)")
	embed.set_image(url='https://cdn.discordapp.com/attachments/717821702180044862/729449197480181810/color_seperater_thingy.gif')
	return await ctx.reply(embed=embed)

@help.command() # by Artic
async def fun(ctx: commands.Context):
	"""
	The help command. (fun)
	"""
	embed = discord.Embed(title=f'Help [fun] ({len(help_fun)})', description=f'`{bot.command_prefix}help fun`', color=discord.Color.blue())
	for _command in help_fun:
		embed.add_field(name=f'{bot.command_prefix}{_command[0]}', value=_command[1])
	embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_footer(text="By this server :)")
	embed.set_image(url='https://cdn.discordapp.com/attachments/717821702180044862/729449197480181810/color_seperater_thingy.gif')
	await ctx.reply(embed=embed)
	return await ctx.message.delete()

token = "put the token here"
bot.run(token)
