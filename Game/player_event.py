from enum import Enum

class PlayerEvent(Enum):
    BEING_SKIPPED = 0
    HAS_TO_TAKE_A_CARD = 1
    PLAYING = 2
    NOT_PLAYING = 3