from constants.move import Move


class SolutionOptimizer:

    @staticmethod
    def optimize_solution(solution):
        for i in range(len(solution) - 1):
            if Move.are_moves_same_face(solution[i], solution[i + 1]):
                return SolutionOptimizer.optimize_solution(solution[:i] + Move.merge_same_face_moves(solution[i], solution[i + 1]) + solution[i + 2:])
        print("optimized solution:")
        Move.print_moves(solution)
        return solution

