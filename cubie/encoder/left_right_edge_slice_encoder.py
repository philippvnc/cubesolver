from algorithm.group_encoder import GroupEncoder
from constants.cubie import Cubie


class LeftRightEdgeSliceEncoder:

    def __init__(self):
        self.encoder = GroupEncoder(Cubie.UP_DOWN_EDGE_SLICE + Cubie.FRONT_BACK_EDGE_SLICE,
                                    Cubie.LEFT_RIGHT_EDGE_SLICE)

    def encode_edges(self, edges: list[tuple[int, int]]) -> int:
        """
        edges: [(cubie_id, orientation), ...] length 12
        gives int [0-69] encoding of how the L/R slices edges are positioned using combinatorics.
        0 means all 4 L/R slice edges are positioned in the L/R slice.
        assumes U/D slice edges are positioned in the U/D slice.
        ignores edge orientations.
        """
        return self.encoder.encode([e for e, _ in edges])

    def encode_cubie(self, cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        cubie: corners, [(cubie_id, orientation), ...] length 12
        gives int [0-69] encoding of how the L/R slices edges are positioned using combinatorics.
        0 means all 4 L/R slice edges are positioned in the L/R slice.
        assumes U/D slice edges are positioned in the U/D slice.
        ignores edge orientations and cubie corners.
        """
        return self.encode_edges(cubie[1])