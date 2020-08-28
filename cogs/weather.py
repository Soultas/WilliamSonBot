import discord
import json
import requests

from discord.ext import commands

api_key="4cdbd2001df9931c5dcc30ab2b574f3b"

base_url="https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=hourly,daily&"


class WeatherCog(commands.Cog):
	def __init__(self,bot):
		self.bot=bot

	@commands.command()
	async def convertc(ctx,c: int):
	#(0°C × 9/5) + 32 = 32°F
		h = c
		fahrenheit = (c * 9/5) + 32
		c = fahrenheit
		await ctx.send('C%d° = F%d°'%(h,c))

	@commands.command(name="convertf")
	async def convertf(ctx, f: int):
	#(32°F − 32) × 5/9 = 0°C
		h = f
		celcius = (f - 32) * 0.55555556
		f = celcius
		await ctx.send('F%d° = C%d°' %(h,f))

	@commands.command()
	async def weather(ctx,*,city: str):
		city_name=city
		complete_url=base_url+"&q="+city_name+"&appid="+api_key
		response = requests.get(complete_url)
		x = response.json()
		print(complete_url)
		print(x)
		channel = ctx.message.channel
		if x["cod"]!="404" and x['cod'] != '400':
			async with channel.typing():
				y  =   x['main']
				current_temp=y['temp']
				current_temp_celcius = str(round(current_temp-273.15))
				current_humidity=y['humidity']
				z=x['weather']
				weather_description= z[0]['description']
		
				embed = discord.Embed(title=f"Weather in {city_name}",
				color=ctx.guild.me.top_role.color,
				timestamp=ctx.message.created_at,)
				embed.add_field(name="Description",value=f"**{weather_description}**",inline=False)
				embed.add_field(name="Temperature(c)",value=f"**{current_temp_celcius}**°",inline=False)
				embed.add_field(name="Humidity%",value=f"**{current_humidity}%**",inline=False)
				embed.set_thumbnail(url="https://i.imgur.com/yfdyQun.png")
				embed.set_footer(text=f"Requested by {ctx.author.name}")
				await channel.send(embed=embed)
		else:
			await channel.send(city_name+' not found')

def setup(bot):
	bot.add_cog(WeatherCog(bot))