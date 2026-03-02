from micropython_compat import const
from pybricks.hubs import InventorHub
from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor


class Hardware:
    __TINY_GEAR = const(8)
    __SMALL_GEAR = const(12)
    __MIDDLE_GEAR = const(20)
    __LARGE_GEAR = const(24)
    __TURNTABLE_BASE_GEAR = const(60)

    def __init__(self):
        self.turntable_motor = Motor(Port.A, Direction.CLOCKWISE, [Hardware.__MIDDLE_GEAR, Hardware.__TURNTABLE_BASE_GEAR])
        self.color_arm_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [Hardware.__TINY_GEAR, Hardware.__LARGE_GEAR])
        self.left_arm_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE, [Hardware.__SMALL_GEAR, Hardware.__MIDDLE_GEAR])
        self.right_arm_motor = Motor(Port.F, Direction.CLOCKWISE, [Hardware.__SMALL_GEAR, Hardware.__MIDDLE_GEAR])
        self.color_sensor = ColorSensor(Port.C)
        self.distance_sensor = UltrasonicSensor(Port.B)
        self.hub = InventorHub()
