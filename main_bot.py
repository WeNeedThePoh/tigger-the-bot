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
    player = message.author
    command = list(msg_content)

    if "!3lines" in msg_content and game.state is False:
        game.start(player, message.mentions[0])
        await channel.send(f"{game.player_name(1)}: X vs {game.player_name(2)}: O")
        msg = await channel.send(f"```{game.board_visual}```")
        turn = await channel.send(f"{game.player_name(1)} your turn!")

    elif game.state is True and command[0] == "!" and len(command) == 3 and player.id == game.turn:
        row = int(command[1])
        column = int(command[2])

        if all(i in range(0,3) for i in [row, column]):
            if game.board[row][column] == " ":
                if game.player1.id == player.id:
                    game.board[row][column] = "X"
                    game.turn = game.player2.id
                elif game.player2.id == player.id:
                    game.board[row][column] = "O"
                    game.turn = game.player1.id

                game.make_visual_board()
                await msg.edit(content=f"```{game.board_visual}```")
                await message.delete()

                winner = game.check_winner()
                if winner is not None:
                    await turn.edit(content=f"{winner.nick} Won the game!")
                else:
                    player_name = client.get_user(game.turn).name.split("#")[0]
                    await turn.edit(content=f"{player_name} your turn!")

client.run(token)
