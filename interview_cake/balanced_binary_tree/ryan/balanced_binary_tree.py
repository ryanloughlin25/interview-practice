import sys
from queue import Queue


def balanced_binary_tree(node):
    min_depth = sys.maxsize
    max_depth = 0
    q = Queue()
    q.put((node, 0))

    while not q.empty():
        node, depth = q.get()
        children = list(filter(None, [node.left, node.right]))
        for child in children:
            q.put((child, depth + 1))
        if not children:
            min_depth = min(min_depth, depth)
            max_depth = max(max_depth, depth)

    return max_depth - min_depth <= 1
