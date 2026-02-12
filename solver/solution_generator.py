from solver.solution_optimizer import SolutionOptimizer
from thistlethwaite.thistlethwaite import Thistlethwaite


class SolutionGenerator:
    def __init__(self):
        pass

    def generate_solution(self, cubie):
        return SolutionOptimizer.optimize_solution(Thistlethwaite.solve(cubie))
