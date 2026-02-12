from algorithm.permutation_parity import PermutationParity


class CornerPermutationParityEncoder:

    @staticmethod
    def encode_corners(corners: list[tuple[int, int]]) -> int:
        """
        """
        return PermutationParity.determine([c for c, _ in corners])

    @staticmethod
    def encode_cubie(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        """
        return CornerPermutationParityEncoder.encode_corners(cubie[0])