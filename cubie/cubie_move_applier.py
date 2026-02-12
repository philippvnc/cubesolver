from constants.face import Face


class CubieMoveApplier:
    # define the changes for the 4 affected corners and edges per face on a clockwise rotation
    __CLOCKWISE_MOVES_PER_FACE = [
        ([(0, 3, 0), (1, 0, 0), (2, 1, 0), (3, 2, 0)], [(0, 3, 0), (1, 0, 0), (2, 1, 0), (3, 2, 0)]),
        ([(0, 4, 2), (3, 0, 1), (7, 3, 2), (4, 7, 1)], [(0, 8, 0), (11, 0, 0), (4, 11, 0), (8, 4, 0)]),
        ([(0, 1, 1), (4, 0, 2), (5, 4, 1), (1, 5, 2)], [(1, 9, 1), (8, 1, 1), (5, 8, 1), (9, 5, 1)]),
        ([(4, 5, 0), (5, 6, 0), (6, 7, 0), (7, 4, 0)], [(4, 5, 0), (5, 6, 0), (6, 7, 0), (7, 4, 0)]),
        ([(1, 2, 1), (2, 6, 2), (6, 5, 1), (5, 1, 2)], [(2, 10, 0), (10, 6, 0), (6, 9, 0), (9, 2, 0)]),
        ([(2, 3, 1), (3, 7, 2), (7, 6, 1), (6, 2, 2)], [(3, 11, 1), (11, 7, 1), (7, 10, 1), (10, 3, 1)])]

    # define how each move translates to the face and the amount of clockwise turns
    __CLOCKWISE_FACE_TURNS_PER_MOVES = [(Face.UP, 1),
                                        (Face.UP, 2),
                                        (Face.UP, 3),
                                        (Face.RIGHT, 1),
                                        (Face.RIGHT, 2),
                                        (Face.RIGHT, 3),
                                        (Face.FRONT, 1),
                                        (Face.FRONT, 2),
                                        (Face.FRONT, 3),
                                        (Face.DOWN, 1),
                                        (Face.DOWN, 2),
                                        (Face.DOWN, 3),
                                        (Face.LEFT, 1),
                                        (Face.LEFT, 2),
                                        (Face.LEFT, 3),
                                        (Face.BACK, 1),
                                        (Face.BACK, 2),
                                        (Face.BACK, 3)]

    __N_CORNER_ORIENTATIONS = 3
    __N_EDGE_ORIENTATIONS = 2

    @staticmethod
    def apply_many(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]],
              moves: list[int]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        for move in moves:
            cubie = CubieMoveApplier.apply(cubie, move)
        return cubie

    @staticmethod
    def apply(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]],
              move: int) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        face, clockwise_turns = CubieMoveApplier.__CLOCKWISE_FACE_TURNS_PER_MOVES[move]
        current_cubie = cubie

        for i in range(clockwise_turns):
            current_cubie = CubieMoveApplier.__apply_clockwise(current_cubie, face)

        return current_cubie

    @staticmethod
    def __apply_clockwise(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]],
                          face: int) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        corners, edges = cubie
        corner_moves, edge_moves = CubieMoveApplier.__CLOCKWISE_MOVES_PER_FACE[face]

        new_corners = CubieMoveApplier.__apply_cubie_moves(
            corners,
            corner_moves,
            CubieMoveApplier.__N_CORNER_ORIENTATIONS
        )

        new_edges = CubieMoveApplier.__apply_cubie_moves(
            edges,
            edge_moves,
            CubieMoveApplier.__N_EDGE_ORIENTATIONS
        )

        return new_corners, new_edges

    @staticmethod
    def __apply_cubie_moves(cubies: list[tuple[int, int]], moves: list[tuple[int, int, int]], orientation_mod: int):
        new_cubies = cubies[:]  # shallow copy

        for new_pos, old_pos, ori_offset in moves:
            cubie_id, ori = cubies[old_pos]
            new_cubies[new_pos] = (
                cubie_id,
                (ori + ori_offset) % orientation_mod
            )

        return new_cubies
