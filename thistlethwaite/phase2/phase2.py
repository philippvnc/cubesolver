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

    def __init__(self, co_pruning_table: list[int], ud_pruning_table: list[int]):
        self.up_down_edge_slice_encoder = UpDownEdgeSliceEncoder()
        self.__co_pruning_table = co_pruning_table
        self.__ud_pruning_table = ud_pruning_table

    def phase_solved(self, cubie):
        return self.heuristic(cubie) == 0

    def heuristic(self, cubie) -> int:
        co = CornerOrientationEncoder.from_cubie(cubie)
        ud = self.up_down_edge_slice_encoder.encode_cubie(cubie)
        return max(self.__co_pruning_table[co], self.__ud_pruning_table[ud])

