import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.test_cubie_util import TestCubieUtil
from thistlethwaite.phase1.phase1 import Phase1
from thistlethwaite.phase2.phase2 import Phase2
from thistlethwaite.phase_solver import PhaseSolver


class TestPhase2Solver(unittest.TestCase):
    def test_phase2_solved_cube(self):
        cubie = TestCubieUtil.solved_cubie()

        solver = PhaseSolver(Phase2())
        solution = solver.solve(cubie)

        self.assertEqual(solution, [])

    def test_phase2_single_U2(self):
        cubie = TestCubieUtil.solved_cubie()
        cubie = CubieMoveApplier.apply(cubie, Move.U2)

        solver = PhaseSolver(Phase2())
        solution = solver.solve(cubie)

        self.assertIsNotNone(solution)
        self.assertLessEqual(len(solution), 1)

    def test_solution_actually_solves_phase2(self):
        for scramble_len in range(1, 5):
            cubie = TestCubieUtil.scrambled_cubie(Phase2.ALLOWED_MOVES, scramble_len)

            solver = PhaseSolver(Phase2())
            solution = solver.solve(cubie)

            self.assertIsNotNone(solution)
            cubie = CubieMoveApplier.apply_many(cubie, solution)
            self.assertEqual(Phase2().phase_solved(cubie), True)

    def test_phase2_moves_preserve_phase1_invariants(self):
        # START FROM A RANDOM G-1 STATE
        cubie = TestCubieUtil.scrambled_cubie(Phase2.ALLOWED_MOVES, 100)

        # sanity check
        self.assertEqual(Phase1().phase_solved(cubie), True)

        # apply random phase-2 moves
        for move in TestCubieUtil.random_moves(Phase2.ALLOWED_MOVES, 1000):
            cubie = CubieMoveApplier.apply(cubie, move)

            # invariants must ALWAYS hold
            self.assertEqual(Phase1().phase_solved(cubie), True)


if __name__ == '__main__':
    unittest.main()
