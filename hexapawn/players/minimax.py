from copy import deepcopy
from hexapawn.environment.action import Action
from hexapawn.environment.board import Board
from hexapawn.environment.coordinate import Coordinate
from hexapawn.environment.pawns import Pawns
from hexapawn.players.action_response import ActionResponse

def find_best_move(board: Board):

    best_score = -1000
    best_move = Action.STRAIGHT
    best_coordinate = None

    for i in range(0, board.length):
        for j in range(0, board.length):
            c = Coordinate(i, j)
            value = board.get_value(c)

            if value == Pawns.AGENT_PAWN:
                # check up
                c_up = Coordinate(i, j - 1)
                if not board.validate(c_up) and board.get_value(c_up) == Pawns.UNOCCUPIED:
                    new_board = deepcopy(board)
                    new_board.set_value(c_up, Pawns.AGENT_PAWN)
                    new_board.set_value(c, Pawns.UNOCCUPIED)
                    score = minimax(new_board)
                    best_score = max(score, best_score)

                    if score == best_score:
                        best_move = Action.STRAIGHT
                        best_coordinate = c
                # check left
                c_left = Coordinate(i + 1, j - 1)
                if not board.validate(c_left) and board.get_value(c_left) == Pawns.USER_PAWN:
                    new_board = deepcopy(board)
                    new_board.set_value(c_left, Pawns.AGENT_PAWN)
                    new_board.set_value(c, Pawns.UNOCCUPIED)
                    score = minimax(new_board)
                    best_score = max(score, best_score)

                    if score == best_score:
                        best_move = Action.LEFT
                        best_coordinate = c
                # check right
                c_right = Coordinate(i - 1, j - 1)
                if not board.validate(c_right) and board.get_value(c_right) == Pawns.USER_PAWN:
                    new_board = deepcopy(board)
                    new_board.set_value(c_right, Pawns.AGENT_PAWN)
                    new_board.set_value(c, Pawns.UNOCCUPIED)
                    score = minimax(new_board)
                    best_score = max(score, best_score)

                    if score == best_score:
                        best_move = Action.RIGHT
                        best_coordinate = c

    return ActionResponse(best_coordinate, best_move)

def minimax(board: Board, is_user=False):
    
    scores = []

    for i in range(0, board.length):
        if board.get_value(Coordinate(i, 0)) == Pawns.USER_PAWN:
            return -1

    for i in range(0, board.length):
        if board.get_value(Coordinate(i, board.length - 1)) == Pawns.AGENT_PAWN:
            return -1

    if not is_user:

        scores.append(-1)
        for i in range(0, board.length):
            for j in range(0, board.length):
                c = Coordinate(i, j)
                value = board.get_value(c)

                if value == Pawns.AGENT_PAWN:
                    # check below
                    c_up = Coordinate(i, j - 1)
                    if not board.validate(c_up) and board.get_value(c_up) == Pawns.UNOCCUPIED:
                        new_board = deepcopy(board)
                        new_board.set_value(c_up, Pawns.AGENT_PAWN)
                        new_board.set_value(c, Pawns.UNOCCUPIED)
                        scores.append(minimax(new_board, True))

                    # check left
                    c_left = Coordinate(i + 1, j - 1)
                    if not board.validate(c_left) and board.get_value(c_left) == Pawns.USER_PAWN:
                        new_board = deepcopy(board)
                        new_board.set_value(c_left, Pawns.AGENT_PAWN)
                        new_board.set_value(c, Pawns.UNOCCUPIED)
                        scores.append(minimax(new_board, True))

                    # check right
                    c_right = Coordinate(i - 1, j - 1)
                    if not board.validate(c_right) and board.get_value(c_right) == Pawns.USER_PAWN:
                        new_board = deepcopy(board)
                        new_board.set_value(c_right, Pawns.AGENT_PAWN)
                        new_board.set_value(c, Pawns.UNOCCUPIED)
                        scores.append(minimax(new_board, True))
  
        return max(scores)
    else:
        scores.append(1)
        for i in range(0, board.length):
            for j in range(0, board.length):
                c = Coordinate(i, j)
                value = board.get_value(c)

                if value == Pawns.USER_PAWN:
                    # check up
                    c_up = Coordinate(i, j + 1)
                    if not board.validate(c_up) and board.get_value(c_up) == Pawns.UNOCCUPIED:
                        new_board = deepcopy(board)
                        new_board.set_value(c_up, Pawns.AGENT_PAWN)
                        new_board.set_value(c, Pawns.UNOCCUPIED)
                        scores.append(minimax(new_board, False))
                    # check left
                    c_left = Coordinate(i - 1, j + 1)
                    if not board.validate(c_left) and board.get_value(c_left) == Pawns.AGENT_PAWN:
                        new_board = deepcopy(board)
                        new_board.set_value(c_left, Pawns.AGENT_PAWN)
                        new_board.set_value(c, Pawns.UNOCCUPIED)
                        scores.append(minimax(new_board, False))
                    # check right
                    c_right = Coordinate(i + 1, j + 1)
                    if not board.validate(c_right) and board.get_value(c_right) == Pawns.AGENT_PAWN:
                        new_board = deepcopy(board)
                        new_board.set_value(c_right, Pawns.AGENT_PAWN)
                        new_board.set_value(c, Pawns.UNOCCUPIED)
                        scores.append(minimax(new_board, False))

        return min(scores)