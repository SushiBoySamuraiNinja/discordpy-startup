import discord
import os


token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('testがログインしました')


@client.event
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

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)