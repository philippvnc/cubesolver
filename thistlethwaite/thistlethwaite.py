from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.encoder.corner_half_turn_permutation_encoder import CornerHalfTurnPermutationEncoder
from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.encoder.corner_tetrad_permutation_parity_encoder import CornerTetradPermutationParityEncoder
from cubie.encoder.edge_half_turn_permutation_encoder import EdgeHalfTurnPermutationEncoder
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from thistlethwaite.heuristic import Heuristic
from thistlethwaite.phase1.phase1 import Phase1
from thistlethwaite.phase2.phase2 import Phase2
from thistlethwaite.phase3.phase3 import Phase3
from thistlethwaite.phase4.phase4 import Phase4
from thistlethwaite.phase_solver import PhaseSolver

'''
Thistlethwaite cube solver, solves 4 phases iteratively and joins solutions.
'''
class Thistlethwaite:

    __PHASES = [
        Phase1(Heuristic().phase_1_heuristic),
        Phase2(Heuristic().phase_2_heuristic),
        Phase3(Heuristic().phase_3_heuristic),
        Phase4(Heuristic().phase_4_heuristic)
    ]

    @staticmethod
    def solve(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> list[int] | None:
        solution: list[int] = []

        for phase in Thistlethwaite.__PHASES:
            cubie, phase_solution = Thistlethwaite.solve_phase(cubie, phase)
            solution.extend(phase_solution)

        return solution

    @staticmethod
    def solve_phase(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]],
                    phase) -> tuple[tuple[list[tuple[int, int]], list[tuple[int, int]]], list[int]] | None:
        print(f"starting {phase.NAME} solve:")
        solver = PhaseSolver(phase)
        solution = solver.solve(cubie)
        if solution is None:
            return None
        print(f"found {phase.NAME} solution:")
        Move.print_moves(solution)
        cubie = CubieMoveApplier.apply_many(cubie, solution)

        edge_orientation = EdgeOrientationEncoder.from_cubie(cubie)
        corner_orientation = CornerOrientationEncoder.from_cubie(cubie)
        ud_down_edge_slice = UpDownEdgeSliceEncoder().encode_cubie(cubie)
        left_right_edge_slice = LeftRightEdgeSliceEncoder().encode_cubie(cubie)
        corner_tetrad = CornerTetradEncoder().encode_cubie(cubie)
        permutation_parity = CornerPermutationParityEncoder().encode_cubie(cubie)
        corner_tetrad_permutation_parity = CornerTetradPermutationParityEncoder.encode_cubie(cubie)
        corner_permutation = CornerHalfTurnPermutationEncoder().encode_cubie(cubie)
        edge_permutation = EdgeHalfTurnPermutationEncoder().encode_cubie(cubie)

        print(f"cubie {cubie}")
        print(f"edge_orientation {edge_orientation}")
        print(f"corner_orientation {corner_orientation}")
        print(f"ud_down_edge_slice {ud_down_edge_slice}")
        print(f"left_right_edge_slice {left_right_edge_slice}")
        print(f"corner_tetrad {corner_tetrad}")
        print(f"permutation_parity {permutation_parity}")
        print(f"corner_tetrad_permutation_parity {corner_tetrad_permutation_parity}")
        print(f"corner_permutation {corner_permutation}")
        print(f"edge_permutation {edge_permutation}")
        return cubie, solution
