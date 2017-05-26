from pathfinding.solver import Solver
from collections import deque


class DepthFirstSearchSolver(Solver):
    """
    DFS solver implementation \n
    Based on http://bryukh.com/labyrinth-algorithms/
    """
    def solve(self):
        start = self.find(self.START)
        finish = self.find(self.FINISH)
        stack = deque([[start]])
        visited = set()
        while stack:
            path = stack.pop()
            current = path[-1]
            if current == finish:
                return path
            if current in visited:
                continue
            visited.add(current)
            for neighbour in self.maze_graph[current]:
                stack.append(path + [neighbour])
        return []
