from constants.move import Move
from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from thistlethwaite.phase import Phase


class Phase2(Phase):

    def __init__(self, heuristic=lambda cubie: 0):
        Phase.__init__(
            self,
            "Phase 2",
            [
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
            ],
            10,
            heuristic
        )
        self.up_down_edge_slice_encoder = UpDownEdgeSliceEncoder()

    def solved(self, cubie):
        return CornerOrientationEncoder.from_cubie(cubie) == 0 and self.up_down_edge_slice_encoder.encode_cubie(
            cubie) == 0
