from algorithm.subset_permutation import SubsetPermutation


class CornerTetradPermutationEncoder:

    def __init__(self, tetrad: list[int]):
        self.encoder = SubsetPermutation(tetrad)

    def encode_corners(self, corners: list[tuple[int, int]]) -> int:
        """
        """
        return self.encoder.encode([c for c, _ in corners])

    def encode_cubie(self, cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        """
        return self.encode_corners(cubie[0])