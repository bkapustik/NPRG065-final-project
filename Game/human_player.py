from Game.player import Player
from Cards.cards import Card

class HumanPlayer(Player):
    """
    Represents a human player in the game.

    Inherits from Player and implements logic specific to human interaction.
    """

    def __init__(self, firstCardPosition: tuple[float, float], appVariableValueHelper):
        """
        Initializes a HumanPlayer instance.

        Args:
            firstCardPosition (tuple[float, float]): The position where the player's first card should be displayed.
            appVariableValueHelper: Helper for application-wide variables.
        """
        super().__init__(firstCardPosition)

    def tryChooseAColor(self):
        """
        Handles the logic for choosing a color (if applicable).

        Returns:
            bool: False by default, can be overridden for color selection logic.
        """
        return False
    
    def takeCards(self, cards: list[Card]):
        """
        Adds the given cards to the player's hand, rotates them face up, and updates their display positions.

        Args:
            cards (list[Card]): The cards to add to the player's hand.
        """
        shiftXBy = 0
        self.displayedSprites.empty()
        for card in cards:
            card.rotateCard()
            self.cards.append(card)
        for card in self.cards:
            card.setPosition(self.firstCardPosition[0] + shiftXBy, self.firstCardPosition[1])
            shiftXBy += 125
            self.displayedSprites.add(card)