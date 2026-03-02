from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from cubie.encoder.phase_2_1_encoder import Phase21Encoder
from cubie.encoder.phase_2_2_encoder import Phase22Encoder
from cubie.encoder.phase_3_encoder import Phase3Encoder
from cubie.encoder.phase_4_1_encoder import Phase41Encoder
from cubie.encoder.phase_4_2_encoder import Phase42Encoder
from cubie.encoder.phase_4_3_encoder import Phase43Encoder
from cubie.encoder.phase_4_4_encoder import Phase44Encoder
from cubie.encoder.phase_4_5_encoder import Phase45Encoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from generated.co_pruning_table import CO_PRUNING_TABLE
from generated.eo_pruning_table import EO_PRUNING_TABLE
from generated.phase_2_1_pruning import PHASE_2_1_PRUNING
from generated.phase_2_2_pruning import PHASE_2_2_PRUNING
from generated.phase_3_pruning_table import PHASE_3_PRUNING_TABLE
from generated.phase_4_1_pruning_table import PHASE_4_1_PRUNING_TABLE
from generated.phase_4_2_pruning_table import PHASE_4_2_PRUNING_TABLE
from generated.phase_4_3_pruning_table import PHASE_4_3_PRUNING_TABLE
from generated.phase_4_4_pruning_table import PHASE_4_4_PRUNING_TABLE
from generated.phase_4_5_pruning_table import PHASE_4_5_PRUNING_TABLE


class Heuristic:

    def __init__(self):
        self._up_down_edge_slice_encoder = UpDownEdgeSliceEncoder()
        self._phase_2_1_encoder = Phase21Encoder()
        self._phase_2_2_encoder = Phase22Encoder()
        self._phase_3_encoder = Phase3Encoder()
        self._phase_4_1_encoder = Phase41Encoder()
        self._phase_4_2_encoder = Phase42Encoder()
        self._phase_4_3_encoder = Phase43Encoder()
        self._phase_4_4_encoder = Phase44Encoder()
        self._phase_4_5_encoder = Phase45Encoder()

    def phase_1_heuristic(self, cubie) -> int:
        return int(EO_PRUNING_TABLE[EdgeOrientationEncoder.from_cubie(cubie)])

    def phase_2_heuristic(self, cubie) -> int:
        index1 = self._phase_2_1_encoder.encode(cubie)
        index2 = self._phase_2_2_encoder.encode(cubie)
        co = CornerOrientationEncoder.from_cubie(cubie)
        return max(
            int(PHASE_2_1_PRUNING[index1]),
            int(PHASE_2_2_PRUNING[index2]),
            int(CO_PRUNING_TABLE[co])
        )

    def phase_3_heuristic(self, cubie) -> int:
        return int(PHASE_3_PRUNING_TABLE[self._phase_3_encoder.encode_cubie(cubie)])

    def phase_4_heuristic(self, cubie) -> int:
        index1 = self._phase_4_1_encoder.encode_cubie(cubie)
        index2 = self._phase_4_2_encoder.encode_cubie(cubie)
        index3 = self._phase_4_3_encoder.encode_cubie(cubie)
        index4 = self._phase_4_4_encoder.encode_cubie(cubie)
        index5 = self._phase_4_5_encoder.encode_cubie(cubie)
        return int(max(PHASE_4_1_PRUNING_TABLE[index1], PHASE_4_2_PRUNING_TABLE[index2], PHASE_4_3_PRUNING_TABLE[index3], PHASE_4_4_PRUNING_TABLE[index4], PHASE_4_5_PRUNING_TABLE[index5]))