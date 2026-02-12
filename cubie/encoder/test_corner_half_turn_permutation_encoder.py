import unittest

from cubie.encoder.corner_half_turn_permutation_encoder import CornerHalfTurnPermutationEncoder
from cubie.encoder.corner_permutation_parity_encoder import CornerPermutationParityEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.test_cubie_move_applier import TestCubieMoveApplier


class TestCornerHalfTurnPermutationEncoder(unittest.TestCase):

    def test_solved(self):
        """solved cube maps to corner half turn permutation of 0 (lowest value)"""
        cubie = TestCubieMoveApplier.solved_cubie()
        encoder = CornerHalfTurnPermutationEncoder()
        self.assertEqual(encoder.encode_cubie(cubie), 0)

    def test_corner_half_turn_permutation_furthest_from_solved(self):
        """cube with both corner tetrad fully reversed maps to corner half turn permutation of 575 (highest value)"""
        corners = [(7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)]
        cubie = corners, []
        encoder = CornerHalfTurnPermutationEncoder()
        self.assertEqual(encoder.encode_cubie(cubie), 575)

    def test_corner_half_turn_encoder_injective_on_g3(self):
        from itertools import permutations

        encoder = CornerHalfTurnPermutationEncoder()
        seen = set()

        for perm in permutations(range(8)):

            # enforce G3 corner conditions
            cubie = [(c, 0) for c in perm], []
            corner_tetrad = CornerTetradEncoder().encode_cubie(cubie)
            permutation_parity = CornerPermutationParityEncoder.encode_cubie(cubie)
            if not (corner_tetrad == 0 and permutation_parity == 0):
                continue

            idx = encoder.encode_cubie(cubie)

            self.assertNotIn(idx, seen, f"Collision for {perm}")
            seen.add(idx)

        self.assertEqual(len(seen), 288)


if __name__ == "__main__":
    unittest.main()
