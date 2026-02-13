from constants.move import Move
from cubie.encoder.corner_half_turn_permutation_encoder import CornerHalfTurnPermutationEncoder
from cubie.encoder.edge_half_turn_permutation_encoder import EdgeHalfTurnPermutationEncoder
from thistlethwaite.phase import Phase


class Phase4(Phase):

    def __init__(self, heuristic=lambda cubie: 0):
        Phase.__init__(
            self,
            "Phase 4",
            [
                Move.U2,
                Move.D2,
                Move.L2,
                Move.R2,
                Move.F2,
                Move.B2,
            ],
            15,
            heuristic
        )
        self.__cp_encoder = CornerHalfTurnPermutationEncoder()
        self.__ep_encoder = EdgeHalfTurnPermutationEncoder()

    def solved(self, cubie):
        return self.__cp_encoder.encode_cubie(cubie) == 0 and self.__ep_encoder.encode_cubie(cubie) == 0
