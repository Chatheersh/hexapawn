from environment.coordinate import Coordinate
from environment.pawns import Pawns


class Board:
    def __init__(self, length=4):
        # the chess board will always be a square
        # we will default to four
        self.length = length
        self.board = self._initialize()

    def _initialize(self):
        board = []

        for i in range(0, self.length):
            board.append([])
            for _ in range(0, self.length):
                board[i].append(Pawns.UNOCCUPIED)

        # Initialize player one's pawns
        # We will indicate them by 1s
        for i in range(0, self.length):
            board[self.length - 1][i] = Pawns.USER_PAWN

        # Intialize agent's pawns
        # We will indicate them by 2s
        for i in range(0, self.length):
            board[0][i] = Pawns.AGENT_PAWN

        return board

    def validate(self, coordinate: Coordinate):
        return coordinate.x < 0 or coordinate.x >= self.length\
            or coordinate.y < 0 or coordinate.y >= self.length

    def draw(self):
        str_board = ""

        for i in range(0, self.length):
            for j in range(0, self.length):
                str_board += f"{self.board[i][j]} "
            str_board += "\n"

        return str_board

    def get_value(self, coordinate: Coordinate):

        if self.validate(coordinate):
            raise Exception(f"coordinates {coordinate} are out of bounds")

        return self.board[self.length - coordinate.y - 1][coordinate.x]

    def set_value(self, coordinate: Coordinate, value: Pawns):
        self.board[self.length - coordinate.y - 1][coordinate.x] = value
