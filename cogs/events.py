import disnake
from disnake.ext import commands, tasks

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	# 	self.boost_stats.start()

	# @tasks.loop(minutes=5)
	# async def boost_stats(self):
	# 	await self.bot.wait_until_ready()
	# 	guild = self.bot.get_guild(817437132397871135)
	# 	lista = []
	# 	for i in guild.premium_subscribers:
	# 		lista.append(i.id)
	# 	await self.bot.boosters.update_one({"_id" : 0}, {"$set" : {"boosters" : lista}})
	# 	for user in lista:
	# 		info = await self.bot.players.find_one({"_id": user})
	# 		badges = info["badges"]
	# 		if "booster" in badges:
	# 			continue
	# 		new_badges = []
	# 		new_badges.append("booster")
	# 		for i in badges:
	# 			new_badges.append(i)
	# 		await self.bot.players.update_one({"_id" : user}, {"$set" : {"badges" : new_badges}})
	# 	print("Boosters have been updated")

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"logged in as {self.bot.user}")
		print(f"id: {self.bot.user.id}")
		print(f"guilds: {len(self.bot.guilds)}")
    
	@commands.Cog.listener()
	async def on_member_join(self, member):
		embed = disnake.Embed(color=0xe6b3ff)
		embed.set_thumbnail(member.guild.icon.url)
		embed.title=f"Welcome to {member.guild.name}"
		embed.set_author(name=str(member), icon_url=member.display_avatar)
		embed.set_footer(text=f"Thanks for joining, your the {member.guild.member_count}th member!", icon_url=self.bot.user.avatar.url)
		embed.description="We are a chill guild all about hedgehogs!\n• Be sure to read the <#813580269998047282>\n• You can chat with other people at <#813110873840549912>\n • share all your hedgehog pictures at <#813111777234518036>"
		cha = self.bot.get_channel(816878772816838666)
		await cha.send(content=f"* Welcome {member.mention}", embed=embed)
    

def setup(bot):
	bot.add_cog(Events(bot))