from solver.solution_optimizer import SolutionOptimizer
from thistlethwaite.thistlethwaite import Thistlethwaite


class SolutionGenerator:

    @staticmethod
    def generate_solution(cubie: tuple[list[tuple[int, int]], list[tuple[int, int]]],
                          show_progress) -> list[int]:
        thistlethwaite = Thistlethwaite(show_progress)
        return SolutionOptimizer.optimize_solution(thistlethwaite.solve(cubie))
