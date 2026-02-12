from collections import deque

from cubie.cubie_move_applier import CubieMoveApplier


class PruningTableCreator:

    @staticmethod
    def create(n_states:int, encode_cubie, allowed_moves: list[int]) -> list[int]:
        pruning = [-1] * n_states
        visited_indexes = []
        visited_corners = []

        # solved cubie
        solved_cubie = (
            [(i, 0) for i in range(8)],
            [(i, 0) for i in range(12)]
        )

        start = encode_cubie(solved_cubie)
        pruning[start] = 0
        visited_indexes.append(start)
        visited_corners.append(solved_cubie[0])

        q = deque([solved_cubie])

        while q:
            cubie = q.popleft()
            depth = pruning[encode_cubie(cubie)]
            for move in allowed_moves:

                next_cubie = CubieMoveApplier.apply(cubie, move)
                state = encode_cubie(next_cubie)
                if pruning[state] == -1:
                    visited_corners.append(next_cubie[0])
                    visited_indexes.append(state)
                    pruning[state] = depth + 1
                    q.append(next_cubie)


        print(f"visited_corners len : {len(visited_corners)}")
        print(f"visited_corners : {visited_corners}")
        print(f"visited_indexes len sorted : {len(sorted(visited_indexes))}")
        print(f"visited_indexes sorted : {sorted(visited_indexes)}")
        print(f"visited_indexes len : {len(visited_indexes)}")
        return pruning