from enum import Enum

class CardColorType(Enum):
    LEAF = 0
    HEART = 1
    ACORN = 2
    BELL = 3

class CardNumberType(Enum):
    SEVEN = 0
    EIGH = 1
    NINE = 2
    TEN = 3

    BOT = 4
    TOP = 5
    KING = 6
    ACE = 7