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

def set_afk(user_id, message):
    with open(db_file, "r") as f:
        data = json.load(f)
    data[str(user_id)] = message
    with open(db_file, "w") as f:
        json.dump(data, f)
    print("AFK status set successfully.")


        
        
intents = discord.Intents.all()
prefix = "."
USER_TOKEN = ""
client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True, intents=intents)
client.remove_command('help')
client.load_extension('DndCog')
    

@client.event
async def on_message(message):
    if message.author != client.user and not message.guild:
        with open(db_file, "r") as f:
            data = json.load(f)
            if str(client.user.id) in data and data[str(client.user.id)]["status"] == "on":
                await message.channel.send("**AFK. | Text me later**")
            else:
                return
    await client.process_commands(message)



client.run(USER_TOKEN, bot=False)


