from Game.game_data import GameData
from Game.player import Player
from Cards.color_card import ColorCard
from Game.player_event import PlayerEvent

import pygame

class GameManager:
    numberOfPlayers: int = 0
    playerOnTurnIndex: int = 0

    gameData: GameData
    playerHasFinished: bool = False
    userInputReceived: bool = True
    players: list[Player] = []
    playerEvent: PlayerEvent = PlayerEvent.NOT_PLAYING
    
    colorSprites: pygame.sprite.Group

    def __init__(self, colorSprites: pygame.sprite.Group, gameData: GameData):
        self.numberOfPlayers = 4
        self.colorSprites = colorSprites

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
