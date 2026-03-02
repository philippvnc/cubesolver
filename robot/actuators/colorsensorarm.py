from pybricks.parameters import Stop
from pybricks.pupdevices import Motor

from constants.scan_position import ScanPosition


class ColorSensorArm:
    _SCAN_ANGLES = {
        ScanPosition.CENTER: -121,
        ScanPosition.EDGE: -94,
        ScanPosition.CORNER: -80,
    }
    _TUCK_AWAY_ANGLE = -40

    def __init__(self,
                 motor: Motor,
                 speed: int = 1000,
                 calibration_speed: int = 400):
        self._motor = motor
        self._speed = speed
        self._calibration_speed = calibration_speed
        self._calibrate()

    def _calibrate(self) -> None:
        print("calibrating color sensor arm ...")
        self._motor.run_until_stalled(self._calibration_speed, duty_limit=40)
        self._motor.reset_angle(0)
        self._motor.run_target(self._calibration_speed, self._TUCK_AWAY_ANGLE, then=Stop.COAST)
        print("calibrating color sensor arm done")

    async def tuck_away(self) -> None:
        await self._motor.run_target(self._speed, self._TUCK_AWAY_ANGLE, wait=True, then=Stop.COAST)

    async def move_to_position(self,
                               position: int) -> None:
        await self._motor.run_target(self._speed, self._SCAN_ANGLES[position], wait=True)
