import sys
from queue import Queue


def balanced_binary_tree(node):
    min_depth = sys.maxsize
    max_depth = 0
    q = Queue()
    q.put((node, 0))

    while not q.empty():
        node, depth = q.get()
        if node.left:
            q.put((node.left, depth + 1))
        if node.right:
            q.put((node.right, depth + 1))

        if not node.left and not node.right:
            min_depth = min(min_depth, depth)
            max_depth = max(max_depth, depth)

    return max_depth - min_depth <= 1
