from player import Player


class Human(Player):
    def play(self, board):
        print(board)
        i = 0
        while i < 1 or i > 9 or board.get(i - 1):
            i = raw_input(self.name + " : ")
            i = i.isdigit() and int(i) or 0
        board.play(i - 1, self)
