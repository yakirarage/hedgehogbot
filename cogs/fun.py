import disnake
from disnake.ext import commands
import datetime
import random
import os

def get_random_image_path(folder_path, inter):
    try:
        files = os.listdir(folder_path)
        images = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        if not images:
            print("no images found in this specific folder")
            return None
        
        random_image = random.choice(images)
        random_image_path = os.path.join(folder_path, random_image)
        print(f"Here the random image path from the folder:")
        print(random_image_path)
        return random_image_path, random_image
    
    except Exception as e:
        print(f"An error occurred while selecting image randomly: {e}")
        return None

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="get a random but adorable hedgehog picture")
    async def hedgehog_pics(self, inter):
        await inter.response.defer()
        folder_path = "./images"
        if os.path.isdir(folder_path):
            random_IP, random_I = get_random_image_path(folder_path, inter)
        else:
            print(f" The specified folder does not exist: {folder_path}")

        file = disnake.File(random_IP, filename=random_I)
        em = disnake.Embed(
            color=0xe6b3ff,
        )
        em.set_thumbnail(url=f"attachment://{random_I}")
        await inter.send(file=file, embed=em)


def setup(bot):
	bot.add_cog(Fun(bot))