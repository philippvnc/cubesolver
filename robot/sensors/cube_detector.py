from micropython_compat import const
from pybricks.pupdevices import UltrasonicSensor
from pybricks.tools import wait

from robot.output.feedback import Feedback


class CubeDetector:
    MINIMAL_ALIGNMENT_DISTANCE: int = const(40)
    __PRESENCE_THRESHOLD: int = const(85)
    __ABSENCE_THRESHOLD: int = const(100)
    __NUMBER_OF_PRESENCE_READINGS: int = const(30)
    __TOLERANCE: int = const(2)
    __MEASUREMENT_INTERVAL_MILLIS: int = const(50)

    def __init__(self,
                 sensor: UltrasonicSensor,
                 feedback: Feedback):
        self.__sensor = sensor
        self.__feedback = feedback

    async def alignment_error(self):
        return await self.__sensor.distance()

    async def wait_for_cube_inserted(self) -> None:
        await self.__sensor.lights.on(100)
        self.__feedback.cube_missing()
        print("Waiting for cube to be inserted")
        distances = [self.__PRESENCE_THRESHOLD] * self.__NUMBER_OF_PRESENCE_READINGS
        reading = 0
        # wait until movement has settled for a second below presence threshold
        while True:
            distances[reading] = await self.__sensor.distance()
            reading = (reading + 1) % self.__NUMBER_OF_PRESENCE_READINGS
            if self.__is_distance_stable(distances) and self.__is_cube_present(distances):
                break
            await self.__wait_measurement_interval()
        await self.__sensor.lights.on(0)
        self.__feedback.cube_present()
        print("Cube is inserted")

    async def __wait_measurement_interval(self) -> None:
        await wait(self.__MEASUREMENT_INTERVAL_MILLIS)

    def __is_cube_present(self, distances: list[int]) -> bool:
        return min(distances) < self.__PRESENCE_THRESHOLD

    def __is_distance_stable(self, distances: list[int]) -> bool:
        return max(distances) - min(distances) <= self.__TOLERANCE

    async def wait_for_cube_removed(self) -> None:
        print("Waiting for cube to be removed")
        self.__feedback.cube_present()
        while await self.__sensor.distance() < self.__ABSENCE_THRESHOLD:
            await self.__wait_measurement_interval()
        self.__feedback.cube_missing()
        print("Cube is removed")
