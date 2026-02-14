from cubie.encoder.corner_tetrad_permutation_encoder import CornerTetradPermutationEncoder
from cubie.encoder.edge_tetrad_permutation_encoder import EdgeTetradPermutationEncoder


class Phase43Encoder:

    def __init__(self):
        self.__cycle_encoders = [CornerTetradPermutationEncoder([0, 2, 5, 7])
            , CornerTetradPermutationEncoder([1, 3, 5, 7]),
                                 EdgeTetradPermutationEncoder([8, 9, 10, 11])]

    def encode_cubie(self, cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        """
        htp = 0
        for i, encoder in enumerate(self.__cycle_encoders):
            htp += pow(24, i) * encoder.encode_cubie(cubie)
        return htp
