import unittest

from cubie.test_cubie_util import TestCubieUtil
from thistlethwaite.phase4.phase4 import Phase4


class TestPhase4Solver(unittest.TestCase):

    def test_phase_4_goal_is_true_for_solved_cube(self):
        cubie = TestCubieUtil.solved_cubie()
        solved = Phase4().phase_solved(cubie)
        self.assertEqual(solved, True)

    def test_phase_4_goal_is_false_for_unsolved_cube(self):
        cubie = ([(2, 0), (3, 0), (7, 0), (4, 0), (1, 0), (5, 0), (6, 0), (0, 0)], [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)])
        solved = Phase4().phase_solved(cubie)
        self.assertEqual(solved, False)


if __name__ == '__main__':
    unittest.main()
