import discord
from game import Game

client = discord.Client()
token = open("to.txt","r").read();
game = Game()
msg = ""
turn = ""

@client.event
async def on_ready():
    user = client.user
    print(f"He have logged in as {user}")
    channel = client.get_channel(503819148254773258)

@client.event
async def on_message(message):
    global msg
    global turn
    channel = message.channel
    msg_content = message.content

    if "!3lines" in msg_content and game.state is False:
        game.start(message.author, message.mentions[0])
        await channel.send(f"{game.player1.nick}: X vs {game.player2.nick}: O")
        msg = await channel.send(f"```{game.board_visual}```")
        turn = await channel.send(f"{game.player1.nick} your turn!")

    elif game.state is True and len(msg_content) == 3 and message.author.id == game.turn:
        move = list(msg_content[1:])
        row = int(move[0])
        column = int(move[1])

        if 0 <= row < 3 and 0 <= column < 3:
            if game.board[row][column] == " ":
                if game.player1.id == message.author.id:
                    game.board[row][column] = "X"
                    game.turn = game.player2.id
                    game.make_visual_board()
                    await turn.edit(content=f"{game.player2.nick} your turn!")
                elif game.player2.id == message.author.id:
                    game.board[row][column] = "O"
                    game.turn = game.player1.id
                    game.make_visual_board()
                    await turn.edit(content=f"{game.player1.nick} your turn!")

                await msg.edit(content=f"```{game.board_visual}```")

client.run(token)
