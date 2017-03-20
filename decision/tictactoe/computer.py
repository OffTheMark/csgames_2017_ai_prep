from player import Player


class Computer(Player):
    other = Player(None, None)

    def play(self, board):
        if not self.other.name:
            for i in range(9):
                x = board.get(i)
                if x and x != self:
                    self.other = x
                    break

        for I in range(1, -3, -1):
            for i in range(9):
                if not board.get(i):
                    b = board.copy()
                    b.play(i, self)
                    if self.minimax(b, False) > I:
                        board.play(i, self)
                        return

    def minimax(self, board, maximizing):
        if board.winner():
            return 1 if board.winner() == self else -1
        if board.full():
            return 0
        if maximizing:
            best = float("-inf")
            for move in board.available_moves():
                b = board.copy()
                b.play(move, self)
                best = max(best, self.minimax(b, False))
                # If move is a winning move for the computer
                if best == 1:
                    return best
            return best
        else:
            best = float("+inf")
            for move in board.available_moves():
                b = board.copy()
                b.play(move, self.other)
                best = min(best, self.minimax(b, True))
                # If move is a losing move for the opponent
                if best == -1:
                    return best
            return best


class AlphaBetaComputer(Player):
    other = Player(None, None)

    def play(self, board):
        if not self.other.name:
            for i in range(9):
                x = board.get(i)
                if x and x != self:
                    self.other = x
                    break

        for I in range(1, -3, -1):
            for i in range(9):
                if not board.get(i):
                    b = board.copy()
                    b.play(i, self)
                    if self.alphabeta(b, float("-inf"), float("+inf"), False) > I:
                        board.play(i, self)
                        return

    def alphabeta(self, board, alpha, beta, maximizing):
        if board.winner():
            return 1 if board.winner() == self else -1
        if board.full():
            return 0
        if maximizing:
            value = float("-inf")
            for move in board.available_moves():
                b = board.copy()
                b.play(move, self)
                value = max(value, self.alphabeta(b, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = float("+inf")
            for move in board.available_moves():
                b = board.copy()
                b.play(move, self.other)
                value = min(value, self.alphabeta(b, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value
