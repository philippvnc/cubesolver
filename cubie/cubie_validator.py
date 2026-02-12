from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.edge_permutation_parity_encoder import EdgePermutationParityEncoder


class CubieValidator:

    @staticmethod
    def valid(cubie) -> bool:
        if not CubieValidator.__corner_orientation_is_valid(cubie):
            return False
        if not CubieValidator.__edge_orientation_is_valid(cubie):
            return False
        if not CubieValidator.__parities_are_equal(cubie):
            return False
        return True

    @staticmethod
    def __parities_are_equal(cubie):
        return CornerPermutationParityEncoder.encode_cubie(cubie) == EdgePermutationParityEncoder.encode_cubie(cubie)

    @staticmethod
    def __corner_orientation_is_valid(cubie):
        return CubieValidator.__summed_orientation_is_multiple_of(cubie[0], 3)

    @staticmethod
    def __edge_orientation_is_valid(cubie):
        return CubieValidator.__summed_orientation_is_multiple_of(cubie[1], 2)

    @staticmethod
    def __summed_orientation_is_multiple_of(cubies: list[tuple[int, int]], divider: int) -> bool:
        summed_orientations = 0
        for _, orientation in cubies:
            summed_orientations += orientation
        return summed_orientations % divider == 0