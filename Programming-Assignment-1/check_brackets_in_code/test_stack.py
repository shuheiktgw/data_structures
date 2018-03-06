from unittest import TestCase
from check_brackets import Stack


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_pop(self):
        self.stack.push('first')
        self.stack.push('second')

        self.assertEqual('second', self.stack.pop())
        self.assertEqual('first', self.stack.pop())

        self.stack.push('third')
        self.stack.push('fourth')

        self.assertEqual('fourth', self.stack.pop())
        self.assertEqual('third', self.stack.pop())

        self.assertRaises(RuntimeError, lambda: self.stack.pop())
