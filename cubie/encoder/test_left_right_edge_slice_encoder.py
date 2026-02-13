import unittest

from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder
from cubie.test_cubie_util import TestCubieUtil


class TestLeftRightEdgeSliceEncoder(unittest.TestCase):

    def test_to_lr_edge_slice_solved(self):
        """solved cube maps to ud slice of 0 (lowest value)"""
        cubie = TestCubieUtil.solved_cubie()
        mapper = LeftRightEdgeSliceEncoder()
        self.assertEqual(mapper.encode_cubie(cubie), 0)

    def test_to_lr_edge_slice_furthest_from_solved(self):
        """cube with all lr slice edges in fb slice maps to lr slice of 69 (highest value)"""
        edges = [(1, 0), (0, 0), (3, 0), (2, 0), (5, 0), (4, 0), (7, 0), (6, 0), (8, 0), (9, 0), (10, 0), (11, 0)]
        mapper = LeftRightEdgeSliceEncoder()
        self.assertEqual(mapper.encode_edges(edges), 69)


if __name__ == "__main__":
    unittest.main()
