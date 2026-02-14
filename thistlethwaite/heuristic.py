from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from cubie.encoder.phase_3_encoder import Phase3Encoder
from cubie.encoder.phase_4_1_encoder import Phase41Encoder
from cubie.encoder.phase_4_2_encoder import Phase42Encoder
from cubie.encoder.phase_4_3_encoder import Phase43Encoder
from cubie.encoder.phase_4_4_encoder import Phase44Encoder
from cubie.encoder.phase_4_5_encoder import Phase45Encoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from generated.co_pruning_table import CO_PRUNING_TABLE
from generated.eo_pruning_table import EO_PRUNING_TABLE
from generated.phase_3_pruning_table import PHASE_3_PRUNING_TABLE
from generated.phase_4_1_pruning_table import PHASE_4_1_PRUNING_TABLE
from generated.phase_4_2_pruning_table import PHASE_4_2_PRUNING_TABLE
from generated.phase_4_3_pruning_table import PHASE_4_3_PRUNING_TABLE
from generated.phase_4_4_pruning_table import PHASE_4_4_PRUNING_TABLE
from generated.phase_4_5_pruning_table import PHASE_4_5_PRUNING_TABLE
from generated.ud_pruning_table import UD_PRUNING_TABLE


class Heuristic:

    def __init__(self):
        self.__up_down_edge_slice_encoder = UpDownEdgeSliceEncoder()
        self.__phase_3_encoder = Phase3Encoder()
        self.__phase_4_1_encoder = Phase41Encoder()
        self.__phase_4_2_encoder = Phase42Encoder()
        self.__phase_4_3_encoder = Phase43Encoder()
        self.__phase_4_4_encoder = Phase44Encoder()
        self.__phase_4_5_encoder = Phase45Encoder()

    def phase_1_heuristic(self, cubie) -> int:
        return int(EO_PRUNING_TABLE[EdgeOrientationEncoder.from_cubie(cubie)])

    def phase_2_heuristic(self, cubie) -> int:
        co = CornerOrientationEncoder.from_cubie(cubie)
        ud = self.__up_down_edge_slice_encoder.encode_cubie(cubie)
        return int(max(CO_PRUNING_TABLE[co], UD_PRUNING_TABLE[ud]))

    def phase_3_heuristic(self, cubie) -> int:
        return int(PHASE_3_PRUNING_TABLE[self.__phase_3_encoder.encode_cubie(cubie)])

    def phase_4_heuristic(self, cubie) -> int:
        index1 = self.__phase_4_1_encoder.encode_cubie(cubie)
        index2 = self.__phase_4_2_encoder.encode_cubie(cubie)
        index3 = self.__phase_4_3_encoder.encode_cubie(cubie)
        index4 = self.__phase_4_4_encoder.encode_cubie(cubie)
        index5 = self.__phase_4_5_encoder.encode_cubie(cubie)
        return int(max(PHASE_4_1_PRUNING_TABLE[index1], PHASE_4_2_PRUNING_TABLE[index2], PHASE_4_3_PRUNING_TABLE[index3], PHASE_4_4_PRUNING_TABLE[index4], PHASE_4_5_PRUNING_TABLE[index5]))