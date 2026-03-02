from constants.cubie import Cubie
from cubie.encoder.edge_tetrad_permutation_encoder import EdgeTetradPermutationEncoder


class EdgeHalfTurnPermutationEncoder:

    def __init__(self):
        self.__cycle_encoders = [EdgeTetradPermutationEncoder(Cubie.UP_DOWN_EDGE_SLICE)
            , EdgeTetradPermutationEncoder(Cubie.LEFT_RIGHT_EDGE_SLICE)
            , EdgeTetradPermutationEncoder(Cubie.FRONT_BACK_EDGE_SLICE)]

    def encode_cubie(self, cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        """
        htp = 0
        for i, encoder in enumerate(self.__cycle_encoders):
            htp += pow(24, i) * encoder.encode_cubie(cubie)
        return htp

