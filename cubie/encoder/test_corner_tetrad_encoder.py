import unittest

from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.test_cubie_move_applier import TestCubieMoveApplier


class TestCornerTetradEncoder(unittest.TestCase):

    def test_to_corner_tetrad_solved(self):
        """solved cube maps to corner tetrad of 0 (lowest value)"""
        cubie = TestCubieMoveApplier.solved_cubie()
        encoder = CornerTetradEncoder()
        self.assertEqual(encoder.encode_cubie(cubie), 0)

    def test_to_corner_tetrad_furthest_from_solved(self):
        """cube with all corners in wrong tetrad maps to tetrad of 69 (highest value)"""
        corners = [(1, 0), (0, 0), (3, 0), (2, 0), (5, 0), (4, 0), (7, 0), (6, 0)]
        encoder = CornerTetradEncoder()
        self.assertEqual(encoder.encode_corners(corners), 69)


if __name__ == "__main__":
    unittest.main()
