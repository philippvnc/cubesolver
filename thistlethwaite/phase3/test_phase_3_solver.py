import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.encoder.corner_tetrad_permutation_parity_encoder import CornerTetradPermutationParityEncoder
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from thistlethwaite.phase3.phase3 import Phase3
from cubie.test_cubie_move_applier import TestCubieMoveApplier
from thistlethwaite.phase_solver import PhaseSolver


class TestPhase3Solver(unittest.TestCase):
    def test_phase3_solved_cube(self):
        cubie = TestCubieMoveApplier.solved_cubie()

        solver = PhaseSolver(Phase3())
        solution = solver.solve(cubie)

        self.assertEqual(solution, [])

    def test_phase3_single_F2(self):
        cubie = TestCubieMoveApplier.solved_cubie()
        cubie = CubieMoveApplier.apply(cubie, Move.F2)

        solver = PhaseSolver(Phase3())
        solution = solver.solve(cubie)

        self.assertIsNotNone(solution)
        self.assertLessEqual(len(solution), 1)

    def test_solution_actually_solves_phase3(self):
        for scramble_len in range(1, 30):
            cubie = TestCubieMoveApplier.scrambled_cubie(Phase3.ALLOWED_MOVES, scramble_len)

            solver = PhaseSolver(Phase3())
            solution = solver.solve(cubie)

            self.assertIsNotNone(solution)

            cubie = CubieMoveApplier.apply_many(cubie, solution)

            self.assertEqual(LeftRightEdgeSliceEncoder().encode_cubie(cubie), 0)
            self.assertEqual(CornerTetradEncoder().encode_cubie(cubie), 0)
            self.assertEqual(CornerPermutationParityEncoder().encode_cubie(cubie), 0)

    def test_phase3_moves_preserve_phase2_invariants(self):
        # START FROM A RANDOM G-2 STATE
        cubie = TestCubieMoveApplier.scrambled_cubie(Phase3.ALLOWED_MOVES, 100)

        # sanity check
        self.assertEqual(EdgeOrientationEncoder.from_cubie(cubie), 0)
        self.assertEqual(CornerOrientationEncoder.from_cubie(cubie), 0)
        self.assertEqual(UpDownEdgeSliceEncoder().encode_cubie(cubie), 0)

        # apply random phase-3 moves
        for move in TestCubieMoveApplier.random_moves(Phase3.ALLOWED_MOVES, 1000):
            cubie = CubieMoveApplier.apply(cubie, move)
            # invariants must ALWAYS hold
            self.assertEqual(EdgeOrientationEncoder.from_cubie(cubie), 0)
            self.assertEqual(CornerOrientationEncoder.from_cubie(cubie), 0)
            self.assertEqual(UpDownEdgeSliceEncoder().encode_cubie(cubie), 0)



if __name__ == '__main__':
    unittest.main()
