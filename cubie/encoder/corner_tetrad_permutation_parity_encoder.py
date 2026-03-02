from algorithm.permutation_parity import PermutationParity

class CornerTetradPermutationParityEncoder:
    """
    Encodes the permutation parity of the first corner tetrad (TETRAD_A) only.
    """

    @staticmethod
    def encode_corners(corners: list[tuple[int, int]]) -> int:
        """
        Compute the parity of the first tetrad of corners (indices 0..3 in positions).
        Normalizes corner IDs to 0..3 before computing parity.
        """
        # todo this seems wrong, why not use actual tetrad?
        tetrad = corners[:4]  # first tetrad positions
        tetrad_ids = [c for c, _ in tetrad]

        # map IDs to 0..3 preserving relative order
        unique_ids = sorted(tetrad_ids)
        normalized = [unique_ids.index(c) for c in tetrad_ids]

        return PermutationParity.determine(normalized)

    @staticmethod
    def encode_cubie(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        Returns the tetrad parity for the cubie.
        """
        return CornerTetradPermutationParityEncoder.encode_corners(cubie[0])