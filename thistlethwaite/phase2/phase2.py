from constants.move import Move
from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder


class Phase2:
    NAME = "Phase 2"
    # Phase 1 moves minus quarter F and B moves (B, B_, F, F_) since these flip edges
    ALLOWED_MOVES = [
        Move.U,
        Move.U_,
        Move.U2,
        Move.D,
        Move.D_,
        Move.D2,
        Move.L,
        Move.L_,
        Move.L2,
        Move.R,
        Move.R_,
        Move.R2,
        Move.F2,
        Move.B2,
    ]

    MAX_DEPTH = 10

    def __init__(self, heuristic = lambda cubie: 0):
        self.up_down_edge_slice_encoder = UpDownEdgeSliceEncoder()
        self.heuristic = heuristic

    def phase_solved(self, cubie):
        return CornerOrientationEncoder.from_cubie(cubie) == 0 and self.up_down_edge_slice_encoder.encode_cubie(cubie) == 0

