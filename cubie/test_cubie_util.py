import random

from cubie.cubie_move_applier import CubieMoveApplier


class TestCubieUtil:

    @staticmethod
    def solved_cubie():
        return [(corner, 0) for corner in range(8)], [(edge, 0) for edge in range(12)]

    @staticmethod
    def random_moves(allowed_moves: list[int], length: int) -> list[int]:
        random.seed(137)
        scramble = []
        last_face = -1
        for _ in range(length):
            move = random.choice(allowed_moves)
            # avoid same-face repetitions
            while last_face != -1 and move // 3 == last_face:
                move = random.choice(allowed_moves)
            scramble.append(move)
            last_face = move // 3
        return scramble

    @staticmethod
    def scrambled_cubie(allowed_moves: list[int], n_moves: int):
        cubie = TestCubieUtil.solved_cubie()
        scramble = TestCubieUtil.random_moves(allowed_moves, n_moves)
        return CubieMoveApplier.apply_many(cubie, scramble)

    @staticmethod
    def __assert_cubie(actual_cubie: tuple[int, int], expected_cubie: int, expected_orientation: int,
                       incorrect_cubie: str, incorrect_orientation: str):
        assert actual_cubie[0] == expected_cubie, incorrect_cubie
        assert actual_cubie[1] == expected_orientation, incorrect_orientation

    @staticmethod
    def assert_corner(actual_corner: tuple[int, int], expected_corner: int, expected_orientation: int):
        TestCubieUtil.__assert_cubie(actual_corner, expected_corner, expected_orientation,
                                       f"incorrect corner, expected : {expected_corner} actual: {actual_corner[0]}",
                                       f"incorrect corner orientation, expected : {expected_orientation} actual: {actual_corner[1]}")

    @staticmethod
    def assert_edge(actual_edge: tuple[int, int], expected_edge: int, expected_orientation: int):
        TestCubieUtil.__assert_cubie(actual_edge, expected_edge, expected_orientation,
                                       f"incorrect edge, expected : {expected_edge} actual: {actual_edge[0]}",
                                       f"incorrect edge orientation, expected : {expected_orientation} actual: {actual_edge[1]}")
    @staticmethod
    def assert_U_clockwise_from_solved(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        corners , edges = cubie

        # only assert changed cubies (top layer)
        TestCubieUtil.assert_corner(corners[0], 3, 0)
        TestCubieUtil.assert_corner(corners[1], 0, 0)
        TestCubieUtil.assert_corner(corners[2], 1, 0)
        TestCubieUtil.assert_corner(corners[3], 2, 0)

        TestCubieUtil.assert_edge(edges[0], 3, 0)
        TestCubieUtil.assert_edge(edges[1], 0, 0)
        TestCubieUtil.assert_edge(edges[2], 1, 0)
        TestCubieUtil.assert_edge(edges[3], 2, 0)

    @staticmethod
    def assert_U_counterclockwise_from_solved(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        corners, edges = cubie

        # only assert changed cubies (top layer)
        TestCubieUtil.assert_corner(corners[0], 1, 0)
        TestCubieUtil.assert_corner(corners[1], 2, 0)
        TestCubieUtil.assert_corner(corners[2], 3, 0)
        TestCubieUtil.assert_corner(corners[3], 0, 0)

        TestCubieUtil.assert_edge(edges[0], 1, 0)
        TestCubieUtil.assert_edge(edges[1], 2, 0)
        TestCubieUtil.assert_edge(edges[2], 3, 0)
        TestCubieUtil.assert_edge(edges[3], 0, 0)

    @staticmethod
    def assert_F_clockwise_from_solved(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        corners, edges = cubie

        # only assert changed cubies (front layer)
        TestCubieUtil.assert_corner(corners[0], 1, 1)
        TestCubieUtil.assert_corner(corners[1], 5, 2)
        TestCubieUtil.assert_corner(corners[4], 0, 2)
        TestCubieUtil.assert_corner(corners[5], 4, 1)

        TestCubieUtil.assert_edge(edges[1], 9, 1)
        TestCubieUtil.assert_edge(edges[9], 5, 1)
        TestCubieUtil.assert_edge(edges[5], 8, 1)
        TestCubieUtil.assert_edge(edges[8], 1, 1)


    @staticmethod
    def assert_F_counterclockwise_from_solved(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        corners, edges = cubie

        # only assert changed cubies (front layer)
        TestCubieUtil.assert_corner(corners[0], 4, 1)
        TestCubieUtil.assert_corner(corners[1], 0, 2)
        TestCubieUtil.assert_corner(corners[4], 5, 2)
        TestCubieUtil.assert_corner(corners[5], 1, 1)

        TestCubieUtil.assert_edge(edges[1], 8, 1)
        TestCubieUtil.assert_edge(edges[9], 1, 1)
        TestCubieUtil.assert_edge(edges[5], 9, 1)
        TestCubieUtil.assert_edge(edges[8], 5, 1)

    @staticmethod
    def assert_R_clockwise_from_solved(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        corners, edges = cubie

        # only assert changed cubies (right layer)
        TestCubieUtil.assert_corner(corners[0], 4, 2)
        TestCubieUtil.assert_corner(corners[3], 0, 1)
        TestCubieUtil.assert_corner(corners[7], 3, 2)
        TestCubieUtil.assert_corner(corners[4], 7, 1)

        TestCubieUtil.assert_edge(edges[0], 8, 0)
        TestCubieUtil.assert_edge(edges[11], 0, 0)
        TestCubieUtil.assert_edge(edges[4], 11, 0)
        TestCubieUtil.assert_edge(edges[8], 4, 0)

    @staticmethod
    def assert_R_counterclockwise_from_solved(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        corners, edges = cubie

        # only assert changed cubies (right layer)
        TestCubieUtil.assert_corner(corners[0], 3, 2)
        TestCubieUtil.assert_corner(corners[3], 7, 1)
        TestCubieUtil.assert_corner(corners[7], 4, 2)
        TestCubieUtil.assert_corner(corners[4], 0, 1)

        TestCubieUtil.assert_edge(edges[0], 11, 0)
        TestCubieUtil.assert_edge(edges[11], 4, 0)
        TestCubieUtil.assert_edge(edges[4], 8, 0)
        TestCubieUtil.assert_edge(edges[8], 0, 0)

    @staticmethod
    def assert_D_clockwise_from_solved(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        corners, edges = cubie

        # only assert changed cubies (bottom layer)
        TestCubieUtil.assert_corner(corners[4], 5, 0)
        TestCubieUtil.assert_corner(corners[5], 6, 0)
        TestCubieUtil.assert_corner(corners[6], 7, 0)
        TestCubieUtil.assert_corner(corners[7], 4, 0)

        TestCubieUtil.assert_edge(edges[4], 5, 0)
        TestCubieUtil.assert_edge(edges[5], 6, 0)
        TestCubieUtil.assert_edge(edges[6], 7, 0)
        TestCubieUtil.assert_edge(edges[7], 4, 0)

    @staticmethod
    def assert_L_clockwise_from_solved(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        corners, edges = cubie

        # only assert changed cubies (left layer)
        TestCubieUtil.assert_corner(corners[1], 2, 1)
        TestCubieUtil.assert_corner(corners[2], 6, 2)
        TestCubieUtil.assert_corner(corners[6], 5, 1)
        TestCubieUtil.assert_corner(corners[5], 1, 2)

        TestCubieUtil.assert_edge(edges[2], 10, 0)
        TestCubieUtil.assert_edge(edges[10], 6, 0)
        TestCubieUtil.assert_edge(edges[6], 9, 0)
        TestCubieUtil.assert_edge(edges[9], 2, 0)

    @staticmethod
    def assert_B_clockwise_from_solved(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        corners, edges = cubie

        # only assert changed cubies (back layer)
        TestCubieUtil.assert_corner(corners[2], 3, 1)
        TestCubieUtil.assert_corner(corners[3], 7, 2)
        TestCubieUtil.assert_corner(corners[7], 6, 1)
        TestCubieUtil.assert_corner(corners[6], 2, 2)

        TestCubieUtil.assert_edge(edges[3], 11, 1)
        TestCubieUtil.assert_edge(edges[11], 7, 1)
        TestCubieUtil.assert_edge(edges[7], 10, 1)
        TestCubieUtil.assert_edge(edges[10], 3, 1)
