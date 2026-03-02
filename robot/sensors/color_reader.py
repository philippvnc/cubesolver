from micropython_compat import const
from pybricks.pupdevices import ColorSensor

from robot.output.feedback import Feedback


class ColorReader:
    _LIGHT_INTENSITY = const(50)

    def __init__(self, sensor: ColorSensor, feedback: Feedback):
        self._sensor = sensor
        self._feedback = feedback
        self.turn_off_lights()

    async def read(self) -> tuple[int, int, int]:
        color = await self._sensor.hsv()
        self._feedback.show_color(color)
        return color.h, color.s, color.v

    async def turn_off_lights(self):
        await self._sensor.lights.off()
        self._feedback.show_color(None)

    async def turn_on_lights(self):
        await self._sensor.lights.on((self._LIGHT_INTENSITY, self._LIGHT_INTENSITY, self._LIGHT_INTENSITY))
