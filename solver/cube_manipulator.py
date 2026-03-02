from pybricks.tools import multitask

from constants.axis import Axis
from constants.direction import Direction
from constants.face import Face
from constants.turn_amount import TurnAmount
from robot.actuators.arm import Arm
from robot.actuators.turntable import Turntable
from solver.orientation_tracker import OrientationTracker


class CubeManipulator:

    def __init__(self,
                 turntable: Turntable,
                 left_arm: Arm,
                 right_arm: Arm,
                 orientation_tracker: OrientationTracker):
        self.turntable = turntable
        self._left_arm = left_arm
        self._right_arm = right_arm
        self._arms = [left_arm, right_arm]
        self._orientation_tracker = orientation_tracker

    async def move_face_to_top(self,
                               face: int) -> None:
        current_orientation = self._orientation_tracker.get_position_of_face(face)
        if current_orientation == Face.RIGHT:
            await self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.COUNTERCLOCKWISE, amount=TurnAmount.QUARTER)
        elif current_orientation == Face.LEFT:
            await self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.CLOCKWISE, amount=TurnAmount.QUARTER)
        elif current_orientation == Face.DOWN:
            await self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.COUNTERCLOCKWISE, amount=TurnAmount.HALF)
        elif current_orientation == Face.FRONT:
            await self.turn_cube(axis=Axis.VERTICAL, direction=Direction.CLOCKWISE, amount=TurnAmount.QUARTER)
            await self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.CLOCKWISE, amount=TurnAmount.QUARTER)
        elif current_orientation == Face.BACK:
            await self.turn_cube(axis=Axis.VERTICAL, direction=Direction.COUNTERCLOCKWISE, amount=TurnAmount.QUARTER)
            await self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.CLOCKWISE, amount=TurnAmount.QUARTER)

    async def move_face_to_bottom(self,
                                  face: int) -> None:
        await self.move_face_to_top(Face.mirror(face))

    async def turn_cube(self,
                        axis: int,
                        direction: int,
                        amount: int = TurnAmount.QUARTER) -> None:
        if amount == TurnAmount.NONE:
            return
        self._orientation_tracker.track_turn(axis, direction, amount)
        if axis == Axis.VERTICAL:
            await self.release_cube()
            await self.turntable.turn(direction, amount)
        elif axis == Axis.HORIZONTAL:
            (flipping_arm, inactive_arm) = self._get_arms(direction)
            for _ in range(amount):
                await self._turn_cube_horizontally(flipping_arm, inactive_arm)

    async def turn_face(self,
                        direction: int,
                        amount: int = TurnAmount.QUARTER) -> None:
        await self.hold_cube()
        flipped_arms = self._get_arms_in_position(Arm.FLIPPED)
        if len(flipped_arms) == 1:
            await multitask(flipped_arms[0].release(), self.turntable.turn(-direction, amount, overturn=True))
        else:
            await self.turntable.turn(-direction, amount, overturn=True)

    async def release_cube(self) -> None:
        await multitask(self._left_arm.release(), self._right_arm.release(), self.turntable.correct_overturn())

    async def hold_cube(self) -> None:
        holder_arms = self._get_arms_in_position(Arm.RELEASED)
        if len(holder_arms) == 1:
            await holder_arms[0].hold()
        else:
            await multitask(self._left_arm.hold(), self._right_arm.hold())

    def _get_arms_in_position(self, position: int) -> list[Arm]:
        return [arm for arm in self._arms if arm.position == position]

    def _get_arms(self,
                  direction: int) -> tuple[Arm, Arm]:
        if direction == Direction.CLOCKWISE:
            return self._left_arm, self._right_arm
        else:
            return self._right_arm, self._left_arm

    async def _turn_cube_horizontally(self,
                                      flipping_arm: Arm,
                                      inactive_arm: Arm) -> None:
        if flipping_arm.position == Arm.FLIPPED:
            await multitask(inactive_arm.hold(), flipping_arm.release())
        await multitask(inactive_arm.release(), flipping_arm.flip())
