from Game.player import Player

class ComputerPlayer(Player):
    def wantsCustomTurn(self):
        return False