from pathfinding.solver import Solver


class DijkstraSolver(Solver):
    def solve(self):
        start = self.find(self.START)
        finish = self.find(self.FINISH)

        visited = set()
        distances = dict.fromkeys(self.maze_graph.keys(), float("inf"))
        predecessors = dict.fromkeys(self.maze_graph.keys(), None)
        distances[start] = 0

        while visited != self.maze_graph.keys():
            shortest = min((set(distances.keys()) - visited), key=distances.get)
            if shortest == finish:
                break
            for neighbour in self.maze_graph[shortest]:
                if neighbour in visited:
                    continue
                new_cost = distances[shortest] + 1
                if new_cost < distances[neighbour]:
                    distances[neighbour] = new_cost
                    predecessors[neighbour] = shortest
            visited.add(shortest)

        path = []
        node = finish
        while node is not None:
            path = [node] + path
            node = predecessors[node]
        return path
