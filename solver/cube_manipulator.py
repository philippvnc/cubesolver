import urandom
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
        self.__left_arm = left_arm
        self.__right_arm = right_arm
        self.__arms = [left_arm, right_arm]
        self.__orientation_tracker = orientation_tracker

    async def move_face_to_top(self,
                               face: int) -> None:
        current_orientation = self.__orientation_tracker.get_position_of_face(face)
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
        self.__orientation_tracker.track_turn(axis, direction, amount)
        if axis == Axis.VERTICAL:
            await self.release_cube()
            await self.turntable.turn(direction, amount)
        elif axis == Axis.HORIZONTAL:
            (flipping_arm, inactive_arm) = self.__get_arms(direction)
            for _ in range(amount):
                await self.__turn_cube_horizontally(flipping_arm, inactive_arm)

    async def turn_face(self,
                        direction: int,
                        amount: int = TurnAmount.QUARTER) -> None:
        await self.hold_cube()
        flipped_arms = self.__get_arms_in_position(Arm.FLIPPED)
        if len(flipped_arms) == 1:
            await multitask(flipped_arms[0].release(), self.turntable.turn(-direction, amount, overturn=True))
        else:
            await self.turntable.turn(-direction, amount, overturn=True)

    async def release_cube(self) -> None:
        await multitask(self.__left_arm.release(), self.__right_arm.release(), self.turntable.correct_overturn())

    async def hold_cube(self) -> None:
        holder_arms = self.__get_arms_in_position(Arm.RELEASED)
        if len(holder_arms) == 1:
            await holder_arms[0].hold()
        else:
            await multitask(self.__left_arm.hold(), self.__right_arm.hold())

    def __get_arms_in_position(self, position: int) -> list[Arm]:
        return [arm for arm in self.__arms if arm.position == position]

    def __get_arms(self,
                   direction: int) -> tuple[Arm, Arm]:
        if direction == Direction.CLOCKWISE:
            return self.__left_arm, self.__right_arm
        else:
            return self.__right_arm, self.__left_arm

    def __print_move(self, axis: int, direction: int, amount: int) -> None:
        print("turning cube " + TurnAmount.name(amount) + " " + Direction.name(direction) + " around " + Axis.name(
            axis) + " axis")

    async def turn_cube_randomly(self):
        await self.turn_cube(urandom.randint(0, 1), urandom.choice([1, -1]), urandom.choice([1, 2]))

    async def __turn_cube_horizontally(self,
                                       flipping_arm: Arm,
                                       inactive_arm: Arm) -> None:
        if flipping_arm.position == Arm.FLIPPED:
            await multitask(inactive_arm.hold(), flipping_arm.release())
        await multitask(inactive_arm.release(), flipping_arm.flip())
