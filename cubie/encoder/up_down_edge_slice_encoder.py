from algorithm.group_encoder import GroupEncoder
from constants.cubie import Cubie


class UpDownEdgeSliceEncoder:

    def __init__(self):
        self.encoder = GroupEncoder(Cubie.EDGES,
                                    Cubie.UP_DOWN_EDGE_SLICE)

    def encode_edges(self, edges: list[tuple[int, int]]) -> int:
        """
        edges: [(cubie_id, orientation), ...] length 12
        gives int [0-494] encoding of how the U/D slices edges are positioned using combinatorics.
        0 means all 4 U/D slice edges are positioned in the U/D slice.
        ignores orientation.
        """
        return self.encoder.encode([e for e, _ in edges])

    def encode_cubie(self, cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        cubie: corners, [(cubie_id, orientation), ...] length 12
        gives int [0-494] encoding of how the U/D slices edges are positioned using combinatorics
        0 means all 4 U/D slice edges are positioned in the U/D slice
        ignores edge orientations and corners completely.
        """
        return self.encode_edges(cubie[1])
