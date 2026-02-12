import unittest
import random

from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder


class TestCornerOrientationEncoder(unittest.TestCase):

    def test_to_co_solved(self):
        """Cubie corners with orientation all 0 should produce encoded co of 0 (the lowest value)"""
        corners = [(i, 0) for i in range(8)]
        self.assertEqual(CornerOrientationEncoder.from_cubie_corners(corners), 0)

    def test_to_co_single_twist(self):
        """Cubie corners with one orientation off of 0 should produce expected encoded co"""
        corners = [(i, 0) for i in range(8)]
        corners[0] = (0, 1)

        expected = 1 * (3 ** 6)
        self.assertEqual(CornerOrientationEncoder.from_cubie_corners(corners), expected)

    def test_to_co_max_value(self):
        """Cubie corners with orientation all 2 should produce encoded co of 3^7 -1 (the highest value)"""
        corners = [(i, 2) for i in range(7)] + [(7, 0)]
        expected = (3 ** 7) - 1
        self.assertEqual(CornerOrientationEncoder.from_cubie_corners(corners), expected)

    def test_decode_co_solved(self):
        """Corner orientation index 0 should produce all corners with orientation 0"""
        co = 0
        cubie_corner_orientations = CornerOrientationEncoder.to_cubie_corner_orientations(co)
        self.assertEqual(len(cubie_corner_orientations), 8)
        # all orientations should be 0
        for ori in cubie_corner_orientations:
            self.assertEqual(ori, 0)

    def test_decode_co_arbitrary(self):
        """Check round-trip: encoding and decoding from random cubies preserves data"""
        random.seed(1337)
        for _ in range(1000):
            expected_oris = [(i, random.randint(0,2)) for i in range(8)]
            expected_oris[7] = (7, (-sum([ori for (_,ori) in expected_oris[:-1]]) % 3))
            co = CornerOrientationEncoder.from_cubie_corners(expected_oris)
            actual_oris = CornerOrientationEncoder.to_cubie_corner_orientations(co)
            for (_, expected_ori), actual_ori in zip(expected_oris, actual_oris):
                self.assertEqual(expected_ori, actual_ori)


if __name__ == "__main__":
    unittest.main()
