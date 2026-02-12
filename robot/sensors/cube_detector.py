from pybricks.pupdevices import UltrasonicSensor
from pybricks.tools import wait

from robot.output.feedback import Feedback


class CubeDetector:
    __PRESENCE_THRESHOLD: int = 120
    __ABSENCE_THRESHOLD: int = 100
    __NUMBER_OF_PRESENCE_READINGS: int = 30
    __TOLERANCE: int = 2

    def __init__(self,
                 sensor: UltrasonicSensor,
                 feedback: Feedback):
        self.__sensor = sensor
        self.__feedback = feedback

    def alignment_error(self):
        return self.__sensor.distance()

    def wait_for_cube_inserted(self) -> None:
        self.__sensor.lights.on(100)
        self.__feedback.cube_missing()
        print("Waiting for cube to be inserted")
        distances = [self.__PRESENCE_THRESHOLD] * self.__NUMBER_OF_PRESENCE_READINGS
        i = 0
        # wait until movement has settled for a second below presence threshold
        while True:
            distances[i] = self.__sensor.distance()
            i = (i + 1) % len(distances)
            if (
                    max(distances) - min(distances) <= self.__TOLERANCE
                    and min(distances) < self.__PRESENCE_THRESHOLD
            ):
                break
            wait(50)
        self.__sensor.lights.on(0)
        self.__feedback.cube_present()
        print("Cube is inserted")

    def wait_for_cube_removed(self) -> None:
        print("Waiting for cube to be removed")
        self.__feedback.cube_present()
        while self.__sensor.distance() < self.__ABSENCE_THRESHOLD:
            wait(50)
        self.__feedback.cube_missing()
        print("Cube is removed")
