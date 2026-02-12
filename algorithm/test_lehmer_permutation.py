import unittest
from itertools import permutations

from algorithm.lehmer_permutation import LehmerPermutation


class TestLehmerPermutation(unittest.TestCase):
    def test_empty_permutation_is_0(self):
        perm = []
        index = LehmerPermutation().encode(perm)
        self.assertEqual(index, 0)

    def test_ordered_permutation_is_0(self):
        perm = [0, 1, 2]
        index = LehmerPermutation().encode(perm)
        self.assertEqual(index, 0)

    def test_longer_ordered_permutation_is_also_0(self):
        perm = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        index = LehmerPermutation().encode(perm)
        self.assertEqual(index, 0)

    def test_reversed_2_piece_permutation_is_1(self):
        perm = [1, 0]
        index = LehmerPermutation().encode(perm)
        self.assertEqual(index, 1)

    def test_partially_reversed_3_piece_permutation_is_2(self):
        perm = [1, 0, 2]
        index = LehmerPermutation().encode(perm)
        self.assertEqual(index, 2)

    def test_reversed_3_piece_permutation_is_5(self):
        perm = [2, 1, 0]
        index = LehmerPermutation().encode(perm)
        self.assertEqual(index, 5)

    def test_it_also_works_with_sparse_input(self):
        perm = [0, 2, 4]
        index = LehmerPermutation().encode(perm)
        self.assertEqual(index, 0)

    def test_it_also_works_with_reversed_sparse_input(self):
        perm = [4, 2, 0]
        index = LehmerPermutation().encode(perm)
        self.assertEqual(index, 5)

    def test_permutation_index_is_unique(self):
        permutation_list = list(permutations(range(4)))
        indexes = []
        for permutation in permutation_list:
            print(f"permutation {permutation}")
            indexes.append(LehmerPermutation().encode(permutation))
        print(f"indexes: {indexes}")
        self.assertEqual(len(set(indexes)), len(indexes))




if __name__ == '__main__':
    unittest.main()
