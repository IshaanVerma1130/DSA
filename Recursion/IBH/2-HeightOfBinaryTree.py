class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


def CalcHeight(Node):
    if Node == None:
        return 0

    left_height = CalcHeight(Node.left)
    right_height = CalcHeight(Node.right)

    return 1 + max(left_height, right_height)
