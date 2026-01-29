import discord
import os
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await tree.sync()

@tree.command(name="hello", description="挨拶します")
async def start_command(interaction: discord.Interaction):
    await interaction.response.send_message("CI/CD成功です！")

client.run(TOKEN)
