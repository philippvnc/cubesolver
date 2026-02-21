from cubie.cubie_validator import CubieValidator
from robot.output.feedback import Feedback
from solver.cube_scanner import CubeScanner
from cubie.cubie_converter import CubieConverter
from solver.label_predictor import LabelPredictor
from solver.solution_executor import SolutionExecutor
from solver.solution_generator import SolutionGenerator


class CubeSolver:
    def __init__(self,
                 cube_scanner: CubeScanner,
                 solution_executor: SolutionExecutor,
                 feedback: Feedback,
                 max_retries: int = 2) -> None:
        self.cube_scanner = cube_scanner
        self.solution_executor = solution_executor
        self.max_retries = max_retries
        self.feedback = feedback

    def solve_cube(self) -> None:
        solution = self.__get_solution()
        if solution:
            self.solution_executor.execute_solution(solution)

    def __get_solution(self) -> list[int] | None:
        for scan_attempt in range(self.max_retries):
            print("scan attempt " + str(scan_attempt))
            scan = self.cube_scanner.scan()
            if not scan:
                self.feedback.fail()
                continue

            labels = LabelPredictor.get_cube_labels(scan)
            if not labels:
                self.feedback.fail()
                continue

            cubie = CubieConverter.convert_to_cubie(labels)
            if not cubie:
                self.feedback.fail()
                continue

            if not CubieValidator.valid(cubie):
                self.feedback.fail()
                continue

            solution = SolutionGenerator.generate_solution(cubie, self.feedback.show_process)
            if solution is None:
                self.feedback.fail()
                continue

            self.feedback.success()
            return solution

        print("could not find a solution after " + str(self.max_retries) + " scan attempts")
        return None
