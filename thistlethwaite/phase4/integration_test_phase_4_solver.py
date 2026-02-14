import unittest

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.encoder.corner_tetrad_permutation_parity_encoder import CornerTetradPermutationParityEncoder
from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder
from cubie.test_cubie_util import TestCubieUtil
from thistlethwaite.phase1.phase1 import Phase1
from thistlethwaite.phase2.phase2 import Phase2
from thistlethwaite.phase3.phase3 import Phase3
from thistlethwaite.phase4.phase4 import Phase4
from thistlethwaite.phase_solver import PhaseSolver


class IntegrationTestPhase4Solver(unittest.TestCase):
    def test_phase4_solved_cube(self):
        cubie = TestCubieUtil.solved_cubie()

        solver = PhaseSolver(Phase4())
        solution = solver.solve(cubie)

        self.assertEqual(solution, [])

    def test_phase4_single_B2(self):
        cubie = TestCubieUtil.solved_cubie()
        cubie = CubieMoveApplier.apply(cubie, Move.B2)

        solver = PhaseSolver(Phase4())
        solution = solver.solve(cubie)

        self.assertIsNotNone(solution)
        self.assertLessEqual(len(solution), 1)

    def test_solution_actually_solves_phase4(self):
        phase4 = Phase4()
        for scramble_len in range(1, 5):
            cubie = TestCubieUtil.scrambled_cubie(phase4.allowed_moves, scramble_len)

            solver = PhaseSolver(phase4)
            solution = solver.solve(cubie)

            self.assertIsNotNone(solution)

            cubie = CubieMoveApplier.apply_many(cubie, solution)

            self.assertEqual(phase4.solved(cubie), True)


    def test_phase4_moves_preserve_phase3_invariants(self):
        # START FROM A RANDOM G-3 STATE
        cubie = TestCubieUtil.scrambled_cubie(Phase4().allowed_moves, 100)
        left_right_edge_slice_encoder = LeftRightEdgeSliceEncoder()
        corner_tetrad_encoder = CornerTetradEncoder()

        # sanity check
        self.assertEqual(Phase1().solved(cubie), True)
        self.assertEqual(Phase2().solved(cubie), True)
        phase_3 = (left_right_edge_slice_encoder.encode_cubie(cubie) == 0 and corner_tetrad_encoder.encode_cubie(
            cubie) == 0 and CornerPermutationParityEncoder.encode_cubie(cubie) == 0)
        self.assertEqual(phase_3, True)

        # apply random phase-4 moves
        for move in TestCubieUtil.random_moves(Phase4().allowed_moves, 1000):
            cubie = CubieMoveApplier.apply(cubie, move)
            # invariants must hold
            self.assertEqual(Phase1().solved(cubie), True)
            self.assertEqual(Phase2().solved(cubie), True)

            phase_3 = (left_right_edge_slice_encoder.encode_cubie(cubie) == 0 and corner_tetrad_encoder.encode_cubie(
                cubie) == 0 and CornerPermutationParityEncoder.encode_cubie(cubie) == 0)
            self.assertEqual(phase_3, True)

            # phase 3 is an exception because corner tetrad permutation parity == 0 is only enforced right after phase 3 solve.
            # after that both corner tetrad permutation parity can go from (0,0) to (1,1) on any half turn.
            # todo change that encoder to check for equal tetrad permutation parity instead of == 0.
            # that way we can assert full invariance here too


if __name__ == '__main__':
    unittest.main()
