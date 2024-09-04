import disnake
import time
from disnake.ext import commands, tasks

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"logged in as {self.bot.user}")
		print(f"id: {self.bot.user.id}")
		print(f"guilds: {len(self.bot.guilds)}")
		time.sleep(3)
		cha = self.bot.get_channel(1280679279213940827)
		await cha.send(content="Bot is up and running!")
    
	@commands.Cog.listener()
	async def on_member_join(self, member):
		embed = disnake.Embed(color=0xe6b3ff)
		embed.set_thumbnail(member.guild.icon.url)
		embed.set_author(name=F"Welcome {member.name} to {member.guild.name}!", icon_url=member.display_avatar)
		embed.set_footer(text=f"Thanks for joining, you’re the {member.guild.member_count}th member!", icon_url=self.bot.user.avatar.url)
		embed.description="Welcome to the guild! Check out our emojis and feel free to introduce yourself <#814598536368226315>"
		cha = self.bot.get_channel(816878772816838666)
		await cha.send(content=f"* Welcome {member.mention}", embed=embed)

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		cha = self.bot.get_channel(813264746815684649)
		await cha.send(content=f"**{member.name}**`{member.id}` left :(")

def setup(bot):
	bot.add_cog(Events(bot))