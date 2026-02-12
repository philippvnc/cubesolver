import unittest

from cubie.encoder.corner_half_turn_permutation_encoder import CornerHalfTurnPermutationEncoder
from cubie.test_cubie_move_applier import TestCubieMoveApplier


class TestCornerHalfTurnPermutationEncoder(unittest.TestCase):

    def test_solved(self):
        """solved cube maps to corner half turn permutation of 0 (lowest value)"""
        cubie = TestCubieMoveApplier.solved_cubie()
        encoder = CornerHalfTurnPermutationEncoder()
        self.assertEqual(encoder.encode_cubie(cubie), 0)

    def test_corner_half_turn_permutation_furthest_from_solved(self):
        """cube with both corner tetrad fully reversed maps to corner half turn permutation of 575 (highest value)"""
        corners = [(7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)]
        cubie = corners, []
        encoder = CornerHalfTurnPermutationEncoder()
        self.assertEqual(encoder.encode_cubie(cubie), 575)


if __name__ == "__main__":
    unittest.main()
