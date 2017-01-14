import unittest
from collections import defaultdict
from check_balanced import check_balanced, BinaryTree


class BalancedTreeTestCase(unittest.TestCase):
    def test_no_tree(self):
        tree = None
        self.assertRaises(TypeError, check_balanced, tree)

    def test_one_node(self):
        tree = BinaryTree()
        result = check_balanced(tree)
        self.assertTrue(result)

    def test_two_nodes(self):
        tree = BinaryTree(
            left = BinaryTree(),
            right = None,
        )
        result = check_balanced(tree)
        self.assertTrue(result)

    def test_three_nodes(self):
        tree = BinaryTree(
            left = BinaryTree(),
            right = BinaryTree(),
        )
        result = check_balanced(tree)
        self.assertTrue(result)
    
    def test_three_in_line(self):
        tree = BinaryTree(
            left = BinaryTree(
                left = BinaryTree(),
                right = None,
            ),
            right = None,
        )
        result = check_balanced(tree)
        self.assertTrue(result)

    def test_unbalanced_small(self):
        tree = BinaryTree(
            left = BinaryTree(
                left = BinaryTree(
                    left = BinaryTree(),
                    right = None,
                ),
                right = None,
            ),
            right = BinaryTree(),
        )
        result = check_balanced(tree)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
