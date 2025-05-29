from Game.player import Player
from Cards.card_types import CardColorType
from Cards.card_types import CardNumberType
from Cards.cards import Card
from Game.game_data import GameData
import random

class ComputerPlayer(Player):
    gameData: GameData

    def __init__(self, firstCardPosition: tuple[float, float], gameData: GameData):
        super().__init__(firstCardPosition)
        self.gameData = gameData

    def returnCard(self, card: Card):
        if (card is not None):
            self.displayedSprites.remove(card)
            self.cards.remove(card)
            self.gameData.colorToBePlayed = card.color
            self.userInputReceived = True
        return card

    def tryReturnCardOfColorAndNumber(self, cardcolor: CardColorType, cardnumber: CardNumberType) -> Card | None:
        foundCard = None

        for card in self.cards:
            if card.color == cardcolor and card.number == cardnumber:
                foundCard = card
                break

        return self.returnCard(foundCard)
    
    def tryReturnCardOfColor(self, cardcolor: CardColorType) -> Card | None:
        foundCard = None
        for card in self.cards:
            if card.color == cardcolor:
                foundCard = card
                break

        return self.returnCard(foundCard)
    
    def tryReturnCardOfNumber(self, cardnumber: CardNumberType) -> Card | None:
        foundCard = None

        for card in self.cards:
            if card.number == cardnumber:
                foundCard = card
                break

        return self.returnCard(foundCard)
    
    def tryCancelBeingSkipped(self) -> Card | None:
        return self.tryReturnCardOfNumber(CardNumberType.ACE)
    
    def tryPlayCard(self, topDeckCard: Card) -> Card | None:
        if self.gameData.cardsToTake > 0:
            cancellingCard = self.tryCancelTakingACard()
            if cancellingCard is not None:
                return cancellingCard
            
        if self.gameData.numberOfPlayersSkippedByAce > 0:
            cancellingCard = self.tryCancelBeingSkipped()
            if cancellingCard is not None:
                return cancellingCard
            
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
        card = self.tryReturnCardOfNumber(CardNumberType.SEVEN)
        if card is not None:
            return card
        
        card = self.tryReturnCardOfColorAndNumber(CardNumberType.BOT, CardColorType.LEAF)
        return card
    
    def takeCards(self, cards: list[Card]):
        shiftXBy = 0
        self.displayedSprites.empty()
        for card in cards:
            self.cards.append(card)
        for card in self.cards:
            card.setPosition(self.firstCardPosition[0] + shiftXBy, self.firstCardPosition[1])
            shiftXBy += 10
            self.displayedSprites.add(card)