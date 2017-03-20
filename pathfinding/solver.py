

class Solver:
    WALL = "#"
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"
    START = "S"
    FINISH = "F"
    DIRECTIONS_MAP = {
        (0, -1): LEFT,
        (0, 1): RIGHT,
        (-1, 0): UP,
        (1, 0): DOWN
    }

    def __init__(self, maze_list):
        self.maze_list = maze_list
        self.maze_graph = self.parse_graph(self.maze_list)

    def parse_graph(self, maze_list):
        height = len(maze_list)
        width = len(maze_list[0]) if height else 0
        graph = {(i, j): [] for j in range(width) for i in range(height) if maze_list[i][j] != self.WALL}

        for row, column in graph.keys():
            if row < height - 1 and maze_list[row + 1][column] != self.WALL:
                graph[(row, column)].append((row + 1, column))
                graph[(row + 1, column)].append((row, column))
            if column < width - 1 and maze_list[row][column + 1] != self.WALL:
                graph[(row, column)].append((row, column + 1))
                graph[(row, column + 1)].append((row, column))
        return graph

    def get_directions(self, path):
        directions = []
        if path:
            current = path[0]
            for node in path[1:]:
                move = (node[0] - current[0], node[1] - current[1])
                directions.append(self.DIRECTIONS_MAP[move])
                current = node
        return directions

    def solve(self):
        pass

    def find(self, cell):
        for row, i in enumerate(self.maze_list):
            try:
                column = i.index(cell)
            except ValueError:
                continue
            return row, column
        return -1
