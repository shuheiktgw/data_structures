from unittest import TestCase
from tree_height import Node

class TestNode(TestCase):
    def setUp(self):
        self.node = Node()

    def test_add_child(self):
        self.node.add_child(Node())
        self.node.add_child(Node())

        self.assertEqual(2, len(self.node.children))
