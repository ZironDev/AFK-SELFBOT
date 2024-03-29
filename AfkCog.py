import discord
from discord.ext import commands
import asyncio
import sqlite3

class DndCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("[DEBUG]: DND LOGGER ONLINE")

    @commands.command(aliases=['afk'])
    async def dnd(self, ctx, arg1="on"):
        conn = sqlite3.connect('afk_status.db')
        c = conn.cursor()
        if arg1.lower() == "on":
            c.execute("INSERT OR REPLACE INTO afk_status (user_id, afk_status, reply) VALUES (?, ?, ?)", (str(ctx.author.id), 1, arg2))
            await ctx.message.delete()
            await ctx.send('> **Set Your DM AFK successfully**')
            await asyncio.sleep(3)
            await ctx.message.delete()
        elif arg1.lower() == "off":
            c.execute("DELETE FROM afk_status WHERE user_id=?", (str(ctx.author.id),))
            await ctx.message.delete()
            await ctx.send(f"> **Removed afk successfully for {ctx.author.name}**")
            await asyncio.sleep(3)
            await ctx.message.delete()
        conn.commit()
        conn.close()

def setup(bot):
    bot.add_cog(DndCog(bot))
