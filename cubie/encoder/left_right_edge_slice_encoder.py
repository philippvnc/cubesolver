from algorithm.group_encoder import GroupEncoder


class LeftRightEdgeSliceEncoder:
    __LEFT_RIGHT_SLICE_EDGES = [1, 3, 7, 5] # UF, UB, DB, DF
    __POSSIBLE_SLICE_POSITIONS = [0, 1, 2, 3, 4, 5, 6, 7] # top and bottom layer

    def __init__(self):
        self.encoder = GroupEncoder(LeftRightEdgeSliceEncoder.__POSSIBLE_SLICE_POSITIONS, LeftRightEdgeSliceEncoder.__LEFT_RIGHT_SLICE_EDGES)

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