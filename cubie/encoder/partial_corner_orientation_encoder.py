class PartialCornerOrientationEncoder:
    """
    Encodes orientation of a subset of corners defined by indices.
    Range: 0 to 3^len(indices) - 1.
    0 = all specified corners correctly oriented.
    """

    def __init__(self, indices: list[int]):
        self._indices = indices

    def from_cubie_corners(self, corners: list[tuple[int, int]]) -> int:
        co = 0
        for i in self._indices:
            co = 3 * co + corners[i][1]
        return co

    def from_cubie(self, cubie) -> int:
        return self.from_cubie_corners(cubie[0])