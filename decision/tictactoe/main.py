from decision.tictactoe import Game, Human, AlphaBetaComputer


if __name__ == '__main__':
    Game(Human('X', "Human"), AlphaBetaComputer('O', "James")).play()
