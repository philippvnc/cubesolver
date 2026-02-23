from pybricks.tools import multitask

from constants.direction import Direction
from constants.facelet import Facelet
from constants.rotation import Rotation
from constants.scan_position import ScanPosition
from robot.actuators.colorsensorarm import ColorSensorArm
from robot.actuators.turntable import TurnAmount
from robot.output.feedback import Feedback
from robot.sensors.color_reader import ColorReader
from solver.cube_manipulator import CubeManipulator, Axis
from solver.orientation_tracker import OrientationTracker


class CubeScanner:
    # initial rotation offset per face
    __FACE_ROTATION_OFFSET = [Rotation.UP,
                              Rotation.UP,
                              Rotation.RIGHT,
                              Rotation.RIGHT,
                              Rotation.RIGHT,
                              Rotation.DOWN]

    # faces get scanned in natural order but for less physical movement facelets get scanned in this particular order
    # (start in the center facelet, then up, then move clockwise on the face)
    __FACELET_SCAN_ORDER = [Facelet.CENTER,
                            Facelet.UPPER_EDGE,
                            Facelet.UPPER_RIGHT_CORNER,
                            Facelet.RIGHT_EDGE,
                            Facelet.LOWER_RIGHT_CORNER,
                            Facelet.LOWER_EDGE,
                            Facelet.LOWER_LEFT_CORNER,
                            Facelet.LEFT_EDGE,
                            Facelet.UPPER_LEFT_CORNER]

    # the scan position for each facelet
    __FACELET_SCAN_POSITIONS = [ScanPosition.CORNER,
                                ScanPosition.EDGE,
                                ScanPosition.CORNER,
                                ScanPosition.EDGE,
                                ScanPosition.CENTER,
                                ScanPosition.EDGE,
                                ScanPosition.CORNER,
                                ScanPosition.EDGE,
                                ScanPosition.CORNER]

    # the relative amount of turn needed to scan each facelet
    __FACELET_SCAN_ROTATION_OFFSET = [TurnAmount.EIGHTH,
                                      TurnAmount.NONE,
                                      TurnAmount.EIGHTH,
                                      TurnAmount.EIGHTH,
                                      TurnAmount.NONE,
                                      TurnAmount.EIGHTH,
                                      TurnAmount.EIGHTH,
                                      TurnAmount.EIGHTH,
                                      TurnAmount.EIGHTH]

    # where each facelet gets mapped when rotating the face counterclockwise
    # needed to account for faces rotating locally on their way to the scan position
    __FACELET_COUNTERCLOCKWISE_ROTATION_MAP = [Facelet.LOWER_LEFT_CORNER,
                                               Facelet.LEFT_EDGE,
                                               Facelet.UPPER_LEFT_CORNER,
                                               Facelet.LOWER_EDGE,
                                               Facelet.CENTER,
                                               Facelet.UPPER_EDGE,
                                               Facelet.LOWER_RIGHT_CORNER,
                                               Facelet.RIGHT_EDGE,
                                               Facelet.UPPER_RIGHT_CORNER]

    def __init__(self,
                 arm: ColorSensorArm,
                 reader: ColorReader,
                 manipulator: CubeManipulator,
                 orientation_tracker: OrientationTracker,
                 feedback: Feedback):
        self.__arm = arm
        self.__reader = reader
        self.__manipulator = manipulator
        self.__orientation_tracker = orientation_tracker
        self.__feedback = feedback

    async def scan(self) -> list[tuple[int, int, int]]:
        # scan each face and return in standard order
        # and return list of facelet color readouts as non-normalized hsv color space tuples.
        # the 2d map would look like this:
        #   U
        # L F R B
        #   D
        self.__orientation_tracker.reset()
        await self.__arm.tuck_away()
        cube_scan = []
        for face in range(6):
            cube_scan.extend(await self.__scan_face(face))
        await self.__manipulator.release_cube()
        print("cube scan: " + str(cube_scan))
        return cube_scan

    async def __scan_face(self,
                    face: int) -> list[tuple[int, int, int]]:
        face_scan = [(0, 0, 0)] * 9
        await self.__manipulator.move_face_to_top(face)
        await self.__manipulator.release_cube()
        await self.__reader.turn_on_lights()
        for facelet in self.__FACELET_SCAN_ORDER:
            face_scan[facelet] = await self.__scan_facelet(facelet)
        await multitask(self.__arm.tuck_away(),
                        self.__manipulator.turn_cube(axis=Axis.VERTICAL,
                                                     direction=Direction.COUNTERCLOCKWISE,
                                                     amount=TurnAmount.EIGHTH))
        await self.__reader.turn_off_lights()
        self.__feedback.deactivate_facelets()
        return self.__correct_face_rotation(face, face_scan)

    async def __scan_facelet(self,
                       facelet: int) -> tuple[int, int, int]:
        await multitask(self.__arm.move_to_position(self.__FACELET_SCAN_POSITIONS[facelet]),
                        self.__manipulator.turn_cube(axis=Axis.VERTICAL,
                                                     direction=Direction.COUNTERCLOCKWISE,
                                                     amount=self.__FACELET_SCAN_ROTATION_OFFSET[facelet]))
        color = await self.__reader.read()
        self.__feedback.activate_facelet(facelet)
        return color

    def __correct_face_rotation(self,
                                face: int,
                                face_scan: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
        face_rotation = self.__orientation_tracker.get_world_rotation_of_face_at_top()
        offset_face_rotation = Rotation.add(face_rotation, self.__FACE_ROTATION_OFFSET[face])
        for _ in range(offset_face_rotation):
            face_scan = self.__rotate_face_scan_counterclockwise(face_scan)
        print("rotation corrected face scan " + str(face_scan))
        return face_scan

    def __rotate_face_scan_counterclockwise(self,
                                            face_scan: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
        rotated_scan = [(0, 0, 0)] * 9
        for facelet in range(9):
            rotated_scan[self.__FACELET_COUNTERCLOCKWISE_ROTATION_MAP[facelet]] = face_scan[facelet]
        return rotated_scan
