import random
import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.test_cubie_asserter import CubieAsserter


class TestCubieMoveApplier(unittest.TestCase):

    @staticmethod
    def solved_cubie():
        return [(corner, 0) for corner in range(8)], [(edge, 0) for edge in range(12)]

    @staticmethod
    def random_moves(allowed_moves: list[int], length: int) -> list[int]:
        random.seed(137)
        scramble = []
        last_face = -1
        for _ in range(length):
            move = random.choice(allowed_moves)
            # avoid same-face repetitions
            while last_face != -1 and move // 3 == last_face:
                move = random.choice(allowed_moves)
            scramble.append(move)
            last_face = move // 3
        return scramble

    @staticmethod
    def scrambled_cubie(allowed_moves: list[int], length: int):
        cubie = TestCubieMoveApplier.solved_cubie()
        scramble = TestCubieMoveApplier.random_moves(allowed_moves, length)
        return CubieMoveApplier.apply_many(cubie, scramble)

    def test_move_U(self):
        actual = CubieMoveApplier.apply(self.solved_cubie(), Move.U)
        CubieAsserter.assert_U_clockwise_from_solved(actual)

    def test_move_D(self):
        actual = CubieMoveApplier.apply(self.solved_cubie(), Move.D)
        CubieAsserter.assert_D_clockwise_from_solved(actual)

    def test_move_R(self):
        actual = CubieMoveApplier.apply(self.solved_cubie(), Move.R)
        CubieAsserter.assert_R_clockwise_from_solved(actual)

    def test_move_L(self):
        actual = CubieMoveApplier.apply(self.solved_cubie(), Move.L)
        CubieAsserter.assert_L_clockwise_from_solved(actual)

    def test_move_F(self):
        actual = CubieMoveApplier.apply(self.solved_cubie(), Move.F)
        CubieAsserter.assert_F_clockwise_from_solved(actual)

    def test_move_B(self):
        actual = CubieMoveApplier.apply(self.solved_cubie(), Move.B)
        CubieAsserter.assert_B_clockwise_from_solved(actual)

    def test_identity_moves(self):
        for move in [Move.L, Move.R, Move.F, Move.B, Move.U, Move.D]:
            actual = self.solved_cubie()
            for i in range(4):
                actual = CubieMoveApplier.apply(actual, move)
            assert actual == self.solved_cubie()

    def test_canceling_moves(self):
        cancel_pairs = [(Move.L, Move.L_), (Move.R, Move.R_), (Move.F,Move.F_), (Move.B,Move.B_), (Move.U,Move.U_), (Move.D,Move.D_)]
        for first, second in cancel_pairs:
            expected = self.solved_cubie()
            modified = CubieMoveApplier.apply(expected, first)
            actual = CubieMoveApplier.apply(modified, second)
            assert actual == self.solved_cubie()


if __name__ == '__main__':
    unittest.main()
