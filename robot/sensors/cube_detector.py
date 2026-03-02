from micropython_compat import const
from pybricks.pupdevices import UltrasonicSensor
from pybricks.tools import wait

from robot.output.feedback import Feedback


class CubeDetector:
    MINIMAL_ALIGNMENT_DISTANCE: int = const(40)
    _PRESENCE_THRESHOLD: int = const(85)
    _ABSENCE_THRESHOLD: int = const(100)
    _NUMBER_OF_PRESENCE_READINGS: int = const(30)
    _TOLERANCE: int = const(2)
    _MEASUREMENT_INTERVAL_MILLIS: int = const(50)

    def __init__(self,
                 sensor: UltrasonicSensor,
                 feedback: Feedback):
        self._sensor = sensor
        self._feedback = feedback

    async def alignment_error(self):
        return await self._sensor.distance()

    async def wait_for_cube_inserted(self) -> None:
        await self._sensor.lights.on(100)
        self._feedback.cube_missing()
        print("Waiting for cube to be inserted")
        distances = [self._PRESENCE_THRESHOLD] * self._NUMBER_OF_PRESENCE_READINGS
        reading = 0
        # wait until movement has settled for a second below presence threshold
        while True:
            distances[reading] = await self._sensor.distance()
            reading = (reading + 1) % self._NUMBER_OF_PRESENCE_READINGS
            if self._is_distance_stable(distances) and self._is_cube_present(distances):
                break
            await self._wait_measurement_interval()
        await self._sensor.lights.on(0)
        self._feedback.cube_present()
        print("Cube is inserted")

    async def _wait_measurement_interval(self) -> None:
        await wait(self._MEASUREMENT_INTERVAL_MILLIS)

    def _is_cube_present(self, distances: list[int]) -> bool:
        return min(distances) < self._PRESENCE_THRESHOLD

    def _is_distance_stable(self, distances: list[int]) -> bool:
        return max(distances) - min(distances) <= self._TOLERANCE

    async def wait_for_cube_removed(self) -> None:
        print("Waiting for cube to be removed")
        self._feedback.cube_present()
        while await self._sensor.distance() < self._ABSENCE_THRESHOLD:
            await self._wait_measurement_interval()
        self._feedback.cube_missing()
        print("Cube is removed")
