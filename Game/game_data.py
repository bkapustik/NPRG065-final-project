from enum import Enum

from Game.player_event import PlayerEvent
from Cards.card_types import CardColorType, CardNumberType

class GameState(Enum):
    INITIAL = 0
    PLAYING = 1
    PLAYER_WON = 2
    PLAYER_LOST = 3
    PAUSED = 4

class GameData:
    cardsToTake: int
    numberOfPlayersSkippedByAce: int
    topHasBeenPlayed: bool

    colorToBePlayed: CardColorType
    displayColorOptions: bool
    playerHasFinished: bool
    gameState: GameState
    userInputReceived: bool

    def __init__(self):
        self.cardsToTake = 0
        self.numberOfPlayersSkippedByAce = 0
        self.topHasBeenPlayed = False
        self.colorToBePlayed = None
        self.displayColorOptions = False
        self.playerHasFinished = False
        self.gameState = GameState.INITIAL
        self.userInputReceived = False

    def evaluateCardNumberSeven(self):
        self.cardsToTake += 3

    def evaluateLeafBotCard(self):
        self.cardsToTake = 0

    def evaluateTopCard(self):
        self.topHasBeenPlayed = True

    def evaluateSkippingCard(self):
        self.numberOfPlayersSkippedByAce += 1

    def evaluateColorOptionCard(self, color: CardColorType):
        self.colorToBePlayed = color
        self.displayColorOptions = False
        self.userInputReceived = True   