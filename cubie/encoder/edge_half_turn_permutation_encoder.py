from cubie.encoder.edge_tetrad_permutation_encoder import EdgeTetradPermutationEncoder


class EdgeHalfTurnPermutationEncoder:

    def __init__(self):
        self.__cycle_encoders = [EdgeTetradPermutationEncoder([8, 9, 10, 11])
            , EdgeTetradPermutationEncoder([1, 3, 5, 7])
            , EdgeTetradPermutationEncoder([0, 2, 4, 6])]

    def encode_cubie(self, cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        """
        htp = 0
        for i, encoder in enumerate(self.__cycle_encoders):
            htp += pow(24, i) * encoder.encode_cubie(cubie)
        return htp

