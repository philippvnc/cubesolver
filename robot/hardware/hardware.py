from pybricks.hubs import InventorHub
from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor


class Hardware:

    def __init__(self):
        self.turntable_motor = Motor(Port.C, Direction.CLOCKWISE, [20, 60])
        self.color_arm_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [8, 24])
        self.left_arm_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE, [12, 20])
        self.right_arm_motor = Motor(Port.F, Direction.CLOCKWISE, [12, 20])
        self.color_sensor = ColorSensor(Port.B)
        self.distance_sensor = UltrasonicSensor(Port.A)
        self.hub = InventorHub()
