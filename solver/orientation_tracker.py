from constants.axis import Axis
from constants.direction import Direction
from constants.face import Face
from constants.rotation import Rotation


class OrientationTracker:
    _CLOCKWISE_POSITION_CYCLES = {
        Axis.VERTICAL: (
            Face.RIGHT,
            Face.BACK,
            Face.LEFT,
            Face.FRONT,
        ),
        Axis.HORIZONTAL: (
            Face.RIGHT,
            Face.UP,
            Face.LEFT,
            Face.DOWN,
        ),
    }

    def __init__(self):
        self._face_at_position = list(range(6))
        self._local_rotation_of_face = [0 for _ in range(6)]
        self._world_rotation = 0

    def reset(self):
        self._face_at_position = list(range(6))
        self._local_rotation_of_face = [0 for _ in range(6)]
        self._world_rotation = 0

    def get_position_of_face(self,
                             face: int) -> int:
        return self._face_at_position.index(face)

    def get_local_rotation_of_face(self, face: int) -> int:
        return self._local_rotation_of_face[face]

    def get_world_rotation_of_face_at_top(self) -> int:
        return Rotation.add(self.get_local_rotation_of_face(self._face_at_position[Face.UP]),
                            self._world_rotation)

    def track_turn(self,
                   axis: int,
                   direction: int,
                   amount: int) -> None:
        for _ in range((1 if direction == Direction.CLOCKWISE else 3) * amount):
            self._apply_position_update(self._CLOCKWISE_POSITION_CYCLES[axis])
            self._apply_local_rotation_update(self._CLOCKWISE_POSITION_CYCLES[axis])
            self._apply_world_rotation_update(axis)

    def _print_current_positions(self):
        face_names = [Face.name(self._face_at_position[position]) for position in range(6)]
        print("current face position:")
        print("      " + face_names[Face.UP])
        print(face_names[Face.LEFT] + " " + face_names[Face.FRONT] + " " + face_names[Face.RIGHT] + " " + face_names[
            Face.BACK])
        print("      " + face_names[Face.DOWN])

    def _apply_position_update(self,
                               cycle: tuple[int, ...]) -> None:
        former_face_at_cycle_start = self._face_at_position[cycle[0]]
        for i in range(len(cycle) - 1):
            self._face_at_position[cycle[i]] = self._face_at_position[cycle[i + 1]]
        self._face_at_position[cycle[-1]] = former_face_at_cycle_start

    def _apply_local_rotation_update(self,
                                     cycle: tuple[int, ...]) -> None:
        for position in cycle:
            face = self._face_at_position[position]
            current_local_rotation = self._local_rotation_of_face[face]
            self._local_rotation_of_face[face] = Rotation.rotate_clockwise(current_local_rotation)

    def _apply_world_rotation_update(self, axis: int):
        if axis == Axis.VERTICAL:
            self._world_rotation = Rotation.rotate_clockwise(self._world_rotation)



