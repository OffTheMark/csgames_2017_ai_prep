import sys
import decision


NODES_1 = range(33)
NODES_2 = range(22)
NODES = [
    NODES_1,
    NODES_2
]
CHILDREN_1 = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [6, 7],
    3: [8, 9],
    4: [10, 11],
    5: [12],
    6: [13, 14],
    7: [15],
    8: [16],
    9: [17, 18],
    10: [19, 20],
    11: [21, 22, 23],
    12: [24],
    13: [25],
    14: [26, 27],
    15: [28],
    16: [29],
    17: [30],
    18: [31]
}
CHILDREN_2 = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [6, 7],
    3: [8, 9],
    4: [10, 11],
    5: [12, 13],
    6: [14, 15],
    7: [16, 17],
    8: [18, 19],
    9: [20, 21]
}
CHILDREN = [
    CHILDREN_1,
    CHILDREN_2
]
VALUES_1 = dict.fromkeys(NODES_1, 0)
VALUES_1[19] = 5
VALUES_1[20] = 6
VALUES_1[21] = 7
VALUES_1[22] = 4
VALUES_1[23] = 5
VALUES_1[24] = 3
VALUES_1[25] = 6
VALUES_1[26] = 6
VALUES_1[27] = 9
VALUES_1[28] = 7
VALUES_1[29] = 5
VALUES_1[30] = 9
VALUES_1[31] = 8
VALUES_1[32] = 6
VALUES_2 = dict.fromkeys(NODES_1, 0)
VALUES_2[10] = 2
VALUES_2[11] = 4
VALUES_2[12] = 5
VALUES_2[13] = 6
VALUES_2[14] = 3
VALUES_2[15] = 0
VALUES_2[16] = 4
VALUES_2[17] = 5
VALUES_2[18] = 2
VALUES_2[19] = 1
VALUES_2[20] = 4
VALUES_2[21] = 3
VALUES = [
    VALUES_1,
    VALUES_2
]
DEPTHS = [
    5,
    4
]
ALGORITHMS = [
    "Minimax",
    "Minimax with alpha-beta pruning"
]


def create_node(index, children, values):
    node = decision.Node(values[index])
    if index in children:
        for children_index in children[index]:
            node.add_child(create_node(children_index, children, values))
    return node


if __name__ == "__main__":
    print("Choose graph :")
    print("Enter a number from 0 to {}".format(len(NODES) - 1))
    graph_choice = int(sys.stdin.readline())
    graph_choice = graph_choice if graph_choice < len(NODES) else 0

    print("Choose algorithm :")
    for i in range(len(ALGORITHMS)):
        print("\t{} : {}".format(i, ALGORITHMS[i]))
    algorithm_choice = int(sys.stdin.readline())
    algorithm_choice = algorithm_choice if algorithm_choice < len(ALGORITHMS) else 0

    root = create_node(0, CHILDREN[graph_choice], VALUES[graph_choice])

    best_value = 0
    if algorithm_choice == 0:
        best_value = decision.minimax(root, DEPTHS[graph_choice], True)
    elif algorithm_choice == 1:
        best_value = decision.alphabeta(root, DEPTHS[graph_choice], float("-inf"), float("+inf"), True)

    print("Graph : {}".format(graph_choice))
    print("Algorithm : {}".format(ALGORITHMS[algorithm_choice]))
    print(
        "Best value from graph {} of depth {} : {}".format(
            graph_choice,
            DEPTHS[graph_choice],
            best_value
        )
    )
