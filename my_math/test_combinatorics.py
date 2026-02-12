import unittest

from my_math.combinatorics import Combinatorics


class TestCombinatorics(unittest.TestCase):
    def test_small_known_values(self):
        self.assertEqual(Combinatorics.comb(0, 0), 1)
        self.assertEqual(Combinatorics.comb(1, 0), 1)
        self.assertEqual(Combinatorics.comb(1, 1), 1)
        self.assertEqual(Combinatorics.comb(5, 0), 1)
        self.assertEqual(Combinatorics.comb(5, 1), 5)
        self.assertEqual(Combinatorics.comb(5, 2), 10)
        self.assertEqual(Combinatorics.comb(5, 3), 10)
        self.assertEqual(Combinatorics.comb(5, 4), 5)
        self.assertEqual(Combinatorics.comb(5, 5), 1)

    def test_out_of_range(self):
        self.assertEqual(Combinatorics.comb(0, 1), 0)
        self.assertEqual(Combinatorics.comb(3, 4), 0)
        self.assertEqual(Combinatorics.comb(5, -1), 0)

    def test_pascal_identity(self):
        # C(n, k) = C(n-1, k-1) + C(n-1, k)
        for n in range(1, 10):
            for k in range(1, n):
                self.assertEqual(
                    Combinatorics.comb(n, k),
                    Combinatorics.comb(n - 1, k - 1) + Combinatorics.comb(n - 1, k)
                )

    def test_ud_slice_known_values(self):
        # C(12,4) must be exactly 495
        self.assertEqual(Combinatorics.comb(12, 4), 495)

        # Edge cases used in slice ranking
        self.assertEqual(Combinatorics.comb(3, 4), 0)
        self.assertEqual(Combinatorics.comb(4, 4), 1)
        self.assertEqual(Combinatorics.comb(11, 4), 330)

    def test_lr_slice_known_values(self):
        # C(8,4) must be exactly 70
        self.assertEqual(Combinatorics.comb(8, 4), 70)

    def test_monotonic_in_n(self):
        # For fixed k, C(n,k) must increase with n
        k = 3
        prev = 0
        for n in range(k, 12):
            current = Combinatorics.comb(n, k)
            self.assertGreaterEqual(current, prev)
            prev = current

if __name__ == '__main__':
    unittest.main()
