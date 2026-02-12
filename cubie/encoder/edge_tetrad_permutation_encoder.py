from algorithm.subset_permutation import SubsetPermutation


class EdgeTetradPermutationEncoder:

    def __init__(self, tetrad: list[int]):
        self.encoder = SubsetPermutation(tetrad)

    def encode_edges(self, edges: list[tuple[int, int]]) -> int:
        """
        """
        return self.encoder.encode([e for e, _ in edges])

    def encode_cubie(self, cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        """
        return self.encode_edges(cubie[1])