class Direction:
    CLOCKWISE = 1
    COUNTERCLOCKWISE = -1

    @staticmethod
    def name(direction: int) -> str:
        if direction == Direction.CLOCKWISE:
            return "CLOCKWISE"
        elif direction == Direction.COUNTERCLOCKWISE:
            return "COUNTERCLOCKWISE"
        else:
            return "INVALID"