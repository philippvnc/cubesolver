import random
import unittest

from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder


class TestEdgeOrientationEncoder(unittest.TestCase):

    def test_to_eo_solved(self):
        """Cubie with edge orientations all 0 should produce eo of 0 (minimal value)"""
        edges = [(i, 0) for i in range(12)]
        self.assertEqual(EdgeOrientationEncoder.from_cubie_edges(edges), 0)

    def test_to_eo_max_value(self):
        """Cubie with edge orientations all 1 should produce maximal value"""
        edges = [(i, 1) for i in range(11)] + [(11, 0)]
        expected = (1 << 11) - 1
        self.assertEqual(EdgeOrientationEncoder.from_cubie_edges(edges), expected)

    def test_to_eo_single_flip(self):
        """Cubie with one edge orientation 1 should produce correct eo"""
        edges = [(i, 0) for i in range(12)]
        edges[0] = (0, 1)
        expected = 1 << 10
        self.assertEqual(EdgeOrientationEncoder.from_cubie_edges(edges), expected)

    def test_decode_eo_solved(self):
        """Edge orientation 0 should produce all edges with orientation 0"""
        eo = 0
        edge_orientations = EdgeOrientationEncoder.to_cubie_edge_orientation(eo)
        self.assertEqual(len(edge_orientations), 12)
        for ori in edge_orientations:
            self.assertEqual(ori, 0)

    def test_decode_co_arbitrary(self):
        """Check round-trip: encoding and decoding from random cubies preserves data"""
        random.seed(1337)
        for _ in range(1000):
            expected_oris = [(i, random.randint(0, 1)) for i in range(12)]
            expected_oris[11] = (11, (-sum([ori for (_, ori) in expected_oris[:-1]]) % 2))
            eo = EdgeOrientationEncoder.from_cubie_edges(expected_oris)
            actual_oris = EdgeOrientationEncoder.to_cubie_edge_orientation(eo)
            for (_, expected_ori), actual_ori in zip(expected_oris, actual_oris):
                self.assertEqual(expected_ori, actual_ori)


if __name__ == "__main__":
    unittest.main()
