# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Tree:
    def __init__(self, n, parent):
            self.nodes = []
            for i in range(n):
                self.nodes.append(Node())

            for i in range(n):
                if parent[i] == -1:
                    self.root = self.nodes[i]
                else:
                    self.nodes[parent[i]].add_child(self.nodes[i])

    def height(self):
        return self._compute_height(self.root)

    def _compute_height(self, node):
        h = [0]
        for child in node.children:
            h.append(self._compute_height(child))

        return 1 + max(h)


class TreeHeight:
        def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
            tree = Tree(self.n, self.parent)
            return tree.height()


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
