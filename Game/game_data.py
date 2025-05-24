from enum import Enum

from Game.player_event import PlayerEvent

class GameState(Enum):
    INITIAL = 0
    PLAYING = 1
    PLAYER_WON = 2
    PLAYER_LOST = 3
    PAUSED = 4

class GameData:
    cardsToTake = 0
    numberOfPlayersSkippedByAce = 0
    topHasBeenPlayed = False

    colorToBePlayed = None
    displayColorOptions = False
    playerHasFinished = False
    gameState: GameState = GameState.INITIAL
    playerEvent: PlayerEvent = PlayerEvent.NOT_PLAYING

    def evaluateCardNumberSeven(self):
        self.cardsToTake += 3
        self.playerEvent = PlayerEvent.HAS_TO_TAKE_A_CARD

    def evaluateLeafBotCard(self):
        self.cardsToTake = 0

    def evaluateTopCard(self):
        self.topHasBeenPlayed = True

    def evaluateSkippingCard(self):
        self.numberOfPlayersSkippedByAce += 1