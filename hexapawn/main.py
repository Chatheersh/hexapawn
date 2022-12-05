from hexapawn.environment.board import Board
from hexapawn.environment.environment import Environment
from hexapawn.players.ai_agent import AiAgent
from hexapawn.players.no_action_exception import NoAgentActionException, NoUserActionException
from hexapawn.players.percept import AiPercept, UserPercept
from hexapawn.players.user_agent import UserAgent


def user_turn(user_agent: UserAgent, user_percept: UserPercept, environment: Environment, board: Board):
    coordinate, action = user_agent.next_action(board)
    return environment.apply_action(user_percept, coordinate, action)


def agent_turn(ai_agent: AiAgent, ai_percept: AiPercept, environment: Environment, board: Board):
    coordinate, action = ai_agent.next_action(board)
    return environment.apply_action(ai_percept, coordinate, action)


def episode(user_agent: UserAgent, user_percept: UserPercept, ai_agent: AiAgent, ai_percept: AiPercept, board: Board, environment: Environment):

    try:
        # fetch action
        user_percept = user_turn(user_agent, user_percept, environment, board)

        print("board state after user action:\n")
        print(board.draw())

        if not user_percept.is_success:
            ai_percept = agent_turn(ai_agent, ai_percept, environment, board)

            print("board state after ai action:\n")
            print(board.draw())
    except NoUserActionException:
        user_percept.is_failure = True
    except NoAgentActionException:
        ai_percept.is_failure = True

    if user_percept.is_success or ai_percept.is_success or user_percept.is_failure or ai_percept.is_failure:
        return
    else:
        return episode(user_agent, user_percept, ai_agent, ai_percept, board, environment)


def main():

    board = Board()
    enviroment = Environment(board)

    user_agent = UserAgent()
    user_percept = UserPercept()

    ai_agent = AiAgent()
    ai_percept = AiPercept()

    print("initial board state:\n")
    print(board.draw())

    episode(user_agent, user_percept, ai_agent, ai_percept, board, enviroment)


if __name__ == "__main__":
    main()
