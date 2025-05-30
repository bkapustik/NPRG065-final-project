from Game.player import Player
from Cards.card_types import CardColorType
from Cards.card_types import CardNumberType
from Cards.cards import Card
from Game.game_data import GameData

class ComputerPlayer(Player):
    """
    Represents a computer-controlled player in the game.
    Inherits from Player and implements logic for automated card selection and play.
    """
    gameData: GameData

    def __init__(self, firstCardPosition: tuple[float, float], gameData: GameData):
        """
        Initialize a ComputerPlayer.

        Args:
            firstCardPosition (tuple[float, float]): The position where the player's first card should be displayed.
            gameData (GameData): Reference to the shared game data.
        """
        super().__init__(firstCardPosition)
        self.gameData = gameData

    def returnCard(self, card: Card):
        """
        Removes the specified card from the player's hand and displayed sprites,
        updates the game state, and returns the card.

        Args:
            card (Card): The card to be played/returned.

        Returns:
            Card: The card that was played, or None if no card was played.
        """
        if (card is not None):
            self.displayedSprites.remove(card)
            self.cards.remove(card)
            self.gameData.colorToBePlayed = card.color
            self.userInputReceived = True
        return card

    def tryReturnCardOfColorAndNumber(self, cardcolor: CardColorType, cardnumber: CardNumberType) -> Card | None:
        """
        Attempts to find and play a card with the specified color and number.

        Args:
            cardcolor (CardColorType): The color to match.
            cardnumber (CardNumberType): The number to match.

        Returns:
            Card | None: The card played, or None if not found.
        """
        foundCard = None

        for card in self.cards:
            if card.color == cardcolor and card.number == cardnumber:
                foundCard = card
                break

        return self.returnCard(foundCard)
    
    def tryReturnCardOfColor(self, cardcolor: CardColorType) -> Card | None:
        """
        Attempts to find and play a card with the specified color.

        Args:
            cardcolor (CardColorType): The color to match.

        Returns:
            Card | None: The card played, or None if not found.
        """
        foundCard = None
        for card in self.cards:
            if card.color == cardcolor:
                foundCard = card
                break

        return self.returnCard(foundCard)
    
    def tryReturnCardOfNumber(self, cardnumber: CardNumberType) -> Card | None:
        """
        Attempts to find and play a card with the specified number.

        Args:
            cardnumber (CardNumberType): The number to match.

        Returns:
            Card | None: The card played, or None if not found.
        """
        foundCard = None

        for card in self.cards:
            if card.number == cardnumber:
                foundCard = card
                break

        return self.returnCard(foundCard)
    
    def tryCancelBeingSkipped(self) -> Card | None:
        """
        Attempts to play an ACE card to cancel being skipped.

        Returns:
            Card | None: The card played, or None if not found.
        """
        return self.tryReturnCardOfNumber(CardNumberType.ACE)
    
    def tryPlayCard(self, topDeckCard: Card) -> Card | None:
        """
        Determines and plays the best card according to the game state and top deck card.

        Args:
            topDeckCard (Card): The card currently on top of the deck.

        Returns:
            Card | None: The card played, or None if no valid card is found.
        """
        if self.gameData.cardsToTake > 0:
            return self.tryCancelTakingACard()
            
        if self.gameData.numberOfPlayersSkippedByAce > 0:
            return self.tryCancelBeingSkipped()
            
        colorToPlay = topDeckCard.color
        
        if self.gameData.topHasBeenPlayed:
            colorToPlay = self.gameData.colorToBePlayed

        card = self.tryReturnCardOfColorAndNumber(colorToPlay, CardNumberType.SEVEN)
        if card is not None:
            return card
        
        card = self.tryReturnCardOfColorAndNumber(colorToPlay, CardNumberType.ACE)
        if card is not None:
            return card
        
        card = self.tryReturnCardOfColor(colorToPlay)
        if card is not None:
            return card
        
        card = self.tryReturnCardOfNumber(topDeckCard.number)
        if card is not None:
            return card
        
        card = self.tryReturnCardOfNumber(CardNumberType.TOP)
        return card
    
    def tryCancelTakingACard(self) -> Card | None:
        """
        Attempts to play a SEVEN card to cancel taking cards, or a BOT-LEAF card as a fallback.

        Returns:
            Card | None: The card played, or None if not found.
        """
        card = self.tryReturnCardOfNumber(CardNumberType.SEVEN)
        if card is not None:
            return card
        
        card = self.tryReturnCardOfColorAndNumber(CardNumberType.BOT, CardColorType.LEAF)
        return card
    
    def takeCards(self, cards: list[Card]):
        """
        Adds the given cards to the player's hand and updates their display positions.

        Args:
            cards (list[Card]): The cards to add to the player's hand.
        """
        shiftXBy = 0
        self.displayedSprites.empty()
        for card in cards:
            self.cards.append(card)
        for card in self.cards:
            card.setPosition(self.firstCardPosition[0] + shiftXBy, self.firstCardPosition[1])
            shiftXBy += 10
            self.displayedSprites.add(card)