import discord
import time
import sys
import json
import requests
import traceback
from discord.ext import commands

startup_extensions = ['cogs.weather']
#TODO LIST:
	#make stickbug cog with random things
	#make movie module that will return list of random movies
	#shutup nero whenever she talks
	#IMDbPY


Init_time = time.time()
api_key="Your api key here"

base_url="https://api.openweathermap.org/data/2.5/weather?"
bot = commands.AutoShardedBot(command_prefix='Dr ', description="Dr Botman")


@bot.command()
async def shutdown(ctx):
	await bot.logout()



@bot.command()
async def uptime(ctx):
	second=time.time() - Init_time
	minute, second = divmod(second, 60)
	hour, minute = divmod(minute, 60)
	day, hour = divmod(hour, 24)
	week, day = divmod(day, 7)
	await ctx.send("I've been online for %d weeks, %d days, %d hours, %d minutes, %d seconds" %(week,day,hour,minute,second))
@bot.command()
async def check(ctx,extension: str):
	extension = "Commands.{}".format(extension)
	if extension in extension and bot.load_extension(extension) == True:
		await ctx.send(extension,' is loaded')
	else:
		await ctx.send(extension,' not loaded')

@bot.command()
async def reload(ctx,extension: str):
	extension = "commands.{}".format(extension)
	await ctx.send('reloading {}..'.format(extension))
	if extension in extension:
		await ctx.send("reloading {}".format(extension))
		bot.unload_extension(extension)
		bot.load_extension(extension)
		await ctx.send('{} reloaded'.format(extension))
	else:
		await ctx.send("Extension isn't available")

@bot.command()
async def disable(ctx,extension: str):
	extension = "commands.{}".format(extension)
	if extension in extension:
		await ctx.send('Disabling {}'.format(extension))
		bot.unload_extension(extension)
		await ctx.send('{} disabled'.format(extension))
	else:
		await ctx.send("extension isn't available")

@bot.command()
async def enable(ctx,extension: str):
	extension = "commands.{}".format(extension)
	if extension in extension:
		await ctx.send("Loading {}..".format(extension))
		try:
			bot.load_extension(extension)
		except:
			await ctx.send(traceback.print_exc())
		else:
			await ctx.send('extension not available')


@bot.event
async def on_ready():
	print('Logged on as ',bot.user.name)
	game = discord.Game('Let me fix you up')
	await bot.change_presence(status=discord.Status.online, activity=game)
	for extension in startup_extensions:
		bot.load_extension(extension)

bot.run('Your api key here',bot=True,reconnect=True)
