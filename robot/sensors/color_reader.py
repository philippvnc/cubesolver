from pybricks.pupdevices import ColorSensor

from robot.output.feedback import Feedback


class ColorReader:
    __LIGHT_INTENSITY = 50

    def __init__(self, sensor: ColorSensor, feedback: Feedback):
        self.__sensor = sensor
        self.__feedback = feedback
        self.turn_off_lights()

    async def read(self) -> tuple[int, int, int]:
        color = await self.__sensor.hsv()
        self.__feedback.show_color(color)
        return color.h, color.s, color.v

    async def turn_off_lights(self):
        await self.__sensor.lights.off()
        self.__feedback.show_color(None)

    async def turn_on_lights(self):
        await self.__sensor.lights.on((self.__LIGHT_INTENSITY, self.__LIGHT_INTENSITY, self.__LIGHT_INTENSITY))
