from board import Board


class Game(object):
    def __init__(self, *players):
        self.players = list(players)
        self.board = Board()

    def play(self):
        while not self.board.winner() and not self.board.full():
            player = self.players.pop(0)
            player.play(self.board)
            self.players.append(player)

        if self.board.winner():
            print(self.board.winner().name, "wins!")
        else:
            print("Draw.")

        print(self.board)
