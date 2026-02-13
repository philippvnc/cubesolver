from solver.solution_optimizer import SolutionOptimizer
from thistlethwaite.thistlethwaite import Thistlethwaite


class SolutionGenerator:

    @staticmethod
    def generate_solution(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> list[int]:
        return SolutionOptimizer.optimize_solution(Thistlethwaite.solve(cubie))
