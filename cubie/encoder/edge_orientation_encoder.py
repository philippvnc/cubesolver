class EdgeOrientationEncoder:

    @staticmethod
    def from_cubie_edges(edges: list[tuple[int, int]]) -> int:
        """
        edges: [(cubie_id, orientation), ...] length 12
        gives base 2 encoding of any edge orientation
        last orientation is left out because it can be inferred for valid cubies
        """
        eo = 0
        for i in range(11):
            eo = (eo << 1) | edges[i][1]
        return eo

    @staticmethod
    def from_cubie(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        edges: corners, [(cubie_id, orientation), ...] length 12
        gives base 2 encoding of any edge orientation
        last orientation is left out because it can be inferred for valid cubies
        """
        return EdgeOrientationEncoder.from_cubie_edges(cubie[1])

    @staticmethod
    def to_cubie_edge_orientation(eo: int) -> list[int]:
        """
        eo: int
        gives the valid cubie edge orientation list that matches the given eo state
        the last edge orientation in the list is inferred by creating a 0 sum
        """
        edges = [0 for _ in range(12)]
        ori_sum = 0

        for i in reversed(range(11)):
            ori = eo & 1
            eo >>= 1
            edges[i] = ori
            ori_sum += ori

        edges[11] = ori_sum % 2
        return edges

    @staticmethod
    def to_cubie(eo: int) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        """
        eo: int
        gives a possible full cubie for the given eo state
        """
        edge_orientations = EdgeOrientationEncoder.to_cubie_edge_orientation(eo)
        return [(corner, 0) for corner in range(8)], [(edge, edge_orientations[edge]) for edge in range(12)]