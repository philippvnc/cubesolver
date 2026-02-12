import unittest

from cubie.encoder.edge_tetrad_permutation_encoder import EdgeTetradPermutationEncoder
from cubie.test_cubie_move_applier import TestCubieMoveApplier


class TestEdgePermutationEncoder(unittest.TestCase):

    def test_to_ep_solved(self):
        """solved cube should produce ep of 0"""
        solved = TestCubieMoveApplier.solved_cubie()
        self.assertEqual(EdgeTetradPermutationEncoder.encode_cubie(solved), 0)

    def test_to_ep_single_swap(self):
        """Cubie with a single swap should produce non-zero ep"""
        _, edges = TestCubieMoveApplier.solved_cubie()
        edges[0] = (1, 0)
        edges[1] = (0, 0)
        self.assertGreater(EdgeTetradPermutationEncoder.encode_edges(edges), 0)

if __name__ == "__main__":
    unittest.main()
