"""
Handles operations related to game and connections
between player, board, chat and round
"""

class Game(object): # object, the parameter not needed

    def __init__(self, id, players):
        self.id = id
        self.player = players
        self.words_used = []
        self.round = None
        self.board = None

    def player_guess(self, player, guess):
        pass

    def player_disconnected(self, player):
        pass

    def skip(self):
        pass

    def round_ended(self):
        pass

    def update_board(seld):
        pass



