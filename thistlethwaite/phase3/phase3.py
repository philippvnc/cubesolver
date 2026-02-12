from constants.move import Move
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.encoder.corner_tetrad_permutation_encoder import CornerTetradPermutationEncoder
from cubie.encoder.corner_tetrad_permutation_parity_encoder import CornerTetradPermutationParityEncoder
from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder
from thistlethwaite.offline.generated.ct_pruning_table import CT_PRUNING_TABLE
from thistlethwaite.offline.generated.lr_pruning_table import LR_PRUNING_TABLE


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

    def __init__(self):
        self.left_right_edge_slice_encoder = LeftRightEdgeSliceEncoder()
        self.corner_tetrad_encoder = CornerTetradEncoder()

    def phase_solved(self, cubie):
        return self.heuristic(cubie) == 0

    def heuristic(self, cubie) -> int:
        left_right_edge_slice = self.left_right_edge_slice_encoder.encode_cubie(cubie)
        corner_tetrad = self.corner_tetrad_encoder.encode_cubie(cubie)
        permutation_parity = CornerPermutationParityEncoder.encode_cubie(cubie)
        corner_tetrad_permutation_parity = CornerTetradPermutationParityEncoder.encode_cubie(cubie)

        return max(LR_PRUNING_TABLE[left_right_edge_slice], CT_PRUNING_TABLE[corner_tetrad], permutation_parity, corner_tetrad_permutation_parity)

