import discord
from game import Game

client = discord.Client()
token = open("to.txt","r").read();
game = Game()

@client.event
async def on_ready():
    user = client.user
    print(f"He have logged in as {user}")
    channel = client.get_channel(503819148254773258)

@client.event
async def on_message(message):
    if "!3lines" in message.content and not game.state:
        game.start(message.author, message.mentions[0])
        await message.channel.send(f"{game.player1.nick}: X vs {game.player2.nick}: O")
        await message.channel.send(f"```{game.board_visual}```")

client.run(token)
