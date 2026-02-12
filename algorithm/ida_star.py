class IDAStar:
    def __init__(self, moves, get_next_node, goal_reached, heuristic, move_pruning):
        self.moves = moves
        self.get_next_node = get_next_node
        self.goal_reached = goal_reached
        self.heuristic = heuristic
        self.move_pruning = move_pruning
        self.visited = 0

    def __search(self, node, g, bound, last_move, path):
        self.visited += 1

        h = self.heuristic(node)
        f = g + h

        if f > bound:
            return f

        if self.goal_reached(node):
            return True

        min_excess = float("inf")

        for move in self.moves:
            if self.move_pruning(move, last_move):
                continue

            next_cubie = self.get_next_node(node, move)

            result = self.__search(
                next_cubie,
                g + 1,
                bound,
                move,
                path
            )

            if result is True:
                path.append(move)
                return True

            if result < min_excess:
                min_excess = result

        return min_excess

    def search(self, node, max_depth=20):
        print("starting search with IDA*")
        self.visited = 0
        bound = self.heuristic(node)

        while bound <= max_depth:
            print(f"bound: {bound}")
            path = []
            result = self.__search(node, 0, bound, -1, path)

            if result is True:
                return list(reversed(path))

            bound = result

        return None
