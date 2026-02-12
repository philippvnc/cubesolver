import unittest

from constants.move import Move
from solver.solution_optimizer import SolutionOptimizer


class TestSolutionOptimizer(unittest.TestCase):
    def test_optimize_solution_with_canceling_moves(self):
        solution = [Move.U, Move.U_]
        optimized_solution = SolutionOptimizer.optimize_solution(solution)
        self.assertEqual(optimized_solution, [])

    def test_optimize_solution_with_identical_half_moves(self):
        solution = [Move.R2, Move.R2]
        optimized_solution = SolutionOptimizer.optimize_solution(solution)
        self.assertEqual(optimized_solution, [])

    def test_optimize_solution_with_adding_quarter_moves(self):
        solution = [Move.R, Move.R]
        optimized_solution = SolutionOptimizer.optimize_solution(solution)
        self.assertEqual(optimized_solution, [Move.R2])

    def test_optimize_solution_with_adding_quarter_counterclockwise_moves(self):
        solution = [Move.R_, Move.R_]
        optimized_solution = SolutionOptimizer.optimize_solution(solution)
        self.assertEqual(optimized_solution, [Move.R2])

    def test_optimize_solution_with_same_face_moves(self):
        solution = [Move.U2, Move.U]
        optimized_solution = SolutionOptimizer.optimize_solution(solution)
        self.assertEqual(optimized_solution, [Move.U_])

    def test_optimize_solution_works_recursively(self):
        solution = [Move.U2, Move.D, Move.D_, Move.U]
        optimized_solution = SolutionOptimizer.optimize_solution(solution)
        self.assertEqual(optimized_solution, [Move.U_])


if __name__ == '__main__':
    unittest.main()
