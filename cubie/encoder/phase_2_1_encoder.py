from constants.cubie import Cubie
from cubie.encoder.partial_corner_orientation_encoder import PartialCornerOrientationEncoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder


class Phase21Encoder:
    """
    Combined encoder: CO_first3 x UD_full.
    Size: 27 * 495 = 13,365 entries.
    """

    def __init__(self):
        self._co_encoder = PartialCornerOrientationEncoder([Cubie.CORNER_URF, Cubie.CORNER_URL, Cubie.CORNER_ULB])
        self._ud_encoder = UpDownEdgeSliceEncoder()

    def encode(self, cubie) -> int:
        return self._co_encoder.from_cubie(cubie) * 495 + self._ud_encoder.encode_cubie(cubie)
