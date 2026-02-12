import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.encoder.corner_half_turn_permutation_encoder import CornerHalfTurnPermutationEncoder
from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.encoder.edge_half_turn_permutation_encoder import EdgeHalfTurnPermutationEncoder
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from cubie.test_cubie_move_applier import TestCubieMoveApplier
from thistlethwaite.phase4.phase4 import Phase4
from thistlethwaite.phase_solver import PhaseSolver


class TestPhase4Solver(unittest.TestCase):
    def test_phase4_solved_cube(self):
        cubie = TestCubieMoveApplier.solved_cubie()

        solver = PhaseSolver(Phase4())
        solution = solver.solve(cubie)

        self.assertEqual(solution, [])

    def test_phase4_single_B2(self):
        cubie = TestCubieMoveApplier.solved_cubie()
        cubie = CubieMoveApplier.apply(cubie, Move.B2)

        solver = PhaseSolver(Phase4())
        solution = solver.solve(cubie)

        self.assertIsNotNone(solution)
        self.assertLessEqual(len(solution), 1)

    def test_solution_actually_solves_phase4(self):
        for scramble_len in range(1, 30):
            cubie = TestCubieMoveApplier.scrambled_cubie(Phase4.ALLOWED_MOVES, scramble_len)

            solver = PhaseSolver(Phase4())
            solution = solver.solve(cubie)

            self.assertIsNotNone(solution)

            cubie = CubieMoveApplier.apply_many(cubie, solution)

            self.assertEqual(CornerHalfTurnPermutationEncoder().encode_cubie(cubie), 0)
            self.assertEqual(EdgeHalfTurnPermutationEncoder().encode_cubie(cubie), 0)


    def test_phase4_moves_preserve_phase3_invariants(self):
        # START FROM A RANDOM G-3 STATE
        cubie = TestCubieMoveApplier.scrambled_cubie(Phase4.ALLOWED_MOVES, 100)

        # sanity check
        self.assertEqual(EdgeOrientationEncoder.from_cubie(cubie), 0)
        self.assertEqual(CornerOrientationEncoder.from_cubie(cubie), 0)
        self.assertEqual(UpDownEdgeSliceEncoder().encode_cubie(cubie), 0)
        self.assertEqual(LeftRightEdgeSliceEncoder().encode_cubie(cubie), 0)
        self.assertEqual(CornerTetradEncoder().encode_cubie(cubie), 0)
        self.assertEqual(CornerPermutationParityEncoder().encode_cubie(cubie), 0)

        # apply random phase-4 moves
        for move in TestCubieMoveApplier.random_moves(Phase4.ALLOWED_MOVES, 1000):
            cubie = CubieMoveApplier.apply(cubie, move)
            # invariants must ALWAYS hold
            self.assertEqual(EdgeOrientationEncoder.from_cubie(cubie), 0)
            self.assertEqual(CornerOrientationEncoder.from_cubie(cubie), 0)
            self.assertEqual(UpDownEdgeSliceEncoder().encode_cubie(cubie), 0)
            self.assertEqual(LeftRightEdgeSliceEncoder().encode_cubie(cubie), 0)
            self.assertEqual(CornerTetradEncoder().encode_cubie(cubie), 0)
            self.assertEqual(CornerPermutationParityEncoder().encode_cubie(cubie), 0)

    def test_phase_4_goal_is_true_for_solved_cube(self):

        cubie = TestCubieMoveApplier.solved_cubie()
        solved = Phase4().phase_solved(cubie)
        self.assertEqual(solved, True)

    def test_phase_4_goal_is_false_for_unsolved_cube(self):
        cubie = ([(2, 0), (3, 0), (7, 0), (4, 0), (1, 0), (5, 0), (6, 0), (0, 0)], [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)])
        solved = Phase4().phase_solved(cubie)
        self.assertEqual(solved, False)


if __name__ == '__main__':
    unittest.main()
