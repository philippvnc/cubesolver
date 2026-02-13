from constants.cubie import Cubie
from constants.move import Move


class CubieMoveApplier:
    # define the changes for the 4 affected corners per face on a clockwise quarter rotation
    # format: (old corner, new corner, orientation diff)
    __CORNER_CLOCKWISE_QUARTER_CHANGES_PER_FACE = [
        [(Cubie.CORNER_URF, Cubie.CORNER_UBR, 0), (Cubie.CORNER_URL, Cubie.CORNER_URF, 0),
         (Cubie.CORNER_ULB, Cubie.CORNER_URL, 0), (Cubie.CORNER_UBR, Cubie.CORNER_ULB, 0)],
        [(Cubie.CORNER_URF, Cubie.CORNER_DFR, 2), (Cubie.CORNER_UBR, Cubie.CORNER_URF, 1),
         (Cubie.CORNER_DRB, Cubie.CORNER_UBR, 2), (Cubie.CORNER_DFR, Cubie.CORNER_DRB, 1)],
        [(Cubie.CORNER_URF, Cubie.CORNER_URL, 1), (Cubie.CORNER_DFR, Cubie.CORNER_URF, 2),
         (Cubie.CORNER_DLF, Cubie.CORNER_DFR, 1), (Cubie.CORNER_URL, Cubie.CORNER_DLF, 2)],
        [(Cubie.CORNER_DFR, Cubie.CORNER_DLF, 0), (Cubie.CORNER_DLF, Cubie.CORNER_DBL, 0),
         (Cubie.CORNER_DBL, Cubie.CORNER_DRB, 0), (Cubie.CORNER_DRB, Cubie.CORNER_DFR, 0)],
        [(Cubie.CORNER_URL, Cubie.CORNER_ULB, 1), (Cubie.CORNER_ULB, Cubie.CORNER_DBL, 2),
         (Cubie.CORNER_DBL, Cubie.CORNER_DLF, 1), (Cubie.CORNER_DLF, Cubie.CORNER_URL, 2)],
        [(Cubie.CORNER_ULB, Cubie.CORNER_UBR, 1), (Cubie.CORNER_UBR, Cubie.CORNER_DRB, 2),
         (Cubie.CORNER_DRB, Cubie.CORNER_DBL, 1), (Cubie.CORNER_DBL, Cubie.CORNER_ULB, 2)]]

    # define the changes for the 4 affected edges per face on a clockwise quarter rotation
    # format: (old edge, new edge, orientation diff)
    __EDGE_CLOCKWISE_QUARTER_CHANGES_PER_FACE = [
        [(Cubie.EDGE_UR, Cubie.EDGE_UB, 0), (Cubie.EDGE_UF, Cubie.EDGE_UR, 0), (Cubie.EDGE_UL, Cubie.EDGE_UF, 0),
         (Cubie.EDGE_UB, Cubie.EDGE_UL, 0)],
        [(Cubie.EDGE_UR, Cubie.EDGE_FR, 0), (Cubie.EDGE_BR, Cubie.EDGE_UR, 0), (Cubie.EDGE_DR, Cubie.EDGE_BR, 0),
         (Cubie.EDGE_FR, Cubie.EDGE_DR, 0)],
        [(Cubie.EDGE_UF, Cubie.EDGE_FL, 1), (Cubie.EDGE_FR, Cubie.EDGE_UF, 1), (Cubie.EDGE_DF, Cubie.EDGE_FR, 1),
         (Cubie.EDGE_FL, Cubie.EDGE_DF, 1)],
        [(Cubie.EDGE_DR, Cubie.EDGE_DF, 0), (Cubie.EDGE_DF, Cubie.EDGE_DL, 0), (Cubie.EDGE_DL, Cubie.EDGE_DB, 0),
         (Cubie.EDGE_DB, Cubie.EDGE_DR, 0)],
        [(Cubie.EDGE_UL, Cubie.EDGE_BL, 0), (Cubie.EDGE_BL, Cubie.EDGE_DL, 0), (Cubie.EDGE_DL, Cubie.EDGE_FL, 0),
         (Cubie.EDGE_FL, Cubie.EDGE_UL, 0)],
        [(Cubie.EDGE_UB, Cubie.EDGE_BR, 1), (Cubie.EDGE_BR, Cubie.EDGE_DB, 1), (Cubie.EDGE_DB, Cubie.EDGE_BL, 1),
         (Cubie.EDGE_BL, Cubie.EDGE_UB, 1)]]

    __MOVES_EXPRESSED_IN_CLOCKWISE_QUARTER_TURNS = [[Move.U] * 1,
                                                    [Move.U] * 2,
                                                    [Move.U] * 3,
                                                    [Move.R] * 1,
                                                    [Move.R] * 2,
                                                    [Move.R] * 3,
                                                    [Move.F] * 1,
                                                    [Move.F] * 2,
                                                    [Move.F] * 3,
                                                    [Move.D] * 1,
                                                    [Move.D] * 2,
                                                    [Move.D] * 3,
                                                    [Move.L] * 1,
                                                    [Move.L] * 2,
                                                    [Move.L] * 3,
                                                    [Move.B] * 1,
                                                    [Move.B] * 2,
                                                    [Move.B] * 3]

    @staticmethod
    def apply_many(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]],
                   moves: list[int]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        for move in moves:
            cubie = CubieMoveApplier.apply(cubie, move)
        return cubie

    @staticmethod
    def apply(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]],
              move: int) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        for quarter_move in CubieMoveApplier.__MOVES_EXPRESSED_IN_CLOCKWISE_QUARTER_TURNS[move]:
            cubie = CubieMoveApplier.__apply_clockwise(cubie, Move.get_face(quarter_move))
        return cubie

    @staticmethod
    def __apply_clockwise(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]],
                          face: int) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        corners, edges = cubie
        new_corners = CubieMoveApplier.__apply_cubie_changes(
            corners,
            CubieMoveApplier.__CORNER_CLOCKWISE_QUARTER_CHANGES_PER_FACE[face],
            Cubie.N_CORNER_ORIENTATIONS
        )
        new_edges = CubieMoveApplier.__apply_cubie_changes(
            edges,
            CubieMoveApplier.__EDGE_CLOCKWISE_QUARTER_CHANGES_PER_FACE[face],
            Cubie.N_EDGE_ORIENTATIONS
        )
        return new_corners, new_edges

    @staticmethod
    def __apply_cubie_changes(cubie_pieces: list[tuple[int, int]], changes: list[tuple[int, int, int]], orientation_mod: int):
        new_cubie_pieces = cubie_pieces[:]  # shallow copy

        for new_pos, old_pos, orientation_offset in changes:
            cubie_id, ori = cubie_pieces[old_pos]
            new_cubie_pieces[new_pos] = (
                cubie_id,
                (ori + orientation_offset) % orientation_mod
            )

        return new_cubie_pieces
