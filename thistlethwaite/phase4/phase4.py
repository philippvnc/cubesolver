from constants.move import Move
from cubie.encoder.corner_half_turn_permutation_encoder import CornerHalfTurnPermutationEncoder
from cubie.encoder.edge_half_turn_permutation_encoder import EdgeHalfTurnPermutationEncoder
from thistlethwaite.offline.generated.cp_pruning_table import CP_PRUNING_TABLE
from thistlethwaite.offline.generated.ep_pruning_table import EP_PRUNING_TABLE


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

    def __init__(self):
        pass

    def phase_solved(self, cubie):
        return self.heuristic(cubie) == 0

    # todo understand why cp in this heuristic has values that do not come up in bfs search when building the pruning table
    # ideas: write more / better tests? try different corner half turn permutation encoder? look at cubes that are outside the known range and reconstruct index?

    def heuristic(self, cubie) -> int:
        cp = CornerHalfTurnPermutationEncoder().encode_cubie(cubie)
        ep = EdgeHalfTurnPermutationEncoder().encode_cubie(cubie)
        heuristic = max(CP_PRUNING_TABLE[cp], EP_PRUNING_TABLE[ep])
        if CP_PRUNING_TABLE[cp] == -1 :
            print("-----------------")
            print(f"found corner half turn permutation encoding out of known pruning indexes:")
            print(f"cubie {cubie}")
            print(f"cp_min_distance {cp}: {CP_PRUNING_TABLE[cp]}")
            print(f"ep_min_distance {ep}: {EP_PRUNING_TABLE[ep]}")
            print(f"heuristic: {heuristic}")
        return heuristic

