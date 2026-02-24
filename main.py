from pybricks.tools import run_task

from robot.robot import Robot


def main():
    robot = Robot()
    run_task(robot.solve_cubes_forever())


main()
