from hexapawn.environment.board import Board
from hexapawn.environment.environment import Environment
from hexapawn.players.ai_agent import AiAgent
from hexapawn.players.percept import AiPercept, UserPercept
from hexapawn.players.user_agent import UserAgent


def episode(user_agent: UserAgent, user_percept: UserPercept, ai_agent: AiAgent, ai_percept: AiPercept, board: Board, environment: Environment):

    # fetch action
    response = user_agent.next_action(board)

    if response.action:
        user_percept = environment.apply_action(user_percept, response.coordinate, response.action)
    else:
        user_percept.is_failure = True

    print("board state after user action:\n")
    print(board.draw())

    if not user_percept.is_success and not user_percept.is_failure:
        response = ai_agent.next_action(board)

        if response.action:
            ai_percept = environment.apply_action(ai_percept, response.coordinate, response.action)

            print("board state after ai action:\n")
            print(board.draw())

    if user_percept.is_success:
        print("User wins!")
        return
    elif user_percept.is_failure:
        print("User cannot make any more moves. Opponent wins!")
        return
    elif ai_percept.is_success:
        print("Opponent wins!")
        return
    elif ai_percept.is_failure:
        print("Opponent cannot make any more moves. User wins!")
        return
    else:
        return episode(user_agent, user_percept, ai_agent, ai_percept, board, environment)


def main():

    board = Board()
    enviroment = Environment(board)

    # instead of taking input from the user we will randomly select
    # moves for the user to take
    user_agent = UserAgent()
    user_percept = UserPercept()

    # the agent will use minimax to determine the best move
    ai_agent = AiAgent()
    ai_percept = AiPercept()

    episode(user_agent, user_percept, ai_agent, ai_percept, board, enviroment)      


if __name__ == "__main__":
    main()
