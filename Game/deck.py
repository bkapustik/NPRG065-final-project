from Cards.cards import Card

import random
import pygame

class Deck:
    frontDeckCard: Card
    cards: list[Card]
    displayedSprites: pygame.sprite.Group

    def __init__(self):
        self.displayedSprites = pygame.sprite.Group()

    def shuffle(self):
        random.shuffle(self.cards)

    def getNCards(self, n: int):
        cardsToReturn = []

        for i in range(n):
            if (len(self.cards) > 0):
                card = self.cards.pop(0)
                cardsToReturn.append(card)
                self.displayedSprites.remove(card)

        return cardsToReturn
    
    def addACard(self, card: Card):
        self.cards.append(card)
        self.frontDeckCard = card

    # def changeShownCard(self):
        