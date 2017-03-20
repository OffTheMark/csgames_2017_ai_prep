import sys
import pathfinding


SMALL_MAZE = (
    '###S#;'
    '# # #;'
    '#   #;'
    '#F###'
)
SIMPLE_MAZE = (
    '############;'
    '#S         #;'
    '# ###### ###;'
    '# #        #;'
    '# # ###### #;'
    '# # #      #;'
    '#   ## ### #;'
    '# #    # ###;'
    '# ## #     #;'
    '# #  ##### #;'
    '#   ##    F#;'
    '############'
)
DEAD_ENDS_MAZE = (
    '############;'
    '#S         #;'
    '# ######## #;'
    '# #      # #;'
    '# # #### # #;'
    '# # #  ### #;'
    '# #      # #;'
    '# # #### # #;'
    '# #    # # #;'
    '# #### # ###;'
    '#      #  F#;'
    '############'
)
SNAKE_MAZE = (
    '############;'
    '#S #   #   #;'
    '#  # # # # #;'
    '#  # # # # #;'
    '#  # # # # #;'
    '#  # # # # #;'
    '#  # # # # #;'
    '#  # # # # #;'
    '#    #   # #;'
    '# ######## #;'
    '#         F#;'
    '############'
)
MAZES = [
    SMALL_MAZE,
    SIMPLE_MAZE,
    DEAD_ENDS_MAZE,
    SNAKE_MAZE
]
MAZE_NAMES = [
    "Small maze",
    "Simple maze",
    "Dead ends maze",
    "Snake maze"
]
ALGORITHM_NAMES = [
    "Breadth-first search",
    "A*",
    "Dijkstra"
]


def parse_list(maze_string):
    return [list(x) for x in maze_string.split(";")]


def format_solution(maze_list, path):
    for cell in path:
        symbol = maze_list[cell[0]][cell[1]]
        if symbol not in ["S", "F"]:
            maze_list[cell[0]][cell[1]] = "X"
    return maze_list


if __name__ == "__main__":
    print("Choose algorithm :")
    for i in range(len(MAZE_NAMES)):
        print("\t{} : {}".format(i, MAZE_NAMES[i]))
    maze_choice = int(sys.stdin.readline())
    print("Choose maze :")
    for i in range(len(ALGORITHM_NAMES)):
        print("\t{} : {}".format(i, ALGORITHM_NAMES[i]))
    algorithm_choice = int(sys.stdin.readline())

    maze_choice = maze_choice if maze_choice < len(MAZE_NAMES) else 0
    algorithm_choice = algorithm_choice if algorithm_choice < len(ALGORITHM_NAMES) else 0
    maze_string = MAZES[maze_choice]
    maze_list = parse_list(maze_string)
    algorithm_name = ALGORITHM_NAMES[algorithm_choice]
    maze_name = MAZE_NAMES[maze_choice]

    solver = None
    if algorithm_choice == 0:
        solver = pathfinding.BreadFirstSearchSolver(maze_list)
    elif algorithm_choice == 1:
        solver = pathfinding.AStarSolver(maze_list)
    elif algorithm_choice == 2:
        solver = pathfinding.DijkstraSolver(maze_list)

    path = solver.solve()
    directions = solver.get_directions(path)
    # directions = solution[0]
    # path = solution[1]
    maze_rows = [" ".join(row) for row in maze_list]
    solution_rows = [" ".join(row) for row in format_solution(maze_list, path)]

    print("")
    print('Algorithm : {}'.format(algorithm_name))
    print(
        'Maze : {}\n{}'.format(
            maze_name,
            "\n".join(maze_rows)
        )
    )
    print(
        'Solution :\n{}'.format(
            "\n".join(solution_rows)
        )
    )
    print(
        'Directions :\n{}'.format(
            ' '.join(directions)
        )
    )
    print(
        'Path :\n{}'.format(
            ' '.join(['{}'.format(x) for x in path])
        )
    )
