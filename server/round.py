"""
Represents a round in the game, storing things like word, time, skips, drawing player, etc
"""
import time as t
from _thread import *
from .game import Game
from .chat import Chat

class Round(object):

    def __init__(self, word, player_drawing, players, game):
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = [] # Who got it correct
        self.skips = 0
        self.player_scores = {player : 0 for player in players} # puts a 0 in value for each player in the players list for this round -> 0
        self.time = 75
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def skip(self): 
        """
        Tells if we gonna skip the round or not
        """
        self.skips += 1
        if self.skips > len(self.players) -2:
            return True
        
        return False

    def get_scores(self):
        """
        Returns all the player scores
        """
        return self.scores
    
    def get_score(self, player):
        """
        Gets a specific player's score
        """
        if player in self.player_scores:
            return self.player_scores[player]
        else:
            raise Exception('Player not in score list!')

    def time_thread(self): 
        """
        Runs in thread to keep track of time!
        """
        while self.time > 0:
            t.sleep(1) # sleeps 1s and decrements so thecountdown (75 -> 0)
            self.time -= 1
        self.end_round('Time is up!')

    def guess(self, player, wrd): 
        """
        Returns bool if player got the guess correct 
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)

    def player_left(self, player): 
        """
        removes player that left from scores, lists, tc
        """
        if player in self.player_scores: # can we use object as dict key
            del self.player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player == self.player_drawing:
            self.end_round('Drawing player left!')

    def end_round(self, msg):
        pass