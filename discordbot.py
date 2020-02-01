from discord.ext import commands
import os
import traceback

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
    
    if message.content.startwith == "ねむい":
        await message.channel.send(f"{message.author.mention}さん 寝ましょう")

    if message.content == "おはよう":
        await message.channel.send(f"{message.author.mention}さん おはよう")
    
    if message.content == "こんにちは":
        await message.channel.send(f"{message.author.mention}さん こんにちは")

    if message.content == "こんばんは":
        await message.channel.send(f"{message.author.mention}さん こんばんは")

    if message.content == "おやすみ":
        await message.channel.send(f"{message.author.mention}さん おやすみなさい")
    


@bot.command()
async def ping(ctx):
    await ctx.send('pong')



client.run(TOKEN)

bot.run(token)
