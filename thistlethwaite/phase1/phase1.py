from constants.move import Move
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder


class Phase1:
    NAME = "Phase 1"
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
        Move.F,
        Move.F_,
        Move.F2,
        Move.B,
        Move.B_,
        Move.B2,
    ]

    MAX_DEPTH = 7

    def __init__(self, heuristic = lambda cubie : 0):
        self.heuristic = heuristic

    def phase_solved(self, cubie):
        return EdgeOrientationEncoder.from_cubie(cubie) == 0

