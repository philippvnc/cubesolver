from micropython_compat import const
from pybricks.hubs import InventorHub
from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor


class Hardware:
    _TINY_GEAR = const(8)
    _SMALL_GEAR = const(12)
    _MIDDLE_GEAR = const(20)
    _LARGE_GEAR = const(24)
    _TURNTABLE_BASE_GEAR = const(60)

    def __init__(self):
        self.turntable_motor = Motor(Port.A, Direction.CLOCKWISE, [Hardware._MIDDLE_GEAR, Hardware._TURNTABLE_BASE_GEAR])
        self.color_arm_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [Hardware._TINY_GEAR, Hardware._LARGE_GEAR])
        self.left_arm_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE, [Hardware._SMALL_GEAR, Hardware._MIDDLE_GEAR])
        self.right_arm_motor = Motor(Port.F, Direction.CLOCKWISE, [Hardware._SMALL_GEAR, Hardware._MIDDLE_GEAR])
        self.color_sensor = ColorSensor(Port.C)
        self.distance_sensor = UltrasonicSensor(Port.B)
        self.hub = InventorHub()
