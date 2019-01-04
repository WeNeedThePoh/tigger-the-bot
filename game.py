class Game:
    ROW_DIFF = 22
    COLUMN_DIFF = 6
    row_matches = ["", "", ""]
    column_matches = ["", "", ""]
    diagonal_matches = ["", ""]
    turn = dict()

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.state = False
        self.turn = ""
        self.moves = []
        self.board = []
        self.board_visual = ""


    def start(self, player1, player2):
        self.state = True
        self.player1 = player1
        self.player2 = player2
        self.turn["id"] = int(player1.id)
        self.turn["player"] = 0
        self.moves = ["X", "O"]
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
                self.move_plays_into_groups(index_r, index_c, column)
        self.board_visual = "".join(board)


    def move_plays_into_groups(self, row_index, column_index, column):
        """
        Group each move by column, row and diagonal, so it's easier to check for a winner
        """

        self.row_matches[row_index] += column.strip()
        self.column_matches[column_index] += column.strip()
        if row_index - column_index == 0:
            self.diagonal_matches[0] += column.strip()
        elif row_index + column_index == 2:
            self.diagonal_matches[1] += column.strip()


    def check_winner(self):
        if "XXX" in self.row_matches or "XXX" in self.column_matches or "XXX" in self.diagonal_matches:
            self.state = False
            return self.player1
        if "OOO" in self.row_matches or "OOO" in self.column_matches or "OOO" in self.diagonal_matches:
            self.state = False
            return self.player2
        else:
            return None

    def changeTurn(self):
        if self.turn["player"] == 0:
            self.turn["player"] = 1
            self.turn["id"] = int(self.player2.id)
        else:
            self.turn["player"] = 0
            self.turn["id"] = int(self.player1.id)


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
