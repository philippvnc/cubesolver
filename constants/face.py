from micropython_compat import const


class Face:
    UP = const(0)
    RIGHT = const(1)
    FRONT = const(2)
    DOWN = const(3)
    LEFT = const(4)
    BACK = const(5)

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
