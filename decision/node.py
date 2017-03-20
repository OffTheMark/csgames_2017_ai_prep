

class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, node):
        self.children.append(node)

    def has_children(self):
        return len(self.children) > 0
