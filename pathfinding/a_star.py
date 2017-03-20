from pathfinding.solver import Solver
from heapq import heappop, heappush
from math import sqrt


class AStarSolver(Solver):
    def manhattan_distance(self, cell, finish):
        return abs(cell[0] - finish[0]) + abs(cell[1] - finish[1])

    def euclidean_distance(self, cell, finish):
        return sqrt((cell[0] - finish[0])**2 + (cell[1] - finish[1])**2)

    def solve(self):
        start = self.find(self.START)
        finish = self.find(self.FINISH)
        priority_queue = []
        heappush(
            priority_queue,
            (
                0 + self.manhattan_distance(start, finish),
                0,
                [start]
            )
        )
        visited = set()
        while priority_queue:
            element = heappop(priority_queue)
            cost = element[1]
            path = element[2]
            current = path[-1]
            if current == finish:
                return path
            if current in visited:
                continue
            visited.add(current)
            for neighbour in self.maze_graph[current]:
                heappush(
                    priority_queue,
                    (
                        cost + self.manhattan_distance(neighbour, finish),
                        cost + 1,
                        path + [neighbour]
                    )
                )
        return []
