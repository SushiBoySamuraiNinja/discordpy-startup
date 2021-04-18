from discord.ext import commands
import discord
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # あっははあ
    if message.content == "!testjoin":
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return

        await message.author.voice.channel.connect()
        await message.channel.send("接続しました。")
    # leaveする
    elif message.content == "!testleave":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return

        # 切断する
        await message.guild.voice_client.disconnect()

        await message.channel.send("切断しました。")

    if message.content == "!testplay":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return
        message.guild.voice_client.play(discord.FFmpegPCMAudio("test.mp3"))

    # 「/test」と発言したら「にゃーん」が返る処理
    if message.content == '/test':
        await message.channel.send('にゃーん')

bot.run(token)
