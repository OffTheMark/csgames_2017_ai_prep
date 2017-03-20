from node import Node


def minimax(node, depth, maximize):
    if depth == 0 or not node.has_children():
        return node.value

    if maximize:
        best_value = float("-inf")
        for child in node.children:
            value = minimax(child, depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float("+inf")
        for child in node.children:
            value = minimax(child, depth - 1, True)
            best_value = min(best_value, value)
        return best_value


def alphabeta(node, depth, alpha, beta, maximize):
    if depth == 0 or not node.has_children():
        return node.value

    if maximize:
        value = float("-inf")
        for child in node.children:
            value = max(value, alphabeta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = float("+inf")
        for child in node.children:
            value = min(value, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value