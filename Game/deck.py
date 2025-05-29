from Cards.cards import Card
from app_variable_value_helper import AppVariableValueHelper

import random
import pygame

class Deck:
    frontDeckCard: Card
    cards: list[Card]
    displayedSprites: pygame.sprite.Group
    frontDeckCardGroup: pygame.sprite.Group
    
    displayedCardBaseX: float
    displayedCardBaseY: float

    displayedCardShiftBy: float
    frontDeckCardShiftBy: float

    def __init__(self, cards: list[Card], appVariableValueHelper: AppVariableValueHelper):
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
        random.shuffle(self.cards)
        self.changeShownCard()
        self.changeDisplayedSprites()

    def changeDisplayedSprites(self):
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
        cardsToReturn = []

        for i in range(n):
            if (len(self.cards) > 0):
                card = self.cards.pop(0)
                cardsToReturn.append(card)
                self.displayedSprites.remove(card)

        return cardsToReturn
    
    def addACard(self, card: Card, rotate: bool = False):
        oldFrontDeckCard = self.frontDeckCard
        oldFrontDeckCard.rotateCard()
        self.cards.append(oldFrontDeckCard)

        self.changeShownCard(card, rotate)
        self.changeDisplayedSprites()

    def changeShownCard(self, card: Card = None, rotate: bool = False):
        if card is not None:
            if rotate:
                card.rotateCard()
            self.frontDeckCard = card
            return
        if len(self.cards) > 0:
            self.frontDeckCard = self.cards.pop()
            self.frontDeckCard.rotateCard()