from constants.cubie import Cubie
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.edge_permutation_parity_encoder import EdgePermutationParityEncoder


class CubieValidator:

    @staticmethod
    def valid(cubie) -> bool:
        if not CubieValidator._corner_orientation_is_valid(cubie):
            return False
        if not CubieValidator._edge_orientation_is_valid(cubie):
            return False
        if not CubieValidator._parities_are_equal(cubie):
            return False
        return True

    @staticmethod
    def _parities_are_equal(cubie):
        return CornerPermutationParityEncoder.encode_cubie(cubie) == EdgePermutationParityEncoder.encode_cubie(cubie)

    @staticmethod
    def _corner_orientation_is_valid(cubie):
        return CubieValidator._summed_orientation_is_multiple_of(cubie[0], Cubie.N_CORNER_ORIENTATIONS)

    @staticmethod
    def _edge_orientation_is_valid(cubie):
        return CubieValidator._summed_orientation_is_multiple_of(cubie[1], Cubie.N_EDGE_ORIENTATIONS)

    @staticmethod
    def _summed_orientation_is_multiple_of(cubies: list[tuple[int, int]], divider: int) -> bool:
        summed_orientations = 0
        for _, orientation in cubies:
            summed_orientations += orientation
        return summed_orientations % divider == 0