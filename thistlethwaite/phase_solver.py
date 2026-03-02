from algorithm.ida_star import IDAStar
from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from thistlethwaite.phase import Phase

'''
A generic phase solver
uses IDA* search
'''
class PhaseSolver:

    def __init__(self,
                 phase : Phase,
                 show_progress=lambda i: print(f"progress: {i}")):
        self.ida_star = IDAStar(phase.allowed_moves,
                                CubieMoveApplier.apply,
                                phase.solved,
                                phase.heuristic,
                                PhaseSolver._move_pruning)
        self.max_depth = phase.max_moves
        self.show_progress = show_progress

    def solve(self,
              cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> list[int]:
        return self.ida_star.search(cubie, self.max_depth, self.show_progress)

    @staticmethod
    def _move_pruning(move: int,
                      last_move: int) -> bool:
        # prune all consecutive moves on same faces
        return last_move != -1 and Move.get_face(move) == Move.get_face(last_move)
