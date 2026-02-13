import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.test_cubie_util import TestCubieUtil
from thistlethwaite.phase1.phase1 import Phase1
from thistlethwaite.phase2.phase2 import Phase2
from thistlethwaite.phase3.phase3 import Phase3
from thistlethwaite.phase_solver import PhaseSolver


class TestPhase3Solver(unittest.TestCase):
    def test_phase3_solved_cube(self):
        cubie = TestCubieUtil.solved_cubie()

        solver = PhaseSolver(Phase3())
        solution = solver.solve(cubie)

        self.assertEqual(solution, [])

    def test_phase3_single_F2(self):
        cubie = TestCubieUtil.solved_cubie()
        cubie = CubieMoveApplier.apply(cubie, Move.F2)

        solver = PhaseSolver(Phase3())
        solution = solver.solve(cubie)

        self.assertIsNotNone(solution)
        self.assertLessEqual(len(solution), 1)

    def test_solution_actually_solves_phase3(self):
        for scramble_len in range(1, 5):
            cubie = TestCubieUtil.scrambled_cubie(Phase3.ALLOWED_MOVES, scramble_len)

            solver = PhaseSolver(Phase3())
            solution = solver.solve(cubie)

            self.assertIsNotNone(solution)

            cubie = CubieMoveApplier.apply_many(cubie, solution)

            self.assertEqual(Phase3().phase_solved(cubie), True)

    def test_phase3_moves_preserve_phase2_invariants(self):
        # START FROM A RANDOM G-2 STATE
        cubie = TestCubieUtil.scrambled_cubie(Phase3.ALLOWED_MOVES, 100)

        # sanity check
        self.assertEqual(Phase1().phase_solved(cubie), True)
        self.assertEqual(Phase2().phase_solved(cubie), True)

        # apply random phase-3 moves
        for move in TestCubieUtil.random_moves(Phase3.ALLOWED_MOVES, 1000):
            cubie = CubieMoveApplier.apply(cubie, move)
            # invariants must ALWAYS hold
            self.assertEqual(Phase1().phase_solved(cubie), True)
            self.assertEqual(Phase2().phase_solved(cubie), True)



if __name__ == '__main__':
    unittest.main()
