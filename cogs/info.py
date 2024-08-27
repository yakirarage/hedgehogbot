import disnake
from disnake.ext import commands
import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Info about our lovely guild!")
    async def guildinfo(self, inter):
        em = disnake.Embed(
            color=0xe6b3ff,
            description=f"""
            **Owner:** <@{inter.guild.owner_id}>
            **Members:** {inter.guild.member_count}/{inter.guild.max_members}
            **Guild ID:** {inter.guild.id}
            """
        )
        em.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

        await inter.send(embed=em)


    @commands.slash_command(description="Info about our lovely guild!")
    async def userinfo(self, inter, user:disnake.User=None):
        if user == None:
            user = inter.author
        em = disnake.Embed(
            color=0xe6b3ff,
            description=f"""
            **Tag:** {user.mention}
            **ID:** `{user.id}`
            **Username:** {user.name}
            **Nickname:** {user.display_name}
            **Created at:** {user.created_at}
            **Color:** {user.color}
            """
        )
        em.set_author(name=user.name, icon_url=user.display_avatar)
        em.set_thumbnail(url=user.display_avatar)

        await inter.send(embed=em)

def setup(bot):
	bot.add_cog(Help(bot))