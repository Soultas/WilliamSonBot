import discord
import json
import asyncio
import time
import aiohttp
import subprocess
import sys
import requests
from discord.ext import commands

#TODO LIST:
#make stickbug cog with random things
#make movie module that will return list of random movies

Init_time = time.time()

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
			await ctx.send('extenbsion not available')


@bot.event
async def on_ready():
	print('Logged on as {0}!'.format(bot.user))
	print('message from {0.author}: {0.content}'.format(bot.message))




bot.run('Insert Bot Key')