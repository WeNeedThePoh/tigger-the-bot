class Game:
    ROW_DIFF = 22
    COLUMN_DIFF = 6

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.state = False
        self.turn = ""
        self.board = []
        self.board_visual = ""

    def start(self, player1, player2):
        self.state = True
        self.player1 = player1
        self.player2 = player2
        self.turn = player1.id
        self.reset_board()

    def make_visual_board(self):
        initial = 23
        board = list(self.board_visual)
        for index, row in enumerate(self.board):
            if (index > 0):
                initial = initial + self.ROW_DIFF
            for column in row:
                board[initial] = column
                initial = initial + self.COLUMN_DIFF
        self.board_visual = "".join(board)

    def reset_board(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        self.board_visual = """|-----------------|
|     |     |     |
|-----|-----|-----|
|     |     |     |
|-----|-----|-----|
|     |     |     |
|-----------------|"""
