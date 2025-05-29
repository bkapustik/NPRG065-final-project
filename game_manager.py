from Game.game_data import GameData
from Game.player import Player
from Cards.cards import Card
from Game.player_event import PlayerEvent
from Game.game_data import GameState
from Game.deck import Deck
from app_variable_value_helper import AppVariableValueHelper
from Game.human_player import HumanPlayer
from Cards.color_card import CardColorType
from Cards.card_types import CardNumberType
from Game.computer_player import ComputerPlayer

import random
import pygame

class GameManager:
    numberOfPlayers: int
    playerOnTurnIndex: int

    gameData: GameData
    playerHasFinished: bool
    players: list[Player]
    humanPlayer: HumanPlayer
    deck: Deck
    
    colorSprites: pygame.sprite.Group
    cards: list[Card]
    appVariableValueHelper: AppVariableValueHelper

    def __init__(self, colorSprites: pygame.sprite.Group, gameData: GameData, appVariableValueHelper: AppVariableValueHelper):
        self.appVariableValueHelper = appVariableValueHelper
        self.numberOfPlayers = 4
        self.colorSprites = colorSprites
        self.gameData = gameData
        self.cards = []
        self.loadCards()
        self.playerOnTurnIndex = 0
        self.deck = None
        self.humanPlayer = None
        self.playerHasFinished = False
        self.players = []

    def playOneTurn(self):
        if not self.gameData.userInputReceived:
            return

        if (self.numberOfPlayers <= 1):
            return
        
        self.playerOnTurnIndex = self.playerOnTurnIndex % self.numberOfPlayers
        playerOnTurn: Player = self.players[self.playerOnTurnIndex]

        if (playerOnTurn == self.humanPlayer):
            self.gameData.userInputReceived = False
            return
        
        playedCard = playerOnTurn.tryPlayCard(self.deck.frontDeckCard)

        if playedCard is not None:
            self.evaluateComputerPlayerCard(playedCard)
            self.deck.addACard(playedCard, rotate=True)
        else:
            if self.gameData.cardsToTake > 0:
                playerOnTurn.takeCards(self.deck.getNCards(self.gameData.cardsToTake))
                self.gameData.cardsToTake = 0
            elif self.gameData.numberOfPlayersSkippedByAce > 0:
                self.gameData.numberOfPlayersSkippedByAce -= 1
            else:
                playerOnTurn.takeCards(self.deck.getNCards(1))

        if playerOnTurn.checkHasFinished():
            self.removeFinishedPlayer()
        else:
            self.playerOnTurnIndex += 1

    def removeFinishedPlayer(self):
        newPlayers = []
        for i in range(self.playerOnTurnIndex):
            newPlayers.append(self.players[i])
        for i in range(self.playerOnTurnIndex + 1, self.numberOfPlayers):
            newPlayers.append(self.players[i])
        self.numberOfPlayers -= 1
        self.players = newPlayers

    def evaluateComputerPlayerCard(self, card: Card):
        if card.number == CardNumberType.TOP:
            self.gameData.colorToBePlayed = self.getRandomColor()
            self.gameData.evaluateTopCard()
            return
        self.gameData.topHasBeenPlayed = False

        if card.number == CardNumberType.ACE:
            self.gameData.evaluateSkippingCard()
            return
        if card.number == CardNumberType.SEVEN:
            self.gameData.evaluateCardNumberSeven()
            return
        if card.number == CardNumberType.BOT and card.color == CardColorType.LEAF:
            self.gameData.evaluateLeafBotCard()
            return
        
    def getRandomColor(self) -> CardColorType:
        numberOfColors = 4
        colors = [CardColorType.ACORN, CardColorType.BELL, CardColorType.LEAF, CardColorType.HEART]
        randomIndex = random.randint(0, numberOfColors - 1)
        return colors[randomIndex]

    def render(self, screen: pygame.Surface):
        self.deck.displayedSprites.draw(screen)
        self.deck.frontDeckCardGroup.draw(screen)
        for player in self.players:
            player.displayedSprites.draw(screen)

    def restartGame(self, gameData: GameData):
        self.gameData = gameData
        self.gameData.gameState = GameState.PLAYING
        self.cards = []
        self.loadCards()
        self.deck = Deck(self.cards, self.appVariableValueHelper)
        self.numberOfPlayers = 4
        self.players = []
        firstCardPositions = [(75, 150), (self.appVariableValueHelper.screenWidth - 300, 150), (75, 400)]
        
        for i in range(self.numberOfPlayers - 1):
            self.players.append(ComputerPlayer(firstCardPositions[i], self.gameData))
        
        self.humanPlayer = HumanPlayer((100, self.appVariableValueHelper.screenHeight - 125), self.appVariableValueHelper)
        self.players.append(self.humanPlayer)

        self.playerOnTurnIndex = random.randint(0, self.numberOfPlayers - 1)
        for player in self.players:
            cardsForPlayer = self.deck.getNCards(5)
            player.takeCards(cardsForPlayer)
            
        if self.players[self.playerOnTurnIndex] != self.humanPlayer:
            self.gameData.userInputReceived = True
        
    def assignColor(self, color: str):
        if color == "Acorns":
            return CardColorType.ACORN
        if color == "Balls":
            return CardColorType.BELL
        if color == "Heart":
            return CardColorType.HEART
        return CardColorType.LEAF
    
    def assignNumber(self, number: str):
        if number == "seven":
            return CardNumberType.SEVEN
        if number == "eight":
            return CardNumberType.EIGH
        if number == "nine":
            return CardNumberType.NINE
        if number == "ten":
            return CardNumberType.TEN
        if number == "bot":
            return CardNumberType.BOT
        if number == "top":
            return CardNumberType.TOP
        if number == "king":
            return CardNumberType.KING
        return CardNumberType.ACE

    def loadCards(self):
        cardColors = ["Acorns", "Balls", "Green", "Heart"]
        cardNames = ["seven", "eight", "nine", "ten", "bot", "top", "king", "ace"]

        for colorName in cardColors:
            for name in cardNames:
                color = self.assignColor(colorName)
                cardNumber = self.assignNumber(name)

                frontImgPath = f"./Textures/Cards/{colorName}/{name}.jpg"
                cardBackImgPath = f"./Textures/CardBackSite/back.jpg"
                card = Card(cardBackImgPath, frontImgPath, 0, 0, color, cardNumber, self.appVariableValueHelper)
                if (cardNumber == CardNumberType.SEVEN):
                    card.cardClickCallBack = self.evaluateCardWithNumberSeven
                elif (cardNumber == CardNumberType.TOP):
                    card.cardClickCallBack = self.evaluateTopCard
                elif (cardNumber == CardNumberType.ACE):
                    card.cardClickCallBack = self.evaluateSkippingCard
                elif (cardNumber == CardNumberType.BOT and color == CardColorType.LEAF):
                    card.cardClickCallBack = self.evaluateLeafBotCard
                else:
                    card.cardClickCallBack = self.evaluateCard

                self.cards.append(card)

    def evaluateCardWithNumberSeven(self, card: Card):
        if not self.canPlayCard(card):
            return
        self.gameData.evaluateCardNumberSeven()
        self.evaluateCard(card)

    def evaluateTopCard(self, card: Card):
        if not self.canPlayCard(card):
            return
        self.gameData.evaluateTopCard()
        self.gameData.displayColorOptions = True
        self.humanPlayer.displayedSprites.remove(card)
        self.humanPlayer.cards.remove(card)

        self.deck.addACard(card)

    def evaluateSkippingCard(self, card: Card):
        if not self.canPlayCard(card):
            return
        self.gameData.evaluateSkippingCard()
        self.evaluateCard(card)

    def evaluateLeafBotCard(self, card: Card):
        if not self.canPlayCard(card):
            return
        self.gameData.evaluateLeafBotCard()
        self.evaluateCard(card)

    def evaluateCard(self, card: Card):
        if not self.canPlayCard(card):
            return
        self.humanPlayer.displayedSprites.remove(card)
        self.humanPlayer.cards.remove(card)

        self.gameData.colorToBePlayed = card.color
        self.gameData.userInputReceived = True
        self.playerOnTurnIndex += 1
        self.deck.addACard(card)

    def evaluateTakeCardButtonClick(self):
        if (not self.gameData.userInputReceived):
            if (self.gameData.cardsToTake > 0):
                self.humanPlayer.takeCards(self.deck.getNCards(self.gameData.cardsToTake))
                self.gameData.cardsToTake = 0
            elif self.gameData.numberOfPlayersSkippedByAce > 0:
                self.gameData.numberOfPlayersSkippedByAce -= 1
            else:
                self.humanPlayer.takeCards(self.deck.getNCards(1))
            self.gameData.userInputReceived = True
            self.playerOnTurnIndex += 1

    def canPlayCard(self, card: Card):
        if self.gameData.userInputReceived or self.gameData.displayColorOptions:
            return False
        
        colorToPlay = self.deck.frontDeckCard.color

        if self.gameData.topHasBeenPlayed:
            colorToPlay = self.gameData.colorToBePlayed
        
        if self.gameData.cardsToTake > 0:
            if card.number == CardNumberType.SEVEN:
                return True
            if card.number == CardNumberType.BOT and card.color == CardColorType.LEAF:
                return True
            return False
        
        if self.gameData.numberOfPlayersSkippedByAce > 0:
            if card.number == CardNumberType.ACE:
                return True
            return False
        
        if colorToPlay == card.color or self.deck.frontDeckCard.number == card.number or card.number == CardNumberType.TOP:
            return True
        
        return False