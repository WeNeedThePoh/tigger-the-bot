class Game:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.state = False
        self.turn = ""
        self.board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
            ]
        self.board_visual = """
            |-----------------|
            |     |     |     |
            |-----|-----|-----|
            |     |     |     |
            |-----|-----|-----|
            |     |     |     |
            |-----------------|"""

    def start(self, player1, player2):
        self.state = True
        self.player1 = player1
        self.player2 = player2
        self.turn = player1.id
