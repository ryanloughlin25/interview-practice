import unittest
from balanced_binary_tree import balanced_binary_tree


class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BalancedBinaryTreeTestCase(unittest.TestCase):
    def test_only_root(self):
        root = BinaryTree()
        self.assertEqual(balanced_binary_tree(root), True)

    def test_single_left(self):
        root = BinaryTree(left=BinaryTree())
        self.assertEqual(balanced_binary_tree(root), True)

    def test_not_balanced(self):
        root = BinaryTree(
            left=BinaryTree(),
            right=BinaryTree(
                right=BinaryTree(
                    right=BinaryTree(),
                ),
            ),
        )
        self.assertEqual(balanced_binary_tree(root), False)

    def test_balanced(self):
        root = BinaryTree(
            left=BinaryTree(
                left=BinaryTree(),
                right=BinaryTree(),
            ),
            right=BinaryTree(
                left=BinaryTree(),
                right=BinaryTree(),
            ),
        )
        self.assertEqual(balanced_binary_tree(root), True)


if __name__ == '__main__':
    unittest.main()
