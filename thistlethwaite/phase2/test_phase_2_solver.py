import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from thistlethwaite.phase2.phase2 import Phase2
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from thistlethwaite.phase_solver import PhaseSolver
from cubie.test_cubie_move_applier import TestCubieMoveApplier


class TestPhase2Solver(unittest.TestCase):
    def test_phase2_solved_cube(self):
        cubie = TestCubieMoveApplier.solved_cubie()

        solver = PhaseSolver(Phase2())
        solution = solver.solve(cubie)

        self.assertEqual(solution, [])

    def test_phase2_single_U2(self):
        cubie = TestCubieMoveApplier.solved_cubie()
        cubie = CubieMoveApplier.apply(cubie, Move.U2)

        solver = PhaseSolver(Phase2())
        solution = solver.solve(cubie)

        self.assertIsNotNone(solution)
        self.assertLessEqual(len(solution), 1)

    def test_solution_actually_solves_phase2(self):
        cubie = TestCubieMoveApplier.solved_cubie()
        cubie = CubieMoveApplier.apply_many(cubie, [Move.F2, Move.U])

        solver = PhaseSolver(Phase2())
        solution = solver.solve(cubie)

        self.assertIsNotNone(solution)

        cubie = CubieMoveApplier.apply_many(cubie, solution)


        self.assertEqual(CornerOrientationEncoder.from_cubie(cubie), 0)
        self.assertEqual(UpDownEdgeSliceEncoder().encode_cubie(cubie), 0)

    def test_phase2_moves_preserve_phase1_invariants(self):
        # START FROM A RANDOM G-1 STATE
        cubie = TestCubieMoveApplier.scrambled_cubie(Phase2.ALLOWED_MOVES, 100)

        # sanity check
        self.assertEqual(EdgeOrientationEncoder.from_cubie(cubie), 0)

        # apply random phase-2 moves
        for move in TestCubieMoveApplier.random_moves(Phase2.ALLOWED_MOVES, 1000):
            cubie = CubieMoveApplier.apply(cubie, move)

            # invariants must ALWAYS hold
            self.assertEqual(EdgeOrientationEncoder.from_cubie(cubie), 0)


if __name__ == '__main__':
    unittest.main()
