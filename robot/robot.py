from micropython_compat import const
from pybricks.tools import wait

from robot.actuators.arm import Arm
from robot.actuators.colorsensorarm import ColorSensorArm
from robot.actuators.turntable import Turntable
from robot.hardware.hardware import Hardware
from robot.output.feedback import Feedback
from robot.sensors.color_reader import ColorReader
from robot.sensors.cube_detector import CubeDetector
from solver.cube_manipulator import CubeManipulator
from solver.cube_scanner import CubeScanner
from solver.cube_solver import CubeSolver
from solver.orientation_tracker import OrientationTracker
from solver.solution_executor import SolutionExecutor


class Robot:
    __START_UP_DELAY_MS = const(2000)

    def __init__(self):
        hardware = Hardware()
        wait(Robot.__START_UP_DELAY_MS)

        feedback = Feedback(hardware.hub)
        self.__detector = CubeDetector(hardware.distance_sensor, feedback)
        color_sensor_arm = ColorSensorArm(hardware.color_arm_motor)
        left_arm = Arm("left arm", hardware.left_arm_motor)
        right_arm = Arm("right arm", hardware.right_arm_motor)
        self.turntable = Turntable(hardware.turntable_motor, self.__detector)
        color_reader = ColorReader(hardware.color_sensor, feedback)
        orientation_tracker = OrientationTracker()
        manipulator = CubeManipulator(self.turntable, left_arm, right_arm, orientation_tracker)
        scanner = CubeScanner(color_sensor_arm, color_reader, manipulator, orientation_tracker, feedback)
        solution_executor = SolutionExecutor(manipulator, feedback)
        self.__cube_solver = CubeSolver(scanner, solution_executor, feedback)

    async def solve_cubes_forever(self):
        await self.__detector.wait_for_cube_inserted()
        await self.turntable.calibrate_dynamically()

        while True:
            await self.__cube_solver.solve_cube()
            await self.__detector.wait_for_cube_removed()
            await self.__detector.wait_for_cube_inserted()
