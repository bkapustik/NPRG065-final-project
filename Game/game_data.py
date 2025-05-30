from enum import Enum

from Game.player_event import PlayerEvent
from Cards.card_types import CardColorType, CardNumberType

class GameState(Enum):
    """
    Enumeration for the possible states of the game.
    """
    INITIAL = 0
    PLAYING = 1
    PLAYER_WON = 2
    PLAYER_LOST = 3
    PAUSED = 4

class GameData:
    """
    Stores the current state and shared variables of the game.

    Attributes:
        cardsToTake (int): Number of cards the next player must take.
        numberOfPlayersSkippedByAce (int): Number of players to skip due to ACE.
        topHasBeenPlayed (bool): Whether the TOP card has been played.
        colorToBePlayed (CardColorType): The color to be played after a color change card.
        displayColorOptions (bool): Whether to display color selection options.
        playerHasFinished (bool): Whether the current player has finished.
        gameState (GameState): The current state of the game.
        userInputReceived (bool): Whether user input has been received.
    """

    cardsToTake: int
    numberOfPlayersSkippedByAce: int
    topHasBeenPlayed: bool

    colorToBePlayed: CardColorType
    displayColorOptions: bool
    playerHasFinished: bool
    gameState: GameState
    userInputReceived: bool

    def __init__(self):
        """
        Initializes the GameData object with default values.
        """
        self.cardsToTake = 0
        self.numberOfPlayersSkippedByAce = 0
        self.topHasBeenPlayed = False
        self.colorToBePlayed = None
        self.displayColorOptions = False
        self.playerHasFinished = False
        self.gameState = GameState.INITIAL
        self.userInputReceived = False

    def evaluateCardNumberSeven(self):
        """
        Evaluates the effect of playing a SEVEN card, increasing the cards to take by 3.
        """
        self.cardsToTake += 3

    def evaluateLeafBotCard(self):
        """
        Evaluates the effect of playing a LEAF BOT card, resetting the cards to take to 0.
        """
        self.cardsToTake = 0

    def evaluateTopCard(self):
        """
        Evaluates the effect of playing a TOP card, setting the topHasBeenPlayed flag.
        """
        self.topHasBeenPlayed = True

    def evaluateSkippingCard(self):
        """
        Evaluates the effect of playing a skipping card (ACE), incrementing the skip counter.
        """
        self.numberOfPlayersSkippedByAce += 1

    def evaluateColorOptionCard(self, color: CardColorType):
        """
        Evaluates the effect of playing a color option card, setting the color to be played and updating flags.

        Args:
            color (CardColorType): The color chosen by the player.
        """
        self.colorToBePlayed = color
        self.displayColorOptions = False
        self.userInputReceived = True