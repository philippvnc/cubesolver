from pybricks.parameters import Stop
from pybricks.pupdevices import Motor


class Arm:
    __HOLDING_ANGLE = -102
    __FLIPPING_ANGLE = -133
    __RELEASING_ANGLE = -5

    __RELEASED = 0
    __HOLDING = 1
    __FLIPPED = 2

    def __init__(self,
                 name: str,
                 motor: Motor,
                 speed: int = 700,
                 calibration_speed: int = 300):
        self.name = name
        self.__motor = motor
        self.__speed = speed
        self.__calibration_speed = calibration_speed
        self.__calibrate()
        self.__position = Arm.__RELEASED

    def __calibrate(self) -> None:
        print("calibrating " + self.name + " ...")
        self.__motor.run_until_stalled(self.__calibration_speed, duty_limit=40)
        self.__motor.reset_angle(0)
        self.__motor.run_target(self.__calibration_speed, self.__RELEASING_ANGLE, then=Stop.COAST)
        print("calibrating " + self.name + " done")

    def release(self,
                wait: bool = False) -> None:
        self.__motor.run_target(self.__speed, self.__RELEASING_ANGLE, wait=wait, then=Stop.COAST)
        self.__position = Arm.__RELEASED

    def hold(self,
             wait: bool = False) -> None:
        self.__motor.run_target(self.__speed, self.__HOLDING_ANGLE, wait=wait, then=Stop.COAST)
        self.__position = Arm.__HOLDING

    def flip(self) -> None:
        if self.__position == Arm.__FLIPPED:
            self.release()
        self.__motor.run_target(self.__speed, self.__FLIPPING_ANGLE)
        self.__position = Arm.__FLIPPED

    def done(self) -> bool:
        return self.__motor.done()



