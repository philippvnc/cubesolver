from pybricks.tools import multitask, wait

from constants.direction import Direction
from constants.facelet import Facelet
from constants.rotation import Rotation
from constants.scan_position import ScanPosition
from constants.turn_amount import TurnAmount
from robot.actuators.colorsensorarm import ColorSensorArm
from robot.output.feedback import Feedback
from robot.sensors.color_reader import ColorReader
from solver.cube_manipulator import CubeManipulator
from solver.orientation_tracker import OrientationTracker


class CubeScanner:
    # order and position of full face scan of all edge and corner pieces on a clockwise rotating cube.
    # center is excluded
    _MEASUREMENTS = [(Facelet.UPPER_LEFT_CORNER, ScanPosition.CORNER),
                     (Facelet.LEFT_EDGE, ScanPosition.EDGE),
                     (Facelet.LOWER_LEFT_CORNER, ScanPosition.CORNER),
                     (Facelet.LOWER_EDGE, ScanPosition.EDGE),
                     (Facelet.LOWER_RIGHT_CORNER, ScanPosition.CORNER),
                     (Facelet.RIGHT_EDGE, ScanPosition.EDGE),
                     (Facelet.UPPER_RIGHT_CORNER, ScanPosition.CORNER),
                     (Facelet.UPPER_EDGE, ScanPosition.EDGE)]

    # initial rotation offset per face.
    # needed to account for faces rotating locally on their way to the scan position
    _FACE_ROTATION_OFFSET = [Rotation.UP,
                             Rotation.UP,
                             Rotation.RIGHT,
                             Rotation.RIGHT,
                             Rotation.RIGHT,
                             Rotation.DOWN]

    # where each facelet gets mapped when rotating the face counterclockwise
    _FACELET_COUNTERCLOCKWISE_ROTATION_MAP = [Facelet.LOWER_LEFT_CORNER,
                                              Facelet.LEFT_EDGE,
                                              Facelet.UPPER_LEFT_CORNER,
                                              Facelet.LOWER_EDGE,
                                              Facelet.CENTER,
                                              Facelet.UPPER_EDGE,
                                              Facelet.LOWER_RIGHT_CORNER,
                                              Facelet.RIGHT_EDGE,
                                              Facelet.UPPER_RIGHT_CORNER]
    _EIGHT_ANGLE = 45
    _ANGLE_TOLERANCE = 2

    def __init__(self,
                 arm: ColorSensorArm,
                 reader: ColorReader,
                 manipulator: CubeManipulator,
                 orientation_tracker: OrientationTracker,
                 feedback: Feedback):
        self._arm = arm
        self._reader = reader
        self._manipulator = manipulator
        self._orientation_tracker = orientation_tracker
        self._feedback = feedback

    async def scan(self) -> list[tuple[int, int, int]]:
        # scan each face and return in standard order
        # and return list of facelet color readouts as non-normalized hsv color space tuples.
        # the 2d map would look like this:
        #   U
        # L F R B
        #   D
        self._orientation_tracker.reset()
        await self._arm.tuck_away()
        cube_scan = []
        for face in range(6):
            cube_scan.extend(await self._scan_face(face))
        await self._manipulator.release_cube()
        print("cube scan: " + str(cube_scan))
        return cube_scan

    async def _scan_face(self,
                         face: int) -> list[tuple[int, int, int]]:
        await self._manipulator.move_face_to_top(face)
        await self._manipulator.hold_cube()
        await self._manipulator.release_cube()
        await self._arm.move_to_position(ScanPosition.CENTER)
        await self._reader.turn_on_lights()
        center_scan = await self._reader.read()
        self._feedback.activate_facelet(Facelet.CENTER)

        neutral_angle = self._manipulator.turntable.current_angle()
        multi_task_result = await multitask(
            self._manipulator.turntable.turn_slowly(direction=Direction.CLOCKWISE, amount=TurnAmount.FULL),
            self._scan_turning_cube(neutral_angle))
        _, face_scan = multi_task_result
        face_scan[Facelet.CENTER] = center_scan
        await self._reader.turn_off_lights()
        await self._arm.tuck_away()
        self._feedback.deactivate_facelets()
        return self._correct_face_rotation(face, face_scan)

    async def _scan_turning_cube(self, starting_angle: int) -> list[tuple[int, int, int]]:
        face_scan = [(0, 0, 0)] * 9
        for n_measurement, (facelet, scan_position) in enumerate(self._MEASUREMENTS):
            angle = await self._get_measurement_angle(n_measurement, starting_angle)
            multi_task_result = await multitask(self._arm.move_to_position(scan_position),
                                                self._read_facelet_at_angle(angle))
            _, facelet_scan = multi_task_result
            face_scan[facelet] = facelet_scan
            self._feedback.activate_facelet(facelet)
        return face_scan

    async def _get_measurement_angle(self, i: int, starting_angle: int) -> int:
        return starting_angle + ((i + 1) * self._EIGHT_ANGLE)

    async def _read_facelet_at_angle(self, target_angle: int) -> tuple[int, int, int]:
        while self._manipulator.turntable.current_angle() < target_angle - self._ANGLE_TOLERANCE:
            await wait(5)
        return await self._reader.read()

    def _correct_face_rotation(self,
                               face: int,
                               face_scan: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
        face_rotation = self._orientation_tracker.get_world_rotation_of_face_at_top()
        offset_face_rotation = Rotation.add(face_rotation, self._FACE_ROTATION_OFFSET[face])
        for _ in range(offset_face_rotation):
            face_scan = self._rotate_face_scan_counterclockwise(face_scan)
        print("rotation corrected face scan " + str(face_scan))
        return face_scan

    def _rotate_face_scan_counterclockwise(self,
                                           face_scan: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
        rotated_scan = [(0, 0, 0)] * 9
        for facelet in range(9):
            rotated_scan[self._FACELET_COUNTERCLOCKWISE_ROTATION_MAP[facelet]] = face_scan[facelet]
        return rotated_scan
