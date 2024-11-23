import disnake
import asyncio
from disnake.ext import commands
import datetime
import random
import os

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="purge set amount of messages")
    async def purge(self, inter, amount: int):
        if amount > 100:
            await inter.send("You can purge up to max `100` message at a time.")
            return
            
        await inter.channel.purge(limit=amount + 1)

        await inter.response.defer()
        await inter.send(f"Purged `{amount}` messages!")


def setup(bot):
	bot.add_cog(Moderation(bot))