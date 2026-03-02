from micropython_compat import const
from pybricks.parameters import Stop
from pybricks.pupdevices import Motor


class Arm:
    __HOLDING_ANGLE = const(-102)
    __FLIPPING_ANGLE = const(-133)
    __RELEASING_ANGLE = const(-5)

    RELEASED = const(0)
    HOLDING = const(1)
    FLIPPED = const(2)

    def __init__(self,
                 name: str,
                 motor: Motor,
                 speed: int = const(700),
                 calibration_speed: int = const(300)):
        self.name = name
        self.__motor = motor
        self.__speed = speed
        self.__calibration_speed = calibration_speed
        self.__calibrate()
        self.position = Arm.RELEASED

    def __calibrate(self) -> None:
        print("calibrating " + self.name + " ...")
        self.__motor.run_until_stalled(self.__calibration_speed, duty_limit=40)
        self.__motor.reset_angle(0)
        self.__motor.run_target(self.__calibration_speed, self.__RELEASING_ANGLE, then=Stop.COAST)
        print("calibrating " + self.name + " done")

    async def release(self) -> None:
        if self.position == Arm.RELEASED:
            return
        await self.__motor.run_target(self.__speed, self.__RELEASING_ANGLE, wait=True, then=Stop.COAST)
        self.position = Arm.RELEASED

    async def hold(self) -> None:
        if self.position == Arm.FLIPPED or self.position == Arm.HOLDING:
            return
        await self.__motor.run_target(self.__speed, self.__HOLDING_ANGLE, wait=True, then=Stop.COAST)
        self.position = Arm.HOLDING

    async def flip(self) -> None:
        if self.position == Arm.FLIPPED:
            await self.release()
        await self.__motor.run_target(self.__speed, self.__FLIPPING_ANGLE, wait=True)
        self.position = Arm.FLIPPED
