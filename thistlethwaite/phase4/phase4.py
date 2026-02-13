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

    def __init__(self, heuristic = lambda cubie: 0):
        self.heuristic = heuristic
        self.__cp_encoder = CornerHalfTurnPermutationEncoder()
        self.__ep_encoder = EdgeHalfTurnPermutationEncoder()

    def phase_solved(self, cubie):
        return self.__cp_encoder.encode_cubie(cubie) == 0 and self.__ep_encoder.encode_cubie(cubie) == 0
