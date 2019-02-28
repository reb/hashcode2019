import unittest
from slideshows.solvers import iterative

class TestFrameValue(unittest.TestCase):

    def test_normal(self):
        frame = [
            {
                'tags': ['a', 'b']
            },
            {
                'tags': ['b', 'c']
            },
            {
                'tags': ['c', 'd']
            }
        ]
        self.assertEqual(iterative.frame_value(frame), 2)

    def test_frame_of_4(self):
        frame = [
            {
                'tags': ['a', 'b']
            },
            {
                'tags': ['b', 'c']
            },
            {
                'tags': ['c', 'd']
            },
            {
                'tags': ['d', 'e']
            }
        ]
        self.assertEqual(iterative.frame_value(frame), 3)

class TestFrameValue(unittest.TestCase):

    def test_shouldnt_swap(self):
        slideshow = [
            {
                'tags': ['a', 'b']
            },
            {
                'tags': ['b', 'c']
            },
            {
                'tags': ['c', 'd']
            }
        ]
        self.assertEqual(iterative.should_swap(slideshow, 1), False)

    def test_shouldnt_swap(self):
        slideshow = [
            {},
            {},
            {
                'tags': ['a', 'b']
            },
            {
                'tags': ['d', 'e']
            },
            {
                'tags': ['b', 'c']
            },
            {
                'tags': ['d', 'e']
            },
            {}
        ]
        self.assertEqual(iterative.should_swap(slideshow, 4), True)
