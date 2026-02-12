import unittest

from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from cubie.test_cubie_move_applier import TestCubieMoveApplier


class TestUpDownEdgeSliceEncoder(unittest.TestCase):

    def test_to_ud_edge_slice_solved(self):
        """solved cube maps to ud slice of 0 (lowest value)"""
        cubie = TestCubieMoveApplier.solved_cubie()
        encoder = UpDownEdgeSliceEncoder()
        self.assertEqual(encoder.encode_cubie(cubie), 0)

    def test_to_ud_edge_slice_furthest_from_solved(self):
        """cube with no ud slice edges in middle layer maps to ud slice of 494 (highest value)"""
        edges = [(11 - i, 0) for i in range(12)]
        encoder = UpDownEdgeSliceEncoder()
        self.assertEqual(encoder.encode_edges(edges), 494)


if __name__ == "__main__":
    unittest.main()
