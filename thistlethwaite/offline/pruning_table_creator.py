from collections import deque

from constants.cubie import Cubie
from cubie.cubie_move_applier import CubieMoveApplier


class PruningTableCreator:

    @staticmethod
    def create(n_states: int, encode_cubie, allowed_moves: list[int]) -> list[int]:
        pruning = [-1] * n_states

        solved_cubie = Cubie.SOLVED

        start = encode_cubie(solved_cubie)
        pruning[start] = 0

        q = deque([solved_cubie])

        while q:
            cubie = q.popleft()
            depth = pruning[encode_cubie(cubie)]
            for move in allowed_moves:
                next_cubie = CubieMoveApplier.apply(cubie, move)
                state = encode_cubie(next_cubie)
                if pruning[state] == -1:
                    pruning[state] = depth + 1
                    q.append(next_cubie)

        pruning = [0 if x == -1 else x for x in pruning]
        return pruning
