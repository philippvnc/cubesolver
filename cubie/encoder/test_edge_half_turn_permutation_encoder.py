import unittest

from cubie.encoder.edge_half_turn_permutation_encoder import EdgeHalfTurnPermutationEncoder
from cubie.test_cubie_util import TestCubieUtil


class TestEdgeHalfTurnPermutationEncoder(unittest.TestCase):

    def test_solved(self):
        """solved cube maps to edge half turn permutation of 0 (lowest value)"""
        cubie = TestCubieUtil.solved_cubie()
        encoder = EdgeHalfTurnPermutationEncoder()
        self.assertEqual(encoder.encode_cubie(cubie), 0)

    def test_edge_half_turn_permutation_furthest_from_solved(self):
        """cube with both edge tetrad fully reversed maps to edge half turn permutation of 13823 (highest value)"""
        edges = [(6, 0), (7, 0), (4, 0), (5, 0), (2, 0), (3, 0), (0, 0), (1, 0), (11, 0), (10, 0), (9, 0), (8, 0)]
        cubie = [], edges
        encoder = EdgeHalfTurnPermutationEncoder()
        self.assertEqual(encoder.encode_cubie(cubie), 13823)


if __name__ == "__main__":
    unittest.main()
