import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.test_cubie_util import TestCubieUtil
from thistlethwaite.thistlethwaite import Thistlethwaite


class TestThistlethwaite(unittest.TestCase):

    def test_scrambled_cube(self):
        expected_solved_cubie = TestCubieUtil.solved_cubie()
        scrambled_cubie = TestCubieUtil.scrambled_cubie(Move.ALL_MOVES, 7)

        solution = Thistlethwaite.solve(scrambled_cubie)
        actual_solved_cubie = CubieMoveApplier.apply_many(scrambled_cubie, solution)

        self.assertEqual(actual_solved_cubie, expected_solved_cubie)