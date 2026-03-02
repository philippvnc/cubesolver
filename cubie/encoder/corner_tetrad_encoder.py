from algorithm.group_encoder import GroupEncoder
from constants.cubie import Cubie


class CornerTetradEncoder:

    def __init__(self):
        self.encoder = GroupEncoder(Cubie.CORNERS,
                                    Cubie.CORNER_TETRAD_A)

    def encode_corners(self, corners: list[tuple[int, int]]) -> int:
        """
        corners: [(cubie_id, orientation), ...] length 8
        gives int [0-69] encoding of how the corners are positioned in the correct tetrad using combinatorics.
        0 means all corners are positioned in their respective tetrad.
        ignores corner orientations.
        """
        return self.encoder.encode([c for c, _ in corners])

    def encode_cubie(self, cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        cubie: corners, [(cubie_id, orientation), ...] length 8
        gives int [0-69] encoding of how the corners are positioned in the correct tetrad using combinatorics.
        0 means all corners are positioned in their respective tetrad.
        ignores edge orientations and cubie corners.
        """
        return self.encode_corners(cubie[0])
