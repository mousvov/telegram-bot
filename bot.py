import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} - البوت شغال ✅")

@bot.command()
async def hello(ctx):
    await ctx.send(f"اهلا بيك يا {ctx.author.mention} ! البوت شغال 🔥")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == "hi":
        await message.channel.send("Hi bro 👋")
    await bot.process_commands(message)

bot.run(os.environ.get("MTU3NDI3MjA0NDg2NTE2NzUwMA.GLsxl9.yuRFTXPy3v5yyIf73IX8weYEliFwM8W6m_m-Xs"))
