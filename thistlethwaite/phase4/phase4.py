from constants.move import Move
from cubie.encoder.corner_half_turn_permutation_encoder import CornerHalfTurnPermutationEncoder
from cubie.encoder.edge_half_turn_permutation_encoder import EdgeHalfTurnPermutationEncoder


class Phase4:
    NAME = "Phase 4"
    ALLOWED_MOVES = [
        Move.U2,
        Move.D2,
        Move.L2,
        Move.R2,
        Move.F2,
        Move.B2,
    ]

    MAX_DEPTH = 15

    def __init__(self, cp_pruning_table: list[int], ep_pruning_table: list[int]):
        self.__cp_pruning_table = cp_pruning_table
        self.__ep_pruning_table = ep_pruning_table

    def phase_solved(self, cubie):
        return self.heuristic(cubie) == 0

    def heuristic(self, cubie) -> int:
        cp = CornerHalfTurnPermutationEncoder().encode_cubie(cubie)
        ep = EdgeHalfTurnPermutationEncoder().encode_cubie(cubie)
        return max(self.__cp_pruning_table[cp], self.__ep_pruning_table[ep])
