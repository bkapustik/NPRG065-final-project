from Game.game_data import GameData
from Game.player import Player
from Cards.cards import Card
from Game.player_event import PlayerEvent
from Game.deck import Deck
from app_variable_value_helper import AppVariableValueHelper

import pygame

class GameManager:
    numberOfPlayers: int = 0
    playerOnTurnIndex: int = 0

    gameData: GameData
    playerHasFinished: bool = False
    userInputReceived: bool = True
    players: list[Player] = []
    deck: Deck
    
    colorSprites: pygame.sprite.Group
    cards: list[Card]
    appVariableValueHelper: AppVariableValueHelper

    def __init__(self, colorSprites: pygame.sprite.Group, gameData: GameData, appVariableValueHelper: AppVariableValueHelper):
        self.appVariableValueHelper = appVariableValueHelper
        self.numberOfPlayers = 4
        self.colorSprites = colorSprites
        self.gameData = gameData
        self.loadCards()
        self.restartGame()

    def playOneTurn(self):
        if (self.numberOfPlayers <= 1):
            return
        
        self.playerOnTurnIndex = self.playerOnTurnIndex % self.numberOfPlayers
        
        playerOnTurn: Player = self.players[self.playerOnTurnIndex]
        playerOnTurn.setOnTurn()
        if (playerOnTurn.wantsCustomTurn() or not self.userInputReceived):
            if (self.gameData.numberOfPlayersSkippedByAce > 0):
                self.playerEvent = PlayerEvent.BEING_SKIPPED
            elif (self.gameData.cardsToTake > 0):
                self.playerEvent = PlayerEvent.HAS_TO_TAKE_A_CARD
            else:
                self.playerEvent = PlayerEvent.PLAYING

    def restartGame(self):
        self.gameData = GameData()
        self.deck = Deck(self.cards)

    def loadCards(self):
        cardColors = ["Acorns", "Balls", "Green", "Heart"]
        cardNames = ["seven", "eight", "nine", "ten", "bot", "top", "king", "ace"]

        for color in cardColors:
            for name in cardNames:
                path = f"./Textures/Cards/{color}/{name}.jpg"
                card = Card(path, 0, 0, name, color, self.appVariableValueHelper)
                if (name == "seven"):
                    card.callback = self.evaluateCardWithNumberSeven
                elif (name == "top"):
                    card.callback = self.evaluateTopCard
                elif (name == "ace"):
                    card.callback = self.evaluateSkippingCard
                elif (name == "bot" and color == "Green"):
                    card.callback = self.evaluateLeafBotCard

    def evaluateCardWithNumberSeven(self):
        self.gameData.evaluateCardNumberSeven()

    def evaluateTopCard(self):
        self.gameData.evaluateTopCard()

    def evaluateSkippingCard(self):
        self.gameData.evaluateSkippingCard()

    def evaluateLeafBotCard(self):
        self.gameData.evaluateLeafBotCard()