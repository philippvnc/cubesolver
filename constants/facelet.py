class Facelet:
    # facelets when looking straight at a face in local face space
    # 0 1 2
    # 3 4 5
    # 6 7 8
    UPPER_LEFT_CORNER = 0
    UPPER_EDGE = 1
    UPPER_RIGHT_CORNER = 2
    LEFT_EDGE = 3
    CENTER = 4
    RIGHT_EDGE = 5
    LOWER_LEFT_CORNER = 6
    LOWER_EDGE = 7
    LOWER_RIGHT_CORNER = 8

    @staticmethod
    def position(facelet: int) -> tuple[int, int] | None:
        if facelet == Facelet.UPPER_LEFT_CORNER:
            return 0, 0
        elif facelet == Facelet.UPPER_EDGE:
            return 0, 1
        elif facelet == Facelet.UPPER_RIGHT_CORNER:
            return 0, 2
        elif facelet == Facelet.LEFT_EDGE:
            return 1, 0
        elif facelet == Facelet.CENTER:
            return 1, 1
        elif facelet == Facelet.RIGHT_EDGE:
            return 1, 2
        elif facelet == Facelet.LOWER_LEFT_CORNER:
            return 2, 0
        elif facelet == Facelet.LOWER_EDGE:
            return 2, 1
        elif facelet == Facelet.LOWER_RIGHT_CORNER:
            return 2, 2
        else:
            return None
