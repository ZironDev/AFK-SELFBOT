import discord
from discord.ext import commands
import asyncio
import sqlite3


conn = sqlite3.connect('afk_status.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS afk_status
             (user_id TEXT PRIMARY KEY, afk_status INTEGER, reply TEXT)''')
conn.commit()
conn.close()

intents = discord.Intents.all()
prefix = "."
USER_TOKEN = ""
client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True, intents=intents)
client.remove_command('help')
client.load_extension('AfkCog')
    
@client.event
async def on_message(message):
    conn = sqlite3.connect('afk_status.db')
    c = conn.cursor()
    
    if message.author != client.user:
        c.execute("SELECT afk_status, reply FROM afk_status WHERE user_id=?", (str(message.author.id),))
        row = c.fetchone()
        if row and row[0] == 1:
            await message.channel.send("> **AFK. | Text me later**")
        elif not message.guild:  # Check if it's a direct message
            await message.channel.send("> **AFK. | Text me later**")
    
    await client.process_commands(message)

    
    
client.run(USER_TOKEN, bot=False)
