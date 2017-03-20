from pathfinding.solver import Solver
from collections import deque


class BreadFirstSearchSolver(Solver):
    """
    BFS solver implementation \n
    Based on http://bryukh.com/labyrinth-algorithms/
    """
    def solve(self):
        start = self.find(self.START)
        finish = self.find(self.FINISH)
        queue = deque([[start]])
        visited = set()
        while queue:
            path = queue.popleft()
            current = path[-1]
            if current == finish:
                return path
            if current in visited:
                continue
            visited.add(current)
            for neighbour in self.maze_graph[current]:
                queue.append(path + [neighbour])
        return []
