from micropython_compat import const


class Rotation:
    # used to encode the rotation of a face
    UP = const(0)
    RIGHT = const(1)
    DOWN = const(2)
    LEFT = const(3)

    @staticmethod
    def add(rotation_a: int, rotation_b: int) -> int:
        return (rotation_a + rotation_b) % 4

    @staticmethod
    def rotate_clockwise(rotation: int) -> int:
        return Rotation.add(rotation, Rotation.RIGHT)
