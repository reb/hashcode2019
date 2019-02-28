import unittest
from slideshows.solvers import general

class TestValue(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(general.value(['a', 'b'], ['b', 'c']), 1)

    def test_same_ending(self):
        self.assertEqual(general.value(['b', 'c', 'e'], ['d', 'e']), 1)

    def test_bigger(self):
        self.assertEqual(general.value(['a', 'b', 'c', 'e'], ['a', 'd', 'e', 'f']), 2)
