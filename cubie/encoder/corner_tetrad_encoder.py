from algorithm.group_encoder import GroupEncoder


class CornerTetradEncoder:
    __TETRAD_CORNERS = [0, 2, 5, 7] # URF, ULB, DFL, DRB
    __POSSIBLE_CORNERS = [0, 1, 2, 3, 4, 5, 6, 7] # all corners

    def __init__(self):
        self.encoder = GroupEncoder(CornerTetradEncoder.__POSSIBLE_CORNERS,
                                    CornerTetradEncoder.__TETRAD_CORNERS)

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