from pathfinding.solver import Solver


class DijkstraSolver(Solver):
    def solve(self):
        start = self.find(self.START)
        finish = self.find(self.FINISH)

        distances = {}
        predecessors = {}
        to_assess = self.maze_graph.keys()

        for node in self.maze_graph:
            distances[node] = float("inf")
            predecessors[node] = None

        labelled = []
        distances[start] = 0

        while len(labelled) < len(to_assess):
            still_in = {
                node: distances[node] for node in [node for node in to_assess if node not in labelled]
            }
            closest = min(still_in, key=distances.get)
            labelled.append(closest)

            for direction, neighbour in self.maze_graph[closest]:
                if distances[neighbour] > distances[closest] + 1:
                    distances[neighbour] = distances[closest] + 1
                    predecessors[neighbour] = closest

        path = [finish]
        while start not in path:
            path.append(predecessors[path[-1]])

        return [], path[::-1]
