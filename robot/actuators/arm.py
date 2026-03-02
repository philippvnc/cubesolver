from micropython_compat import const
from pybricks.parameters import Stop
from pybricks.pupdevices import Motor


class Arm:
    _HOLDING_ANGLE = const(-102)
    _FLIPPING_ANGLE = const(-133)
    _RELEASING_ANGLE = const(-5)

    RELEASED = const(0)
    HOLDING = const(1)
    FLIPPED = const(2)

    def __init__(self,
                 name: str,
                 motor: Motor,
                 speed: int = const(700),
                 calibration_speed: int = const(300)):
        self.name = name
        self._motor = motor
        self._speed = speed
        self._calibration_speed = calibration_speed
        self._calibrate()
        self.position = Arm.RELEASED

    def _calibrate(self) -> None:
        print("calibrating " + self.name + " ...")
        self._motor.run_until_stalled(self._calibration_speed, duty_limit=40)
        self._motor.reset_angle(0)
        self._motor.run_target(self._calibration_speed, self._RELEASING_ANGLE, then=Stop.COAST)
        print("calibrating " + self.name + " done")

    async def release(self) -> None:
        if self.position == Arm.RELEASED:
            return
        await self._motor.run_target(self._speed, self._RELEASING_ANGLE, wait=True, then=Stop.COAST)
        self.position = Arm.RELEASED

    async def hold(self) -> None:
        if self.position == Arm.FLIPPED or self.position == Arm.HOLDING:
            return
        await self._motor.run_target(self._speed, self._HOLDING_ANGLE, wait=True, then=Stop.COAST)
        self.position = Arm.HOLDING

    async def flip(self) -> None:
        if self.position == Arm.FLIPPED:
            await self.release()
        await self._motor.run_target(self._speed, self._FLIPPING_ANGLE, wait=True)
        self.position = Arm.FLIPPED
