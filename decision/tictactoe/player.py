class Player(object):
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return self.color

    def play(self, board):
        raise NotImplementedError
