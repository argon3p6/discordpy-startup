from discord.ext import commands
import os
import traceback
import re

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:
        return
    
    if re.search("[ねむい|眠い|眠たい]", message.content):
        await message.channel.send(f"{message.author.mention}さん 寝ましょう")

    if re.search("おはよう", message.content):
        await message.channel.send(f"{message.author.mention}さん おはよう")
    
    if re.search("こんばんは" or "こんばんわ", message.content):
        await message.channel.send(f"{message.author.mention}さん こんばんは")
    
    if re.search("こんにちは" or "こんにちわ", message.content):
        await message.channel.send(f"{message.author.mention}さん こんにちは")
    

"""
    if message.content == "おはよう":
        await message.channel.send(f"{message.author.mention}さん おはよう")
    
    if message.content == "こんにちは":
        await message.channel.send(f"{message.author.mention}さん こんにちは")

    if message.content == "こんばんは":
        await message.channel.send(f"{message.author.mention}さん こんばんは")

    if message.content == "おやすみ":
        await message.channel.send(f"{message.author.mention}さん おやすみなさい")
""" 


@bot.command()
async def ping(ctx):
    await ctx.send('pong')




bot.run(token)
