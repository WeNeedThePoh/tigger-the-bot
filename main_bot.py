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
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "!3lines" in message.content and not game.state:
        game.start_game(message.author, message.mentions[0])
        await message.add_reaction("\U0001F44D")
        await message.channel.send(game.board_visual)
        print(f"{game.player1} vs {game.player2}")
        print(f"{game.board_visual}")

client.run(token)
