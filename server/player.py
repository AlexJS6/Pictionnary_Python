"""
Represents a player object on the server side
"""

class Player(object):
    def __init(self, ip, name):
        self.ip = ip
        self.name = name
        self.score = 0

    def update_score(self, x):
        self.score += x
    
    def guess(self, string):
        pass

    def disconnect(self):
        pass

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

