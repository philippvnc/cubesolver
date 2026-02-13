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

    def __init__(self, heuristic = lambda cubie : 0):
        self.left_right_edge_slice_encoder = LeftRightEdgeSliceEncoder()
        self.corner_tetrad_encoder = CornerTetradEncoder()
        self.heuristic = heuristic

    def phase_solved(self, cubie):
        return (self.left_right_edge_slice_encoder.encode_cubie(cubie) == 0 and
                self.corner_tetrad_encoder.encode_cubie(cubie) == 0 and
                CornerPermutationParityEncoder.encode_cubie(cubie) == 0 and
                CornerTetradPermutationParityEncoder.encode_cubie(cubie) == 0)
