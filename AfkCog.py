import discord
from discord.ext import commands
import asyncio
import json
import os

from discord.ext import commands


db_file = "db.json"


if not os.path.exists(db_file):
    with open(db_file, "w") as f:
        json.dump({}, f)

def set_afk(user_id):
    with open(db_file, "r") as f:
        data = json.load(f)
    data[str(user_id)] = {"status": "on"}
    with open(db_file, "w") as f:
        json.dump(data, f)
    print("AFK status set successfully.")

def remove_afk(user_id):
    with open(db_file, "r") as f:
        data = json.load(f)
    data[str(user_id)] = {"status": "off"}
    with open(db_file, "w") as f:
        json.dump(data, f)
    print("AFK status removed successfully.")
        
class DndCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("[DEBUG]: AFK CMD COG CONNECTED")

    @commands.command()
    async def afk(self, ctx):
        if message.lower() == "off":
            remove_afk(ctx.author.id)
            await ctx.send(f"Removed Afk")
        else:
            set_afk(ctx.author.id)
            await ctx.send(f"Turned on Afk")  

def setup(bot):
    bot.add_cog(DndCog(bot))



