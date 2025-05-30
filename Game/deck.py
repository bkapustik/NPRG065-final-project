from Cards.cards import Card
from app_variable_value_helper import AppVariableValueHelper

import random
import pygame

class Deck:
    """
    Represents the deck of cards in the game, including the draw pile and the front (top) card.

    Attributes:
        frontDeckCard (Card): The card currently shown on top of the deck.
        cards (list[Card]): The list of cards currently in the deck (draw pile).
        displayedSprites (pygame.sprite.Group): Sprites for cards in the deck.
        frontDeckCardGroup (pygame.sprite.Group): Sprite group for the front card.
        displayedCardBaseX (float): X position for the first card in the deck.
        displayedCardBaseY (float): Y position for the cards in the deck.
        displayedCardShiftBy (float): Horizontal shift between cards in the deck.
        frontDeckCardShiftBy (float): Additional shift for the front card.
    """

    frontDeckCard: Card
    cards: list[Card]
    displayedSprites: pygame.sprite.Group
    frontDeckCardGroup: pygame.sprite.Group
    
    displayedCardBaseX: float
    displayedCardBaseY: float

    displayedCardShiftBy: float
    frontDeckCardShiftBy: float

    def __init__(self, cards: list[Card], appVariableValueHelper: AppVariableValueHelper):
        """
        Initializes the Deck with a list of cards and app variable helper.

        Args:
            cards (list[Card]): The initial list of cards for the deck.
            appVariableValueHelper (AppVariableValueHelper): Helper for app-wide variables.
        """
        self.displayedCardShiftBy = 20
        self.frontDeckCardShiftBy = 50
        self.cards = []
        self.frontDeckCard = None
        self.displayedCardBaseY = appVariableValueHelper.screenHeight - 400
        self.displayedCardBaseX = 300
        self.displayedSprites = pygame.sprite.Group()
        self.frontDeckCardGroup = pygame.sprite.Group()
        for card in cards:
            self.cards.append(card)
        self.shuffle()

    def shuffle(self):
        """
        Shuffles the deck and updates the shown and displayed cards.
        """
        random.shuffle(self.cards)
        self.changeShownCard()
        self.changeDisplayedSprites()

    def changeDisplayedSprites(self):
        """
        Updates the positions and sprite groups for all cards in the deck and the front card.
        """
        self.displayedSprites.empty()
        shiftedBy = self.displayedCardBaseX
        for card in self.cards:
            card.setPosition(shiftedBy, self.displayedCardBaseY)
            shiftedBy += self.displayedCardShiftBy
            self.displayedSprites.add(card)
        self.frontDeckCard.setPosition(shiftedBy + self.frontDeckCardShiftBy, self.displayedCardBaseY)
        self.frontDeckCardGroup.empty()
        self.frontDeckCardGroup.add(self.frontDeckCard)

    def getNCards(self, n: int):
        """
        Removes and returns n cards from the top of the deck.

        Args:
            n (int): Number of cards to draw.

        Returns:
            list[Card]: The drawn cards.
        """
        cardsToReturn = []

        for i in range(n):
            if (len(self.cards) > 0):
                card = self.cards.pop(0)
                cardsToReturn.append(card)
                self.displayedSprites.remove(card)

        return cardsToReturn
    
    def addACard(self, card: Card, rotate: bool = False):
        """
        Adds a card to the deck, rotating the previous front card and updating the display.

        Args:
            card (Card): The card to add as the new front card.
            rotate (bool): Whether to rotate the card when adding.
        """
        oldFrontDeckCard = self.frontDeckCard
        oldFrontDeckCard.rotateCard()
        self.cards.append(oldFrontDeckCard)

        self.changeShownCard(card, rotate)
        self.changeDisplayedSprites()

    def changeShownCard(self, card: Card = None, rotate: bool = False):
        """
        Changes the card shown on top of the deck.

        Args:
            card (Card, optional): The card to show. If None, pops the last card from the deck.
            rotate (bool): Whether to rotate the card when showing.
        """
        if card is not None:
            if rotate:
                card.rotateCard()
            self.frontDeckCard = card
            return
        if len(self.cards) > 0:
            self.frontDeckCard = self.cards.pop()
            self.frontDeckCard.rotateCard()