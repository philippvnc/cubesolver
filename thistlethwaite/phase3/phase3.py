from constants.move import Move
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.encoder.corner_tetrad_permutation_parity_encoder import CornerTetradPermutationParityEncoder
from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder


class Phase3:
    NAME = "Phase 3"
    ALLOWED_MOVES = [
        Move.U,
        Move.U_,
        Move.U2,
        Move.D,
        Move.D_,
        Move.D2,
        Move.L2,
        Move.R2,
        Move.F2,
        Move.B2,
    ]

    MAX_DEPTH = 13

    def __init__(self, lr_pruning_table: list[int], ct_pruning_table: list[int]):
        self.left_right_edge_slice_encoder = LeftRightEdgeSliceEncoder()
        self.corner_tetrad_encoder = CornerTetradEncoder()
        self.__lr_pruning_table = lr_pruning_table
        self.__ct_pruning_table = ct_pruning_table

    def phase_solved(self, cubie):
        return self.heuristic(cubie) == 0

    def heuristic(self, cubie) -> int:
        left_right_edge_slice = self.left_right_edge_slice_encoder.encode_cubie(cubie)
        corner_tetrad = self.corner_tetrad_encoder.encode_cubie(cubie)
        permutation_parity = CornerPermutationParityEncoder.encode_cubie(cubie)
        corner_tetrad_permutation_parity = CornerTetradPermutationParityEncoder.encode_cubie(cubie)

        return max(self.__lr_pruning_table[left_right_edge_slice],
                   self.__ct_pruning_table[corner_tetrad],
                   permutation_parity,
                   corner_tetrad_permutation_parity)
