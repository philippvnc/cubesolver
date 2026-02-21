from constants.direction import Direction
from constants.face import Face
from constants.move import Move
from constants.turn_amount import TurnAmount
from robot.output.feedback import Feedback
from solver.cube_manipulator import CubeManipulator


class SolutionExecutor:
    def __init__(self, manipulator: CubeManipulator, feedback: Feedback):
        self.manipulator = manipulator
        self.feedback = feedback

    def execute_solution(self, moves: list[int]) -> None:
        n_moves = len(moves)
        self.feedback.show_process(0)
        for i, move in enumerate(moves, 1):
            command = SolutionExecutor.__translate_to_command(move)
            if command is None:
                continue
            face, direction, amount = command
            self.manipulator.move_face_to_bottom(face)
            self.manipulator.turn_face(direction, amount)
            self.feedback.show_process((i * 100) // n_moves)

        self.manipulator.release_cube(False)
        self.feedback.solved()


    @staticmethod
    def __translate_to_command(move: int) -> tuple[int, int, int] | None:
        if move == Move.U:
            return Face.UP, Direction.CLOCKWISE, TurnAmount.QUARTER
        elif move == Move.U2:
            return Face.UP, Direction.CLOCKWISE, TurnAmount.HALF
        elif move == Move.U_:
            return Face.UP, Direction.COUNTERCLOCKWISE, TurnAmount.QUARTER
        elif move == Move.R:
            return Face.RIGHT, Direction.CLOCKWISE, TurnAmount.QUARTER
        elif move == Move.R2:
            return Face.RIGHT, Direction.CLOCKWISE, TurnAmount.HALF
        elif move == Move.R_:
            return Face.RIGHT, Direction.COUNTERCLOCKWISE, TurnAmount.QUARTER
        elif move == Move.F:
            return Face.FRONT, Direction.CLOCKWISE, TurnAmount.QUARTER
        elif move == Move.F2:
            return Face.FRONT, Direction.CLOCKWISE, TurnAmount.HALF
        elif move == Move.F_:
            return Face.FRONT, Direction.COUNTERCLOCKWISE, TurnAmount.QUARTER
        elif move == Move.D:
            return Face.DOWN, Direction.CLOCKWISE, TurnAmount.QUARTER
        elif move == Move.D2:
            return Face.DOWN, Direction.CLOCKWISE, TurnAmount.HALF
        elif move == Move.D_:
            return Face.DOWN, Direction.COUNTERCLOCKWISE, TurnAmount.QUARTER
        elif move == Move.L:
            return Face.LEFT, Direction.CLOCKWISE, TurnAmount.QUARTER
        elif move == Move.L2:
            return Face.LEFT, Direction.CLOCKWISE, TurnAmount.HALF
        elif move == Move.L_:
            return Face.LEFT, Direction.COUNTERCLOCKWISE, TurnAmount.QUARTER
        elif move == Move.B:
            return Face.BACK, Direction.CLOCKWISE, TurnAmount.QUARTER
        elif move == Move.B2:
            return Face.BACK, Direction.CLOCKWISE, TurnAmount.HALF
        elif move == Move.B_:
            return Face.BACK, Direction.COUNTERCLOCKWISE, TurnAmount.QUARTER
        else:
            return None