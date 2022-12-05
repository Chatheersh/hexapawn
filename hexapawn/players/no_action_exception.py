class NoActionException(Exception):
    pass

class NoUserActionException(NoActionException):
    pass

class NoAgentActionException(NoActionException):
    pass