from pybricks.tools import wait

from robot.actuators.arm import Arm
from robot.actuators.colorsensorarm import ColorSensorArm
from robot.actuators.turntable import Turntable
from algorithm.k_means import KMeans
from robot.hardware.hardware import Hardware
from robot.output.feedback import Feedback
from robot.sensors.color_reader import ColorReader
from robot.sensors.cube_detector import CubeDetector
from solver.cube_manipulator import CubeManipulator
from solver.cube_scanner import CubeScanner
from solver.cube_solver import CubeSolver
from cubie.cubie_converter import CubieConverter
from solver.label_predictor import LabelPredictor
from solver.orientation_tracker import OrientationTracker
from solver.solution_executor import SolutionExecutor
from solver.solution_generator import SolutionGenerator



def main():
    hardware = Hardware()

    wait(2000)

    feedback = Feedback(hardware.hub)
    detector = CubeDetector(hardware.distance_sensor, feedback)
    color_sensor_arm = ColorSensorArm(hardware.color_arm_motor)
    left_arm = Arm("left arm", hardware.left_arm_motor)
    right_arm = Arm("right arm", hardware.right_arm_motor)
    turntable = Turntable(hardware.turntable_motor, detector)
    color_reader = ColorReader(hardware.color_sensor, feedback)
    orientation_tracker = OrientationTracker()
    manipulator = CubeManipulator(turntable, left_arm, right_arm, orientation_tracker)
    scanner = CubeScanner(color_sensor_arm, color_reader, manipulator, orientation_tracker, feedback)
    solution_executor = SolutionExecutor(manipulator, feedback)
    cube_solver = CubeSolver(scanner, solution_executor, feedback)

    detector.wait_for_cube_inserted()
    turntable.calibrate_dynamically()

    while True:
        cube_solver.solve_cube()
        detector.wait_for_cube_removed()
        detector.wait_for_cube_inserted()

main()
