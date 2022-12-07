from abc import abstractmethod
from hexapawn.environment.action import Action
from hexapawn.environment.board import Board
from hexapawn.environment.coordinate import Coordinate
from hexapawn.environment.pawns import Pawns
from hexapawn.players.percept import Percept


class Environment:
    def __init__(self, board: Board):
        self.board = board

    def apply_action(self, percept: Percept, pawn_coordinate: Coordinate, action: Action):

        new_coordinate = percept.apply_action(pawn_coordinate, action)

        if self.board.get_value(new_coordinate) == percept.get_enemy_pawn():
            percept.kills += 1

        self.board.set_value(pawn_coordinate, Pawns.UNOCCUPIED)
        self.board.set_value(new_coordinate, percept.get_pawn())

        if percept.end_of_board(self.board):
            percept.is_success = True

        self.print_state(action, percept)

        return percept

    def print_state(self, action: Action, percept: Percept):
        print(f"{percept.get_pawn_str()}'s turn - action: {action.name.lower()} is_success: {percept.is_success} is_failure: {percept.is_failure} kills: {percept.kills}")
