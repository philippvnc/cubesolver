

class Phase:

    def __init__(self,
                 name: str,
                 allowed_moves: list[int],
                 max_moves: int,
                 heuristic):
        self.name = name
        self.allowed_moves = allowed_moves
        self.max_moves = max_moves
        self.heuristic = heuristic

    def solved(self, cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]):
        pass