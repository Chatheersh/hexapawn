from abc import abstractmethod
from hexapawn.environment.action import Action
from hexapawn.environment.board import Board
from hexapawn.environment.coordinate import Coordinate
from hexapawn.environment.pawns import Pawns


class Percept:

    def __init__(self, is_success: bool = False, is_failure: bool = False, kills: int = 0):
        self.is_success = is_success
        self.is_failure = is_failure
        self.kills = kills
        
    @abstractmethod
    def apply_action(self, coordinate: Coordinate, action: Action):
        pass

    @abstractmethod
    def get_pawn(self):
        pass

    @abstractmethod
    def get_pawn_str(self):
        pass

    @abstractmethod
    def end_of_board(self, board: Board):
        pass

    @abstractmethod
    def get_enemy_pawn(self):
        pass


class UserPercept(Percept):

    def apply_action(self, coordinate: Coordinate, action: Action):
        if action == Action.STRAIGHT:
            x = coordinate.x
            y = coordinate.y + 1
        elif action == Action.LEFT:
            x = coordinate.x - 1
            y = coordinate.y + 1
        elif action == Action.RIGHT:
            x = coordinate.x + 1
            y = coordinate.y + 1

        return Coordinate(x, y)

    def get_pawn(self):
        return Pawns.USER_PAWN

    def get_pawn_str(self):
        return "user"

    def end_of_board(self, board: Board):

        for i in range(0, board.length):
            if board.get_value(Coordinate(i, board.length - 1)) == Pawns.USER_PAWN:
                return True

        return False

    def get_enemy_pawn(self):
        return Pawns.AGENT_PAWN


class AiPercept(Percept):
    def apply_action(self, coordinate: Coordinate, action: Action):
        if action == Action.STRAIGHT:
            x = coordinate.x
            y = coordinate.y - 1
        elif action == Action.LEFT:
            x = coordinate.x + 1
            y = coordinate.y - 1
        elif action == Action.RIGHT:
            x = coordinate.x - 1
            y = coordinate.y - 1

        return Coordinate(x, y)

    def get_pawn(self):
        return Pawns.AGENT_PAWN

    def get_pawn_str(self):
        return "opponent"

    def end_of_board(self, board: Board):

        for i in range(0, board.length):
            if board.get_value(Coordinate(i, 0)) == Pawns.AGENT_PAWN:
                return True

        return False

    def get_enemy_pawn(self):
        return Pawns.USER_PAWN