import discord
import json
import requests

from discord.ext import commands
api_key="Insert your key here"

base_url="https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=hourly,daily&"

print(base_url)

class weather(commands.cog):
	def __init__(self,bot):
		self.bot=bot
	@bot.command()
	async def weather(self,ctx,*,city: str):
		city_name=city
		complete_url=base_url+"appid="+api_key+"&q="+city_name
		response = requests.get(complete_url)
		x = response.json()
		channel = ctx.message.channel
		if x['cod']!='404':
			async with channel.typing():
				y=x['main']
				current_temp=y['temp']
				current_temp_celcius = str(round(current_temp-273.15))
				current_pressure=y['pressure']
				current_humidity=y['humidity']
				z=x['weather']
				weather_description= z[0]['description']
		
			embed = discord.Embed(title=f"weather in {city_name}",
			color=ctx.guild.me.top_role.color,
			timestamp=ctx.message.created_at,)
			embed.add_field(name="description",value=f"**{weather_description}**",inline=False)
			embed.add_field(name="temperature(c)",value=f"**{current_temp_celcius}**°",inline=False)
			embed.add_field(name="Humidity%",value=f"**{current_humidity}%**",inline=False)
			embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**",inline=False)
			embed.set_thumbnail(url="https://i.bb.co/cMrsxdX/weather.png")
			embed.set_footer(text=f"Requested by {ctx.author.name}")

			await channel.send(embed=embed)
		else:
			await.channel.send('city not found')

def setup(bot):
	bot.add_cog(weather(bot))