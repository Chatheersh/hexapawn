import random
from hexapawn.environment.action import Action
from hexapawn.environment.coordinate import Coordinate
from hexapawn.environment.pawns import Pawns
from hexapawn.players.action_response import ActionResponse
from hexapawn.players.agent import Agent
from hexapawn.environment.board import Board
from hexapawn.players.no_action_exception import NoUserActionException


class UserAgent(Agent):
    def __init__(self):
        pass

    def can_move_up(self, coordinate: Coordinate, board: Board):

        x = coordinate.x
        y = coordinate.y + 1

        try:
            value = board.get_value(Coordinate(x, y))
        except Exception:
            return False

        if value == Pawns.UNOCCUPIED:
            return True
        else:
            return False

    def can_move_left_diagonal(self, coordinate: Coordinate, board: Board):
        x = coordinate.x - 1
        y = coordinate.y + 1

        try:
            value = board.get_value(Coordinate(x, y))
        except Exception:
            return False

        if value == Pawns.AGENT_PAWN:
            return True
        else:
            return False

    def can_move_right_diagonal(self, coordinate: Coordinate, board: Board):
        x = coordinate.x + 1
        y = coordinate.y + 1

        try:
            value = board.get_value(Coordinate(x, y))
        except Exception:
            return False

        if value == Pawns.AGENT_PAWN:
            return True
        else:
            return False

    def fetch_available_pawn_actions(self, board: Board):

        pawn_coordinates = {}

        for i in range(board.length):
            for j in range(board.length):
                c = Coordinate(i, j)
                actions = []
                if board.get_value(Coordinate(i, j)) == Pawns.USER_PAWN:
                    if self.can_move_up(c, board):
                        actions.append(Action.STRAIGHT)

                    if self.can_move_left_diagonal(c, board):
                        actions.append(Action.LEFT)

                    if self.can_move_right_diagonal(c, board):
                        actions.append(Action.RIGHT)

                    if actions:
                        pawn_coordinates[f"{c}"] = actions

        return pawn_coordinates

    def next_action(self, board: Board) -> ActionResponse:

        available_actions = self.fetch_available_pawn_actions(board)

        if len(available_actions) == 0:
            return ActionResponse()
        else:
            number_of_pawns = len(available_actions)

            random_number_index = random.randint(0, number_of_pawns - 1)
            keys = list(available_actions.keys())
            number_of_actions = len(
                available_actions[keys[random_number_index]])
            random_action_index = random.randint(0, number_of_actions - 1)

            x = int(keys[random_number_index].split(',')[0])
            y = int(keys[random_number_index].split(',')[1])

            return ActionResponse(Coordinate(x, y), available_actions[keys[random_number_index]][random_action_index])
