from unittest import TestCase
from tree_height import Tree


class TestTree(TestCase):
    def test___init__small_tree(self):
        tree = Tree(2, [1, -1])
        self.assertEqual(1, len(tree.root.children))

    def test___init__middle_tree(self):
        tree = Tree(5, [-1, 0, 4, 0, 3])
        self.assertEqual(2, len(tree.root.children))
        self.assertEqual(0, len(tree.root.children[0].children))
        self.assertEqual(1, len(tree.root.children[1].children))

    def test___init__small_tree_height(self):
        tree = Tree(2, [1, -1])
        self.assertEqual(2, tree.height())

    def test___init__middle_tree_height_first(self):
        tree = Tree(5, [-1, 0, 4, 0, 3])
        self.assertEqual(4, tree.height())

    def test___init__middle_tree_height_second(self):
        tree = Tree(5, [4, -1, 4, 1, 1])
        self.assertEqual(3, tree.height())
