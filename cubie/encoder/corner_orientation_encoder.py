class CornerOrientationEncoder:

    @staticmethod
    def from_cubie_corners(corners: list[tuple[int, int]]) -> int:
        """
        corners: [(cubie_id, orientation), ...] length 8
        gives base 3 encoding of any corner orientation
        last orientation is left out because it can be inferred for valid cubies
        """
        co = 0
        for i in range(7):
            co = 3 * co + corners[i][1]
        return co

    @staticmethod
    def from_cubie(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> int:
        """
        corners: [(cubie_id, orientation), ...], edges length 8
        gives base 3 encoding of any corner orientation
        last orientation is left out because it can be inferred for valid cubies
        """
        return CornerOrientationEncoder.from_cubie_corners(cubie[0])

    @staticmethod
    def to_cubie_corner_orientations(co: int) -> list[int]:
        """
        co: int
        gives the valid cubie corner orientation list that matches the given co state
        the last corner orientation in the list is inferred by creating a 0 sum
        """
        corner_oris = [0] * 8
        ori_sum = 0

        for i in reversed(range(7)):
            ori = co % 3
            co //= 3
            corner_oris[i] = ori
            ori_sum += ori

        corner_oris[7] = (-ori_sum) % 3
        return corner_oris

    @staticmethod
    def to_cubie(co: int) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        """
        co: int
        gives a possible full cubie for the given co state
        """
        corner_orientations = CornerOrientationEncoder.to_cubie_corner_orientations(co)
        return [(corner, corner_orientations[corner]) for corner in range(8)], [(edge, 0) for edge in range(12)]