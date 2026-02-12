import urandom
from pybricks.tools import wait

from robot.actuators.arm import Arm
from robot.actuators.turntable import Turntable, TurnAmount
from constants.axis import Axis
from constants.direction import Direction
from constants.face import Face
from solver.orientation_tracker import OrientationTracker


class CubeManipulator:

    def __init__(self,
                 turntable: Turntable,
                 left_arm: Arm,
                 right_arm: Arm,
                 orientation_tracker: OrientationTracker):
        self.__turntable = turntable
        self.__left_arm = left_arm
        self.__right_arm = right_arm
        self.__orientation_tracker = orientation_tracker

    def move_face_to_top(self,
                         face: int) -> None:
        current_orientation = self.__orientation_tracker.get_position_of_face(face)
        if current_orientation == Face.RIGHT:
            self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.COUNTERCLOCKWISE, amount=TurnAmount.QUARTER)
        elif current_orientation == Face.LEFT:
            self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.CLOCKWISE, amount=TurnAmount.QUARTER)
        elif current_orientation == Face.DOWN:
            self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.COUNTERCLOCKWISE, amount=TurnAmount.HALF)
        elif current_orientation == Face.FRONT:
            self.turn_cube(axis=Axis.VERTICAL, direction=Direction.CLOCKWISE, amount=TurnAmount.QUARTER)
            self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.CLOCKWISE, amount=TurnAmount.QUARTER)
        elif current_orientation == Face.BACK:
            self.turn_cube(axis=Axis.VERTICAL, direction=Direction.COUNTERCLOCKWISE, amount=TurnAmount.QUARTER)
            self.turn_cube(axis=Axis.HORIZONTAL, direction=Direction.CLOCKWISE, amount=TurnAmount.QUARTER)

    def move_face_to_bottom(self,
                            face: int) -> None:
        self.move_face_to_top(Face.mirror(face))

    def turn_cube(self,
                  axis: int,
                  direction: int,
                  amount: float = TurnAmount.QUARTER,
                  wait_for_turn: bool = True) -> None:
        if amount == TurnAmount.NONE:
            return
        # self.__print_move(axis, direction, int(amount))
        # can only track full moves (even amounts of quarter turns)
        if not amount == TurnAmount.EIGHTH and not amount == TurnAmount.NONE:
            self.__orientation_tracker.track_turn(axis, direction, int(amount))
        if axis == Axis.VERTICAL:
            self.release_cube()
            self.__turntable.turn(direction, amount, wait_for_turn=wait_for_turn)
        elif axis == Axis.HORIZONTAL:
            (flipping_arm, holding_arm) = self.__get_arms(direction)
            for _ in range(int(amount)):
                self.__turn_cube_horizontally(flipping_arm, holding_arm)

    def turn_face(self,
                  direction: int,
                  amount: int = TurnAmount.QUARTER) -> None:
        self.__hold_cube()
        self.__turntable.turn(-direction, amount)

    def release_cube(self, wait: bool = True) -> None:
        self.__left_arm.release(wait)
        self.__right_arm.release(wait)
        if wait:
            self.__wait_until_arms_done()

    def done(self) -> bool:
        return self.__turntable.done() and self.__arms_done()

    def __arms_done(self) -> bool:
        return self.__left_arm.done() and self.__right_arm.done()

    def __wait_until_arms_done(self) -> None:
        while not self.__arms_done():
            wait(5)

    def __hold_cube(self) -> None:
        self.__left_arm.hold()
        self.__right_arm.hold()
        self.__wait_until_arms_done()

    def __get_arms(self,
                   direction: int) -> tuple[Arm, Arm]:
        if direction == Direction.CLOCKWISE:
            return self.__left_arm, self.__right_arm
        else:
            return self.__right_arm, self.__left_arm

    def __print_move(self, axis: int, direction: int, amount: int) -> None:
        print("turning cube " + TurnAmount.name(amount) + " " + Direction.name(direction) + " around " + Axis.name(axis) + " axis")

    def turn_cube_randomly(self):
        self.turn_cube(urandom.randint(0, 1), urandom.choice([1, -1]), urandom.choice([1, 2]))

    def __turn_cube_horizontally(self,
                                 flipping_arm: Arm,
                                 holding_arm: Arm) -> None:
        holding_arm.release(wait=True)
        flipping_arm.flip()


