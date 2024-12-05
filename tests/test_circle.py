import unittest
from circle import area, perimeter, arc_length, sector_area, segment_area


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(5), 78.53981633974483)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(5), 31.41592653589793)

    def test_arc_length(self):
        self.assertAlmostEqual(arc_length(5, 90), 7.853981633974483)

    def test_sector_area(self):
        self.assertAlmostEqual(sector_area(5, 90), 19.634954084936208)

    def test_segment_area(self):
        self.assertAlmostEqual(segment_area(5, 90), 7.134954084936207)


if __name__ == '__main__':
    unittest.main()
