from Game.player import Player

class HumanPlayer(Player):
    def wantsCustomTurn(self):
        return True
    
    def tryChooseAColor(self):
        return False