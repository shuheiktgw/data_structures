from unittest import TestCase
from check_brackets import Bracket


class TestBracket(TestCase):
    def setUp(self):
        self.bracket = Bracket('[', 1)

    def test_match(self):
        self.assertTrue(self.bracket.match(']'))
        self.assertFalse(self.bracket.match('['))
        self.assertFalse(self.bracket.match(')'))

