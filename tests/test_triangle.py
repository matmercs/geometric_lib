import unittest
from triangle import area, perimeter, semi_perimeter, heron_area, is_valid_triangle, circumscribed_circle_radius, inscribed_circle_radius


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(10, 5), 25.0)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_semi_perimeter(self):
        self.assertEqual(semi_perimeter(3, 4, 5), 6.0)

    def test_heron_area(self):
        self.assertAlmostEqual(heron_area(3, 4, 5), 6.0)

    def test_is_valid_triangle(self):
        self.assertTrue(is_valid_triangle(3, 4, 5))
        self.assertFalse(is_valid_triangle(1, 2, 10))

    def test_circumscribed_circle_radius(self):
        self.assertAlmostEqual(circumscribed_circle_radius(3, 4, 5), 2.5)

    def test_inscribed_circle_radius(self):
        self.assertAlmostEqual(inscribed_circle_radius(3, 4, 5), 1.0)


if __name__ == '__main__':
    unittest.main()
