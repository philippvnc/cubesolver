import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.test_cubie_util import TestCubieUtil


class TestCubieMoveApplier(unittest.TestCase):

    def test_move_U(self):
        actual = CubieMoveApplier.apply(TestCubieUtil.solved_cubie(), Move.U)
        TestCubieUtil.assert_U_clockwise_from_solved(actual)

    def test_move_D(self):
        actual = CubieMoveApplier.apply(TestCubieUtil.solved_cubie(), Move.D)
        TestCubieUtil.assert_D_clockwise_from_solved(actual)

    def test_move_R(self):
        actual = CubieMoveApplier.apply(TestCubieUtil.solved_cubie(), Move.R)
        TestCubieUtil.assert_R_clockwise_from_solved(actual)

    def test_move_L(self):
        actual = CubieMoveApplier.apply(TestCubieUtil.solved_cubie(), Move.L)
        TestCubieUtil.assert_L_clockwise_from_solved(actual)

    def test_move_F(self):
        actual = CubieMoveApplier.apply(TestCubieUtil.solved_cubie(), Move.F)
        TestCubieUtil.assert_F_clockwise_from_solved(actual)

    def test_move_B(self):
        actual = CubieMoveApplier.apply(TestCubieUtil.solved_cubie(), Move.B)
        TestCubieUtil.assert_B_clockwise_from_solved(actual)

    def test_identity_moves(self):
        for move in [Move.L, Move.R, Move.F, Move.B, Move.U, Move.D]:
            actual = TestCubieUtil.solved_cubie()
            for i in range(4):
                actual = CubieMoveApplier.apply(actual, move)
            assert actual == TestCubieUtil.solved_cubie()

    def test_canceling_moves(self):
        cancel_pairs = [(Move.L, Move.L_), (Move.R, Move.R_), (Move.F,Move.F_), (Move.B,Move.B_), (Move.U,Move.U_), (Move.D,Move.D_)]
        for first, second in cancel_pairs:
            expected = TestCubieUtil.solved_cubie()
            modified = CubieMoveApplier.apply(expected, first)
            actual = CubieMoveApplier.apply(modified, second)
            assert actual == TestCubieUtil.solved_cubie()


if __name__ == '__main__':
    unittest.main()
