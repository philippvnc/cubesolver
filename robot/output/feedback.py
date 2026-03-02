from pybricks.hubs import InventorHub
from pybricks.parameters import Color
from pybricks.tools import Matrix

from constants.facelet import Facelet


class Feedback:
    _VOLUME = 50
    _PROGRESS_PIXEL_ORDER = [
        (4, 0), (2, 2), (3, 4), (1, 1), (0, 3),
        (4, 4), (3, 1), (2, 0), (1, 4), (0, 1),
        (3, 3), (4, 2), (1, 0), (0, 4), (2, 4),
        (4, 1), (3, 0), (0, 2), (2, 1), (1, 3),
        (4, 3), (3, 2), (2, 3), (1, 2), (0, 0),
    ]
    _CUBE_PIXEL_MASK = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    _OFF_INTENSITY = 30
    _ON_INTENSITY = 80

    def __init__(self, hub: InventorHub):
        self._display = hub.display
        self._light = hub.light
        self._speaker = hub.speaker
        self._speaker.volume(self._VOLUME)
        self._active_pixels = []

    def cube_missing(self) -> None:
        self._display.icon(Matrix(self._set_pixels(self._OFF_INTENSITY)))

    def cube_present(self) -> None:
        self._display.icon(Matrix(self._set_pixels(self._ON_INTENSITY)))

    def activate_facelet(self, facelet: int) -> None:
        self._active_pixels.append(Facelet.position(facelet))
        base_pixels = self._set_pixels(self._OFF_INTENSITY)
        for x, y in self._active_pixels:
            base_pixels[x + 1][y + 1] = self._ON_INTENSITY
        self._display.icon(Matrix(base_pixels))

    def deactivate_facelets(self) -> None:
        self._active_pixels = []
        self.cube_missing()

    def show_process(self, percent: int) -> None:
        # clamp percent
        if percent < 0:
            percent = 0
        elif percent > 100:
            percent = 100

        filled_pixels = (percent * 25) // 100

        # start with faint background
        pixels = [[self._OFF_INTENSITY for _ in range(5)] for _ in range(5)]

        # fill pixels according to shuffled order
        for i in range(filled_pixels):
            r, c = self._PROGRESS_PIXEL_ORDER[i]
            pixels[r][c] = self._ON_INTENSITY

        self._display.icon(Matrix(pixels))

    async def success(self):
        await self._speaker.play_notes(["G4/8", "C5/4"], 160)

    async def solved(self):
        await self._speaker.play_notes(["C5/8", "E5/8", "G5/4"], 160)

    async def fail(self):
        await self._speaker.play_notes(["G3/8", "R/16", "G3/4"], 120)

    def show_color(self, color: Color | None) -> None:
        if color is None:
            self._light.off()
        else:
            self._light.on(color)

    def clear_display(self) -> None:
        self._display.off()

    def _set_pixels(self, intensity: int):
        return [
            [
                intensity if self._CUBE_PIXEL_MASK[r][c] else 0
                for c in range(5)
            ]
            for r in range(5)
        ]
