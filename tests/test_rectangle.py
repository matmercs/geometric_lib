import unittest
from rectangle import area, perimeter, diagonal, is_square


class TestRectangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 3), 15)

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 3), 16)

    def test_diagonal(self):
        self.assertAlmostEqual(diagonal(5, 3), 5.830951894845301)

    def test_is_square(self):
        self.assertTrue(is_square(5, 5))
        self.assertFalse(is_square(5, 3))


if __name__ == '__main__':
    unittest.main()
