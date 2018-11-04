class Game:
    ROW_DIFF = 22
    COLUMN_DIFF = 6
    row_matches = ["", "", ""]
    column_matches = ["", "", ""]
    diagonal_matches = ["", ""]

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

    def player_name(self, player):
        if player == 1:
            return self.player1.name.split("#")[0]
        else:
            return self.player2.name.split("#")[0]

    def make_visual_board(self):
        initial = 23
        self.row_matches = ["", "", ""]
        self.column_matches = ["", "", ""]
        self.diagonal_matches = ["", ""]
        board = list(self.board_visual)
        for index_r, row in enumerate(self.board):
            if index_r > 0:
                initial = initial + self.ROW_DIFF
            for index_c, column in enumerate(row):
                board[initial] = column
                initial = initial + self.COLUMN_DIFF
                self.row_matches[index_r] += column.strip()
                self.column_matches[index_c] += column.strip()
                if index_r - index_c == 0:
                    self.diagonal_matches[0] += column.strip()
                elif index_r + index_c == 2:
                    self.diagonal_matches[1] += column.strip()
        self.board_visual = "".join(board)

    def check_winner(self):
        if "XXX" in self.row_matches or "XXX" in self.column_matches or "XXX" in self.diagonal_matches:
            self.state = False
            return self.player1
        if "OOO" in self.row_matches or "OOO" in self.column_matches or "OOO" in self.diagonal_matches:
            self.state = False
            return self.player2
        else:
            return None

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
