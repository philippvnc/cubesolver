import unittest

from algorithm.subset_permutation import SubsetPermutation


class TestSubsetPermutation(unittest.TestCase):

    def test_full_ordered_reversed_subset(self):
        subset_permutation = SubsetPermutation([3, 2, 1, 0])
        index = subset_permutation.encode([3, 2, 1, 0])
        self.assertEqual(index, 0)

    def test_full_ordered_subset(self):
        subset_permutation = SubsetPermutation([0, 1, 2, 3])
        index = subset_permutation.encode([0, 1, 2, 3])
        self.assertEqual(index, 0)

    def test_full_non_ordered_subset(self):
        subset_permutation = SubsetPermutation([0, 1])
        index = subset_permutation.encode([1, 0])
        self.assertEqual(index, 1)

    def test_full_non_ordered_permutation(self):
        subset_permutation = SubsetPermutation([1, 0])
        index = subset_permutation.encode([0, 1])
        self.assertEqual(index, 1)

    def test_ordered_subset_with_ordered_permutation(self):
        subset_permutation = SubsetPermutation([1, 2])
        index = subset_permutation.encode([0, 1, 2, 3])
        self.assertEqual(index, 0)

    def test_ordered_subset_with_non_ordered_permutation_outside_of_subset(self):
        subset_permutation = SubsetPermutation([1, 2])
        index = subset_permutation.encode([3, 1, 2, 0])
        self.assertEqual(index, 0)

    def test_ordered_subset_with_non_ordered_permutation_outside_of_subset_but_flipped(self):
        subset_permutation = SubsetPermutation([2, 1])
        index = subset_permutation.encode([3, 2, 1, 0])
        self.assertEqual(index, 0)

    def test_sparsely_indexed_subset(self):
        subset_permutation = SubsetPermutation([1, 5, 7])
        index = subset_permutation.encode([0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(index, 0)
        index = subset_permutation.encode([2, 1, 6, 4, 3, 5, 2, 7])
        self.assertEqual(index, 0)
        index = subset_permutation.encode([0, 5, 2, 3, 4, 1, 6, 7])
        self.assertEqual(index, 2)
        index = subset_permutation.encode([0, 7, 2, 3, 4, 5, 6, 1])
        self.assertEqual(index, 5)

    def test_relative_order_collision_example(self):
        subset = [0, 2, 5, 7]
        sp = SubsetPermutation(subset)

        # Two distinct permutations
        perm1 = [7, 1, 5, 3, 4, 2, 6, 0]
        perm2 = [6, 1, 4, 3, 2, 0, 7, 5]

        self.assertNotEqual(perm1, perm2)

        idx1 = sp.encode(perm1)
        idx2 = sp.encode(perm2)

        self.assertNotEqual(
            idx1,
            idx2,
            "Collision due to missing normalization"
        )


if __name__ == "__main__":
    unittest.main()
