"""
Represents a round in the game, storing things like word, time, skips, drawing player, etc
"""
import time as t
from _thread import *
from .game import Game
from .chat import Chat

class Round(object):

    def __init__(self, word, player_drawing, players):
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = [] # Who got it correct
        self.skips = 0
        self.player_scores = {player : 0 for player in players} # puts a 0 in value for each player in the players list for this round -> 0
        self.time = 75
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def time_thread(self): # Runs ins thread to keep track of time!
        while self.time > 0:
            t.sleep(1) # sleeps 1s and decrements so thecountdown (75 -> 0)
            self.time -= 1
        self.end_round('Time is up!')

    def guess(self, player, wrd): # Returns bool if player got the guess correct 
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)

    def player_left(self, player): # removes player that left from scores, lists, tc
        if player in self.player_scores: # can we use object as dict key
            del player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player == self.player_drawing:
            self.end_round('Drawing player left!')

    def end_round(self, msg):
        pass