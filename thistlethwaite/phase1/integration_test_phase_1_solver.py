import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.test_cubie_util import TestCubieUtil
from thistlethwaite.phase1.phase1 import Phase1
from thistlethwaite.phase_solver import PhaseSolver


class TestPhase1IDAStarSolver(unittest.TestCase):
    def test_phase1_solved_cube(self):
        cubie = TestCubieUtil.solved_cubie()
        solver = PhaseSolver(Phase1())
        solution = solver.solve(cubie)
        self.assertEqual(solution, [])

    def test_phase1_single_F(self):
        cubie = TestCubieUtil.solved_cubie()
        cubie = CubieMoveApplier.apply(cubie, Move.F)

        solver = PhaseSolver(Phase1())
        solution = solver.solve(cubie)

        self.assertIsNotNone(solution)
        self.assertLessEqual(len(solution), 1)

    def test_solution_actually_solves_phase1(self):
        for scramble_len in range(1, 5):
            cubie = TestCubieUtil.scrambled_cubie(Phase1().allowed_moves, scramble_len)

            solver = PhaseSolver(Phase1())
            solution = solver.solve(cubie)

            self.assertIsNotNone(solution)
            cubie = CubieMoveApplier.apply_many(cubie, solution)
            self.assertEqual(Phase1().solved(cubie), True)


if __name__ == '__main__':
    unittest.main()
