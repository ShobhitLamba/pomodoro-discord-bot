import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents) 

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

active_sessions = {}

@bot.tree.command(name="start", description="Start a pomodoro session")
@app_commands.describe(
    num_of_sessions="Number of pomodoro sessions", 
    work_duration="Duration of work session in minutes", 
    break_duration="Duration of break session in minutes"
)
async def start(
    interaction: discord.Interaction, 
    num_of_sessions: int = 4, 
    work_duration: int = 25, 
    break_duration: int = 5
):
    """Start a pomodoro session with specified parameters."""
    user_id = interaction.user.id
    user_mention = interaction.user.mention
    if active_sessions.get(user_id):
        await interaction.response.send_message(f"{user_mention} You already have an active pomodoro session.")
        return
    active_sessions[user_id] = True
    await interaction.response.send_message(f"Starting a pomodoro session: {num_of_sessions} sessions of {work_duration} minutes of work followed by {break_duration} minutes of break.")
    for session in range(1, num_of_sessions + 1):
        if not active_sessions.get(user_id):
            await interaction.followup.send(f"{user_mention} Pomodoro session ended early.")
            return
        await interaction.followup.send(f"{user_mention} Session {session}: Work for {work_duration} minutes!")
        await asyncio.sleep(work_duration * 60)
        if session < num_of_sessions and active_sessions.get(user_id):
            await interaction.followup.send(f"{user_mention} Session {session}: Break for {break_duration} minutes!")
            await asyncio.sleep(break_duration * 60)
    active_sessions.pop(user_id, None)
    await interaction.followup.send(f"{user_mention} Pomodoro sessions complete! Great job!")

@bot.tree.command(name="end", description="End your active pomodoro session")
async def end(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_mention = interaction.user.mention
    if active_sessions.get(user_id):
        active_sessions.pop(user_id, None)
        await interaction.response.send_message(f"{user_mention} Your pomodoro session has been ended.")
    else:
        await interaction.response.send_message(f"{user_mention} You have no active pomodoro session.")

@bot.tree.command(name="session", description="Check if user has any active pomodoro session")
async def session(interaction: discord.Interaction):
    user_id = interaction.user.id
    user_mention = interaction.user.mention
    if active_sessions.get(user_id):
        await interaction.response.send_message(f"{user_mention} You have an active pomodoro session.")
    else:
        await interaction.response.send_message(f"{user_mention} You have no active pomodoro session.")

if __name__ == "__main__":
    import sys
    
    # Check for token
    DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    
    if not DISCORD_BOT_TOKEN:
        print("Error: DISCORD_BOT_TOKEN environment variable not set")
        print("\nTo set your token:")
        print("  export DISCORD_BOT_TOKEN='your-token-here'")
        print("\nOr create a .env file with:")
        print("  DISCORD_BOT_TOKEN=your-token-here")
        sys.exit(1)
    
    bot.run(DISCORD_BOT_TOKEN)