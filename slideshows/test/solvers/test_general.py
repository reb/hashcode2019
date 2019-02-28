import unittest
from slideshows.solvers import general

class TestValue(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(general.value(['a', 'b'], ['b', 'c']), 1)
