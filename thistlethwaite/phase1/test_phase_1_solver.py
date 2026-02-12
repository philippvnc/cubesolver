import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from thistlethwaite.phase1.phase1 import Phase1
from thistlethwaite.phase_solver import PhaseSolver
from cubie.test_cubie_move_applier import TestCubieMoveApplier


class TestPhase1IDAStarSolver(unittest.TestCase):
    def test_phase1_solved_cube(self):
        cubie = TestCubieMoveApplier.solved_cubie()
        solver = PhaseSolver(Phase1())
        solution = solver.solve(cubie)
        self.assertEqual(solution, [])

    def test_phase1_single_F(self):
        cubie = TestCubieMoveApplier.solved_cubie()
        cubie = CubieMoveApplier.apply(cubie, Move.F)

        solver = PhaseSolver(Phase1())
        solution = solver.solve(cubie)

        self.assertIsNotNone(solution)
        self.assertLessEqual(len(solution), 1)

    def test_phase1_result_has_zero_eo(self):
        cubie = TestCubieMoveApplier.scrambled_cubie([Move.F, Move.R], 10)

        solver = PhaseSolver(Phase1())
        solution = solver.solve(cubie)
        self.assertIsNotNone(solution)

        cubie = CubieMoveApplier.apply_many(cubie, solution)

        eo = EdgeOrientationEncoder.from_cubie(cubie)
        self.assertEqual(eo, 0)



if __name__ == '__main__':
    unittest.main()
