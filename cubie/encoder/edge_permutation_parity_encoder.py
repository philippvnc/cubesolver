from algorithm.permutation_parity import PermutationParity


class EdgePermutationParityEncoder:

    @staticmethod
    def encode_corners(edges: list[tuple[int, int]]) -> int:
        """
        """
        return PermutationParity.determine([c for c, _ in edges])

    @staticmethod
    def encode_cubie(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        """
        return EdgePermutationParityEncoder.encode_corners(cubie[1])