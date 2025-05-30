from Cards.cards import Card
import pygame

class Player:
    """
    Base class representing a player in the game.

    Attributes:
        isOnTurn (bool): Indicates if it is currently this player's turn.
        hasFinished (bool): Indicates if the player has finished the game.
        firstCardPosition (tuple[float, float]): The position where the player's first card should be displayed.
        cards (list[Card]): The list of cards currently held by the player.
        displayedSprites (pygame.sprite.Group): Sprite group for displaying the player's cards.
    """

    isOnTurn: bool
    hasFinished: bool
    firstCardPosition: tuple[float, float]
    cards: list[Card]
    displayedSprites: pygame.sprite.Group

    def __init__(self, firstCardPosition: tuple[float, float]):
        """
        Initializes a Player instance.

        Args:
            firstCardPosition (tuple[float, float]): The position where the player's first card should be displayed.
        """
        self.firstCardPosition = firstCardPosition
        self.displayedSprites = pygame.sprite.Group()
        self.isOnTurn = False
        self.hasFinished = False
        self.cards = []

    def tryChooseAColor(self):
        """
        Handles the logic for choosing a color (if applicable).

        Returns:
            bool: False by default, can be overridden for color selection logic.
        """
        return False
    
    def tryPlayCard(self, topDeckCard: Card) -> Card | None:
        """
        Attempts to play a card based on the top card of the deck.

        Args:
            topDeckCard (Card): The card currently on top of the deck.

        Returns:
            Card | None: The card played, or None if no valid card is found.
        """
        return None
    
    def takeCards(self, cards: list[Card]):
        """
        Adds the given cards to the player's hand.

        Args:
            cards (list[Card]): The cards to add to the player's hand.
        """
        pass

    def checkHasFinished(self) -> bool:
        """
        Checks if the player has finished the game (i.e., has no cards left).

        Returns:
            bool: True if the player has finished, False otherwise.
        """
        if len(self.cards) == 0:
            self.hasFinished = True
        return self.hasFinished