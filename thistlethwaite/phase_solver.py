from algorithm.ida_star import IDAStar
from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier

'''
A generic phase solver for thistlethwaite.
uses IDA* search
'''
class PhaseSolver:

    def __init__(self,
                 phase):
        self.ida_star = IDAStar(phase.ALLOWED_MOVES,
                                CubieMoveApplier.apply,
                                phase.phase_solved,
                                phase.heuristic,
                                PhaseSolver.__move_pruning)
        self.max_depth = phase.MAX_DEPTH

    def solve(self,
              cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> list[int]:
        return self.ida_star.search(cubie, self.max_depth)

    @staticmethod
    def __move_pruning(move: int,
                       last_move: int) -> bool:
        # prune all consecutive moves on same faces
        return last_move != -1 and Move.get_face(move) == Move.get_face(last_move)
