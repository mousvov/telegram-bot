import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"البوت شغال باسم : {bot.user}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if channel:
        await channel.send(f"نورت السيرفر يا {member.mention} ❤️ اهلا بيك في سيرفرنا، اتمنى تنبسط معانا 🎉")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "بحب" in message.content:
        await message.channel.send("موسي سام ❤️")

    if "السلام عليكم" in message.content:
        await message.channel.send("وعليكم السلام ❤️")

    await bot.process_commands(message)

bot.run("MTU3NDI3MjA0NDg2NTE2NzUwMA.G95Oh9.1Vgts54_GXyfZ9Hw72OPKBfYQQ_nsZBk9ViJgM")
