from enum import Enum


class Action(Enum):

    STRAIGHT = 1
    LEFT = 2
    RIGHT = 3

    @staticmethod
    def get_actions():
        return [Action.STRAIGHT, Action.LEFT, Action.RIGHT]