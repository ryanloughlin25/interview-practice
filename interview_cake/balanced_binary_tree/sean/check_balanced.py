class BinaryTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.leaf = not bool(self.left or self.right)

def check_balanced(tree, depth=0):
    if not isinstance(tree, BinaryTree):
        raise TypeError("you need a tree mang")

    if tree.leaf:
        depths = [depth]
    else:
        left_depths = []
        right_depths = []
        if tree.left:
            left_depths = check_balanced(tree.left, depth=depth+1)
        if tree.right:
            right_depths = check_balanced(tree.right, depth=depth+1)
        depths = left_depths + right_depths

    if depth == 0:
        unbalanced = bool(min(depths) >= max(depths) - 1)
        return unbalanced
    else:
        return depths
