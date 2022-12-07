from dataclasses import dataclass

from hexapawn.environment.coordinate import Coordinate
from hexapawn.environment.action import Action


@dataclass
class ActionResponse:
    coordinate: Coordinate = None
    action: Action = None
