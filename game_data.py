class GameData:
    cardsToTake = 0
    numberOfPlayersSkippedByAce = 0
    topHasBeenPlayed = False

    colorToBePlayed = None

    def evaluateCardNumberSeven(self):
        self.cardsToTake += 3

    def evaluateLeafBotCard(self):
        self.cardsToTake = 0

    def evaluateTopCard(self):
        self.topHasBeenPlayed = True

    def evaluateSkippingCard(self):
        self.numberOfPlayersSkippedByAce += 1