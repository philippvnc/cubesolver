class Move:
    U = 0
    U2 = 1
    U_ = 2
    R = 3
    R2 = 4
    R_ = 5
    F = 6
    F2 = 7
    F_ = 8
    D = 9
    D2 = 10
    D_ = 11
    L = 12
    L2 = 13
    L_ = 14
    B = 15
    B2 = 16
    B_ = 17

    ALL_MOVES = [U, U2, U_, R, R2, R_, F, F2, F_, D, D2, D_, L, L2, L_, B, B2, B_]

    @staticmethod
    def print_moves(moves: list[int]) -> None:
        for move in moves:
            print(Move.name(move))

    @staticmethod
    def name(move: int) -> str:
        if move == Move.U:
            return "U"
        elif move == Move.U2:
            return "U2"
        elif move == Move.U_:
            return "U'"
        elif move == Move.R:
            return "R"
        elif move == Move.R2:
            return "R2"
        elif move == Move.R_:
            return "R'"
        elif move == Move.F:
            return "F"
        elif move == Move.F2:
            return "F2"
        elif move == Move.F_:
            return "F'"
        elif move == Move.D:
            return "D"
        elif move == Move.D2:
            return "D2"
        elif move == Move.D_:
            return "D'"
        elif move == Move.L:
            return "L"
        elif move == Move.L2:
            return "L2"
        elif move == Move.L_:
            return "L'"
        elif move == Move.B:
            return "B"
        elif move == Move.B2:
            return "B2"
        elif move == Move.B_:
            return "B'"
        else:
            return "INVALID"

    @staticmethod
    def get_face(move:int) -> int:
        return move // 3

    @staticmethod
    def are_moves_same_face(move_a: int, move_b: int) -> bool:
        return Move.get_face(move_a) == Move.get_face(move_b)

    @staticmethod
    def merge_same_face_moves(move_a: int, move_b: int) -> list[int]:
        face = Move.get_face(move_a)
        combined_move_offset = (move_a % 3 + move_b % 3) % 4
        if combined_move_offset == 0:
            return [face * 3 + 1]
        elif combined_move_offset == 1:
            return [face * 3 + 2]
        elif combined_move_offset == 2:
            return []
        else:
            return [face * 3]
