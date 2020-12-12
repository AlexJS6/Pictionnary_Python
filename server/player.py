"""
Represents a player object on the server side
"""
from .game import Game


class Player(object):

    def __init(self, ip, name):
        """ 
        init the player object
        """
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0

    def set_game(self, game):
        """
        sets the players game association
        """
        self.game = game

    def update_score(self, x):
        """
        updates a player score
        """
        self.score += x
    
    def guess(self, wrd):
        """
        makes a player guess
        """
        return self.game.player_guess(self, wrd)

    def disconnect(self):
        """
        call to disconnect player
        """
        pass

    def get_ip(self):
        """
        gets player ip address
        """
        return self.ip

    def get_name(self):
        """
        gets player name
        """
        return self.name

    def get_score(self):
        """
        gets player score
        """
        return self.score

