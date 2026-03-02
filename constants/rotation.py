class Rotation:
    # used to encode the rotation of a face
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @staticmethod
    def add(rotation_a: int, rotation_b: int) -> int:
        return (rotation_a + rotation_b) % 4

    @staticmethod
    def rotate_clockwise(rotation: int) -> int:
        return Rotation.add(rotation, Rotation.RIGHT)
