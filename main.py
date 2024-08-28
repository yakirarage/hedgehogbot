import os
import disnake
from dotenv import load_dotenv
from disnake.ext import commands
from disnake import AllowedMentions

load_dotenv()

description = """The most awesome hedgehog bot!!!"""

intents = disnake.Intents.all()

class HedgehogBot(commands.AutoShardedInteractionBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BotToken = os.getenv("TOKEN")
        self.activity = disnake.Game("with hedgehogs")
        self.help_command = None

    def load_all_cogs(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                self.load_extension(f"cogs.{filename[:-3]}")
                print(f"🔁 cogs.{filename[:-3]} is loaded and ready.")
        return


bot = HedgehogBot(
    intents=intents,
    owner_ids=[536538183555481601, 743948399270822029],
    allowed_mentions=AllowedMentions(
        users=True,
        everyone=True,
        roles=True,
        replied_user=True,
    )
)


bot.load_all_cogs()
bot.run(bot.BotToken)