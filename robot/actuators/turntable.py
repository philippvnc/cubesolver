from pybricks.pupdevices import Motor

from robot.sensors.cube_detector import CubeDetector


class Turntable:
    # unfortunately this value depends on axle and gear positions
    __INITIAL_PHYSICAL_ANGLE_OFFSET = 68
    __CALIBRATION_INCREMENT = 120
    __ANGLE_PER_AMOUNT = 90
    __OVERTURN_ANGLE = 2
    __NEUTRAL_OVERTURN_STATE = 0

    def __init__(self,
                 motor: Motor,
                 detector: CubeDetector,
                 speed: int = 800,
                 slow_speed: int = 135) -> None:
        self.__motor = motor
        self.__detector = detector
        self.__speed = speed
        self.__slow_speed = slow_speed
        self.__overturn_state = self.__NEUTRAL_OVERTURN_STATE

    async def calibrate_dynamically(self):
        print("calibrating turntable ...")
        best_error = 10 ** 9
        best_pos = 0

        # 1) go to initial reference
        await self.__motor.run_target(self.__speed,
                                      self.__INITIAL_PHYSICAL_ANGLE_OFFSET)

        for pos in range(3):
            error = await self.__detector.alignment_error()

            if error == self.__detector.MINIMAL_ALIGNMENT_DISTANCE:
                return

            if error < best_error:
                best_error = error
                best_pos = pos

            # only move for the first two positions
            if pos < 2:
                await self.__motor.run_angle(self.__speed,
                                             self.__CALIBRATION_INCREMENT)

        # rotate to best alignment
        turn_times = ((best_pos + 2) % 3) - 1
        await self.__motor.run_angle(self.__speed,
                                     self.__CALIBRATION_INCREMENT * turn_times)
        print("calibrating turntable done")

    async def turn(self,
                   direction: int,
                   amount: int,
                   overturn: bool = False) -> None:
        await self.__turn(direction, amount, self.__speed, overturn=overturn)

    async def turn_slowly(self,
                          direction: int,
                          amount: int) -> None:
        await self.__turn(direction, amount, self.__slow_speed)

    async def correct_overturn(self) -> None:
        await self.__motor.run_angle(self.__speed, - self.__overturn_state * self.__OVERTURN_ANGLE , wait=True)
        self.__overturn_state = self.__NEUTRAL_OVERTURN_STATE

    async def __turn(self, direction: int, amount: int, speed: int, overturn: bool = False) -> None:
        await self.__motor.run_angle(speed, await self.__get_turn_angle(amount, direction, overturn), wait=True)
        if overturn:
            self.__overturn_state = direction
        else:
            self.__overturn_state = self.__NEUTRAL_OVERTURN_STATE

    async def __get_turn_angle(self, amount: int, direction: int, overturn: bool) -> int:
        overturn_angle = 0
        if overturn:
            if self.__overturn_state == self.__NEUTRAL_OVERTURN_STATE:
                overturn_angle = self.__OVERTURN_ANGLE
            elif self.__overturn_state != direction:
                overturn_angle = self.__OVERTURN_ANGLE * 2
        else:
            if self.__overturn_state == direction:
                overturn_angle = - self.__OVERTURN_ANGLE
            elif self.__overturn_state == - direction:
                overturn_angle = self.__OVERTURN_ANGLE
        return direction * (amount * self.__ANGLE_PER_AMOUNT + overturn_angle)

    def current_angle(self) -> int:
        return self.__motor.angle()

    def reset_angle(self) -> None:
        self.__motor.reset_angle(0)
