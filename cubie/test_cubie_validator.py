import random
import unittest

from cubie.cubie_move_applier import CubieMoveApplier
from cubie.cubie_validator import CubieValidator
from cubie.test_cubie_move_applier import TestCubieMoveApplier
from cubie.test_cubie_util import TestCubieUtil


class TestCubieValidator(unittest.TestCase):
    def test_solved_cube_is_valid(self):
        solved = TestCubieUtil.solved_cubie()
        self.assertEqual(CubieValidator.valid(solved), True)

    def test_cube_with_single_corner_off_orientation_is_invalid(self):
        solved = TestCubieUtil.solved_cubie()
        solved[0][0] = (0, 1) # mess up corner orientation sum
        self.assertEqual(CubieValidator.valid(solved), False)

    def test_cube_with_single_edge_off_orientation_is_invalid(self):
        solved = TestCubieUtil.solved_cubie()
        solved[1][0] = (0, 1) # mess up edge orientation sum
        self.assertEqual(CubieValidator.valid(solved), False)

    def test_cube_with_different_permutation_parities_is_invalid(self):
        solved = TestCubieUtil.solved_cubie()
        solved[0][0] = (1, 0)
        solved[0][1] = (0, 0) # swap corners, but not edges
        self.assertEqual(CubieValidator.valid(solved), False)

    def test_solved_cube_stays_valid_after_random_moves(self):
        cubie = TestCubieUtil.solved_cubie()
        random.seed(1337)
        for _ in range(1000):
            cubie = CubieMoveApplier.apply(cubie, random.randint(0, 17))
            self.assertEqual(CubieValidator.valid(cubie), True)


if __name__ == '__main__':
    unittest.main()
