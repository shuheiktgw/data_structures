# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.first = None

    def push(self, value):
        self.first = Node(value, self.first)

    def pop(self):
        if self.first is None:
            raise RuntimeError('Stack is empty!')

        value = self.first.value
        self.first = self.first.next_node
        return value


if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                print(i + 1)
                sys.exit(None)

            bracket = opening_brackets_stack.pop()
            if not bracket.match(next):
                print(i + 1)
                sys.exit(None)

    print('Success')
