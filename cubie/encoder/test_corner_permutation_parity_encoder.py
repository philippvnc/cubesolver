import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.test_cubie_util import TestCubieUtil


class TestCornerPermutationParityEncoder(unittest.TestCase):

    def test_solved_cubie_has_parity_0(self):
        """solved cube maps to corner permutation parity of 0"""
        cubie = TestCubieUtil.solved_cubie()
        parity = CornerPermutationParityEncoder.encode_cubie(cubie)
        self.assertEqual(parity, 0)

    def test_single_quarter_turn_has_parity_1(self):
        """cube with single quarter turn maps to corner permutation parity of 1"""
        for move in [Move.U, Move.D, Move.R, Move.L, Move.B, Move.F]:
            cubie = TestCubieUtil.solved_cubie()
            cubie = CubieMoveApplier.apply(cubie, move)
            parity = CornerPermutationParityEncoder.encode_cubie(cubie)
            self.assertEqual(parity, 1)

    def test_single_half_turn_has_parity_0(self):
        """cube with single half turn maps to corner permutation parity of 0"""
        for move in [Move.U2, Move.D2, Move.R2, Move.L2, Move.B2, Move.F2]:
            cubie = TestCubieUtil.solved_cubie()
            cubie = CubieMoveApplier.apply(cubie, move)
            parity = CornerPermutationParityEncoder.encode_cubie(cubie)
            self.assertEqual(parity, 0)


if __name__ == "__main__":
    unittest.main()
