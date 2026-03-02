from pybricks.parameters import Stop
from pybricks.pupdevices import Motor

from constants.scan_position import ScanPosition


class ColorSensorArm:
    __SCAN_ANGLES = {
        ScanPosition.CENTER: -121,
        ScanPosition.EDGE: -94,
        ScanPosition.CORNER: -80,
    }
    __TUCK_AWAY_ANGLE = -40

    def __init__(self,
                 motor: Motor,
                 speed: int = 1000,
                 calibration_speed: int = 400):
        self.__motor = motor
        self.__speed = speed
        self.__calibration_speed = calibration_speed
        self.__calibrate()

    def __calibrate(self) -> None:
        print("calibrating color sensor arm ...")
        self.__motor.run_until_stalled(self.__calibration_speed, duty_limit=40)
        self.__motor.reset_angle(0)
        self.__motor.run_target(self.__calibration_speed, self.__TUCK_AWAY_ANGLE, then=Stop.COAST)
        print("calibrating color sensor arm done")

    async def tuck_away(self) -> None:
        await self.__motor.run_target(self.__speed, self.__TUCK_AWAY_ANGLE, wait=True, then=Stop.COAST)

    async def move_to_position(self,
                               position: int) -> None:
        await self.__motor.run_target(self.__speed, self.__SCAN_ANGLES[position], wait=True)
