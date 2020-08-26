import discord

class myClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
	async def on_message(self, message):
		print('message from {0.author}: {0.content}'.format(message))

client = myClient()
client.run('NzMwNTkxODQ0OTMyNzgwMDgy.XwZurQ.eJn9_b7SUJGujfVZhMskIPQqIps')