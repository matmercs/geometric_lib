import unittest
from square import area, perimeter, diagonal


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4), 16)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)

    def test_diagonal(self):
        self.assertAlmostEqual(diagonal(4), 5.656854249492381)


if __name__ == '__main__':
    unittest.main()
