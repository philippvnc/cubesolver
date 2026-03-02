from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.encoder.corner_tetrad_permutation_parity_encoder import CornerTetradPermutationParityEncoder
from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder


class Phase3Encoder:

    def __init__(self):
        self._left_right_encoder = LeftRightEdgeSliceEncoder()
        self._corner_tetrad_encoder = CornerTetradEncoder()

    def encode_cubie(self, cubie):
        left_right_edge_slice = self._left_right_encoder.encode_cubie(cubie)
        corner_tetrad = self._corner_tetrad_encoder.encode_cubie(cubie)
        permutation_parity = CornerPermutationParityEncoder.encode_cubie(cubie)
        corner_tetrad_permutation_parity = CornerTetradPermutationParityEncoder.encode_cubie(cubie)
        return (((left_right_edge_slice * 70
                  + corner_tetrad) * 2
                 + permutation_parity) * 2
                + corner_tetrad_permutation_parity)
