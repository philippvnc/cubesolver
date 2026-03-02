from micropython_compat import const


class Direction:
    CLOCKWISE = const(1)
    COUNTERCLOCKWISE = const(-1)

    @staticmethod
    def name(direction: int) -> str:
        if direction == Direction.CLOCKWISE:
            return "CLOCKWISE"
        elif direction == Direction.COUNTERCLOCKWISE:
            return "COUNTERCLOCKWISE"
        else:
            return "INVALID"