import unittest

from algorithm.permutation_parity import PermutationParity


class TestPermutationParity(unittest.TestCase):
    def test_empty_permutation_has_0_parity(self):
        perm = []
        parity = PermutationParity.determine(perm)
        self.assertEqual(parity, 0)

    def test_ordered_permutation_has_0_parity(self):
        perm = [0, 1, 2, 3]
        parity = PermutationParity.determine(perm)
        self.assertEqual(parity, 0)

    def test_offset_ordered_permutation_has_0_parity(self):
        perm = [4, 5, 6, 7]
        parity = PermutationParity.determine(perm)
        self.assertEqual(parity, 0)

    def test_permutation_with_single_swap_has_1_parity(self):
        perm = [0, 2, 1, 3]
        parity = PermutationParity.determine(perm)
        self.assertEqual(parity, 1)

    def test_permutation_with_2_individual_swaps_has_0_parity(self):
        perm = [3, 2, 1, 0]
        parity = PermutationParity.determine(perm)
        self.assertEqual(parity, 0)

    def test_permutation_with_2_swaps_in_3_cycle_has_0_parity(self):
        perm = [0, 2, 3, 1]
        parity = PermutationParity.determine(perm)
        self.assertEqual(parity, 0)

if __name__ == '__main__':
    unittest.main()
