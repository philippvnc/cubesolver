import urandom
from pybricks.tools import StopWatch

from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from thistlethwaite.thistlethwaite import Thistlethwaite


def main():
    n_scrambles = 10
    min_scramble_moves = 1000
    thistlethwaite = Thistlethwaite()
    watch = StopWatch()
    _ = map(thistlethwaite.solve, [scrambled_cubie(Move.ALL_MOVES, n_moves) for n_moves in range(min_scramble_moves,min_scramble_moves+n_scrambles)])
    total_time = watch.time()
    print(f"total time {total_time} ms")
    print(f"average time {total_time//n_scrambles} ms")

def solved_cubie():
    return [(corner, 0) for corner in range(8)], [(edge, 0) for edge in range(12)]

def scrambled_cubie(allowed_moves: list[int], n_moves: int):
    cubie = solved_cubie()
    scramble_moves = random_moves(allowed_moves, n_moves)
    return CubieMoveApplier.apply_many(cubie, scramble_moves)

def random_moves(allowed_moves: list[int], length: int) -> list[int]:
    urandom.seed(137)
    scramble = []
    last_face = -1
    for _ in range(length):
        move = urandom.choice(allowed_moves)
        # avoid same-face repetitions
        while last_face != -1 and move // 3 == last_face:
            move = urandom.choice(allowed_moves)
        scramble.append(move)
        last_face = move // 3
    return scramble

main()
