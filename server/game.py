"""
Handles operations related to game and connections
between player, board, chat and round
"""
from .player import Player
from .board import Board
from .round import Round
import random

class Game(object): # object, the parameter not needed

    def __init__(self, id, players, thread): 
        """
        When enough players, 
        a new game object is created and loop 
        through them and let them all play
        """
        self.id = id
        self.player = players
        self.words_used = []
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0 
        self.connected_thread = thread
        self.start_new_round() # If called in the methods need to call it here (every attribute)

    def start_new_round(self): 
        """
        Starts new round with a new word
        """
        self.round = Round(self.get_word(), self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()

    def player_guess(self, player, guess): 
        """
        Makes the player guess the word
        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player): 
        """
        Call to clean up objects when player disconnects
        """
        pass

    def skip(self): 
        """
        Increments the round skips if skips 
        are greater than threshold, new round
        """
        if self.round:
           new_round = self.round.skip()
           if new_round:
               self.round_ended()
        else:
            raise Exception('No round started yet!')

    def round_ended(self):
        """
        If the round ends call this
        """
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):
        """
        Calls update method on board
        """
        if not self.board:
            raise Exception('No board created')
        self.board.update(x, y, color)

    def end_game(self):
        """
        Ends the game
        """
        pass

    @staticmethod
    def get_word(): 
        """
        gets word that has not yet been used
        """
        with open("words.txt", "r") as f:
            words = f.readlines()
            r = random.randint(0, len(words))
            return words[r].strip()




