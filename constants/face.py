class Face:
    UP = 0
    RIGHT = 1
    FRONT = 2
    DOWN = 3
    LEFT = 4
    BACK = 5

    @staticmethod
    def mirror(face: int) -> int:
        return (face + 3) % 6

    @staticmethod
    def name(face: int) -> str:
        if face == Face.FRONT:
            return "FRONT"
        elif face == Face.BACK:
            return "BACK "
        elif face == Face.LEFT:
            return "LEFT "
        elif face == Face.RIGHT:
            return "RIGHT"
        elif face == Face.UP:
            return "UP   "
        elif face == Face.DOWN:
            return "DOWN "
        return "INVALID"

    @staticmethod
    def short_name(face: int) -> str:
        return Face.name(face)[0]
