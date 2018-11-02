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
        await message.channel.send(f"{game.player1.nick} your turn!")

    elif game.state and len(message.content) == 3 and message.author.id == game.turn:
        play = list(message.content[1:])
        column = int(play[0])
        row = int(play[1])
        print(f"column: {column}   row: {row}")

        if 0 <= column < 3 and 0 <= row < 3:
            if game.board[column][row] == '-':
                if game.player1.id == message.author.id:
                    game.board[column][row] = 'X'
                    game.turn = game.player2.id
                elif game.player2.id + 1 == message.author.id:
                    game.board[column][row] = 'O'
                    game.turn = game.player1.id
        print(f"{game.board}")

client.run(token)
