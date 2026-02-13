from cubie.encoder.corner_half_turn_permutation_encoder import CornerHalfTurnPermutationEncoder
from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.encoder.corner_tetrad_permutation_parity_encoder import CornerTetradPermutationParityEncoder
from cubie.encoder.edge_half_turn_permutation_encoder import EdgeHalfTurnPermutationEncoder
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from generated.co_pruning_table import CO_PRUNING_TABLE
from generated.cp_pruning_table import CP_PRUNING_TABLE
from generated.ct_pruning_table import CT_PRUNING_TABLE
from generated.eo_pruning_table import EO_PRUNING_TABLE
from generated.ep_pruning_table import EP_PRUNING_TABLE
from generated.ud_pruning_table import UD_PRUNING_TABLE


class Heuristic:

    def __init__(self):
        self.__left_right_edge_slice_encoder = LeftRightEdgeSliceEncoder()
        self.__corner_tetrad_encoder = CornerTetradEncoder()
        self.__corner_half_turn_permutation_encoder = CornerHalfTurnPermutationEncoder()
        self.__edge_half_turn_permutation_encoder = EdgeHalfTurnPermutationEncoder()
        self.__up_down_edge_slice_encoder = UpDownEdgeSliceEncoder()

    def phase_1_heuristic(self, cubie) -> int:
        eo = EdgeOrientationEncoder.from_cubie(cubie)
        return EO_PRUNING_TABLE[eo]

    def phase_2_heuristic(self, cubie) -> int:
        co = CornerOrientationEncoder.from_cubie(cubie)
        ud = self.__up_down_edge_slice_encoder.encode_cubie(cubie)
        return max(CO_PRUNING_TABLE[co], UD_PRUNING_TABLE[ud])

    def phase_3_heuristic(self, cubie) -> int:
        left_right_edge_slice = self.__left_right_edge_slice_encoder.encode_cubie(cubie)
        corner_tetrad = self.__corner_tetrad_encoder.encode_cubie(cubie)
        permutation_parity = CornerPermutationParityEncoder.encode_cubie(cubie)
        corner_tetrad_permutation_parity = CornerTetradPermutationParityEncoder.encode_cubie(cubie)
        return max(CO_PRUNING_TABLE[left_right_edge_slice],
                   CT_PRUNING_TABLE[corner_tetrad],
                   permutation_parity,
                   corner_tetrad_permutation_parity)

    def phase_4_heuristic(self, cubie) -> int:
        cp = self.__corner_half_turn_permutation_encoder.encode_cubie(cubie)
        ep = self.__edge_half_turn_permutation_encoder.encode_cubie(cubie)
        return max(CP_PRUNING_TABLE[cp], EP_PRUNING_TABLE[ep])