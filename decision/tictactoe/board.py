class Board(object):
    def __init__(self, inner=None):
        self.inner = inner or [None for x in range(9)]

    def play(self, position, player):
        assert(0 <= position < len(self.inner))
        if self.inner[position]:
            return False
        self.inner[position] = player
        return True

    def get(self, position):
        assert(0 <= position < len(self.inner))
        return self.inner[position]

    def available_moves(self):
        return [i for i in range(len(self.inner)) if not self.get(i)]

    def winner(self):
        return self._horizontal_winner() or self._vertical_winner() or self._diagonal_winner()

    def _horizontal_winner(self):
        I = self.inner
        for i in range(0, 9, 3):
            if I[i] and I[i] == I[i + 1] and I[i] == I[i + 2]:
                return I[i]

    def _vertical_winner(self):
        I = self.inner
        for i in range(3):
            if I[i] and I[i] == I[i+3] and I[i] == I[i+6]:
                return I[i]

    def _diagonal_winner(self):
        I = self.inner
        if I[0] and I[0] == I[4] and I[0] == I[8]:
            return I[0]
        if I[2] and I[2] == I[4] and I[2] == I[6]:
            return I[2]

    def full(self):
        return all(self.inner)

    def __str__(self):
        acc = []
        for i, n in enumerate(self.inner):
            if acc:
                acc.append(i % 3 and ' ' or '\n')
            acc.append(str(n or i + 1))
        return ''.join(acc)

    def copy(self):
        return Board(self.inner[:])
