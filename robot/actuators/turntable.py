from micropython_compat import const
from pybricks.pupdevices import Motor

from robot.sensors.cube_detector import CubeDetector


class Turntable:
    # unfortunately this value depends on axle and gear positions
    _INITIAL_PHYSICAL_ANGLE_OFFSET = const(68)
    _CALIBRATION_INCREMENT = const(120)
    _ANGLE_PER_AMOUNT = const(90)
    _OVERTURN_ANGLE = const(2)
    _NEUTRAL_OVERTURN_STATE = const(0)

    def __init__(self,
                 motor: Motor,
                 detector: CubeDetector,
                 speed: int = const(800),
                 slow_speed: int = const(135)) -> None:
        self._motor = motor
        self._detector = detector
        self._speed = speed
        self._slow_speed = slow_speed
        self._overturn_state = self._NEUTRAL_OVERTURN_STATE

    async def calibrate_dynamically(self):
        print("calibrating turntable ...")
        best_error = 10 ** 9
        best_pos = 0

        # 1) go to initial reference
        await self._motor.run_target(self._speed,
                                     self._INITIAL_PHYSICAL_ANGLE_OFFSET)

        for pos in range(3):
            error = await self._detector.alignment_error()

            if error == self._detector.MINIMAL_ALIGNMENT_DISTANCE:
                return

            if error < best_error:
                best_error = error
                best_pos = pos

            # only move for the first two positions
            if pos < 2:
                await self._motor.run_angle(self._speed,
                                            self._CALIBRATION_INCREMENT)

        # rotate to best alignment
        turn_times = ((best_pos + 2) % 3) - 1
        await self._motor.run_angle(self._speed,
                                    self._CALIBRATION_INCREMENT * turn_times)
        print("calibrating turntable done")

    async def turn(self,
                   direction: int,
                   amount: int,
                   overturn: bool = False) -> None:
        await self._turn(direction, amount, self._speed, overturn=overturn)

    async def turn_slowly(self,
                          direction: int,
                          amount: int) -> None:
        await self._turn(direction, amount, self._slow_speed)

    async def correct_overturn(self) -> None:
        await self._motor.run_angle(self._speed, - self._overturn_state * self._OVERTURN_ANGLE, wait=True)
        self._overturn_state = self._NEUTRAL_OVERTURN_STATE

    async def _turn(self, direction: int, amount: int, speed: int, overturn: bool = False) -> None:
        await self._motor.run_angle(speed, await self._get_turn_angle(amount, direction, overturn), wait=True)
        if overturn:
            self._overturn_state = direction
        else:
            self._overturn_state = self._NEUTRAL_OVERTURN_STATE

    async def _get_turn_angle(self, amount: int, direction: int, overturn: bool) -> int:
        overturn_angle = 0
        if overturn:
            if self._overturn_state == self._NEUTRAL_OVERTURN_STATE:
                overturn_angle = self._OVERTURN_ANGLE
            elif self._overturn_state != direction:
                overturn_angle = self._OVERTURN_ANGLE * 2
        else:
            if self._overturn_state == direction:
                overturn_angle = - self._OVERTURN_ANGLE
            elif self._overturn_state == - direction:
                overturn_angle = self._OVERTURN_ANGLE
        return direction * (amount * self._ANGLE_PER_AMOUNT + overturn_angle)

    def current_angle(self) -> int:
        return self._motor.angle()

    def reset_angle(self) -> None:
        self._motor.reset_angle(0)
