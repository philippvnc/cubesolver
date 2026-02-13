import unittest

from cubie.encoder.corner_tetrad_permutation_parity_encoder import CornerTetradPermutationParityEncoder
from cubie.test_cubie_util import TestCubieUtil


class TestCornerTetradParityEncoder(unittest.TestCase):

    def test_solved_cubie_even_parity(self):
        cubie = TestCubieUtil.solved_cubie()
        self.assertEqual(CornerTetradPermutationParityEncoder().encode_cubie(cubie), 0)

    def test_tetrad_a_swap_odd_parity(self):
        # Swap two corners in the first tetrad (0,2,5,7) -> parity becomes odd
        cubie = [(2,0), (1,0), (0,0), (3,0), (4,0), (5,0), (6,0), (7,0)], []
        self.assertEqual(CornerTetradPermutationParityEncoder().encode_cubie(cubie), 1)

    def test_tetrad_a_reorder_even_parity(self):
        # Rotate within tetrad but parity stays even
        cubie = [(5,0), (2,0), (7,0), (0,0), (1,0), (3,0), (4,0), (6,0)], []
        self.assertEqual(CornerTetradPermutationParityEncoder().encode_cubie(cubie), 0)

    def test_partial_tetrad_ignored_corners(self):
        # Corners outside the tetrad can move, but only tetrad matters
        cubie = [(0,0), (3,0), (2,0), (1,0), (4,0), (7,0), (5,0), (6,0)], []
        self.assertEqual(CornerTetradPermutationParityEncoder().encode_cubie(cubie), 1)

if __name__ == "__main__":
    unittest.main()
