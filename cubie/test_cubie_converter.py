import unittest
from unittest import TestCase

from constants.face import Face
from cubie.cubie_converter import CubieConverter
from cubie.test_cubie_util import TestCubieUtil


class TestCubieConverter(TestCase):

    @staticmethod
    def assert_conversion_passed(labels: list[int]):
        conv = CubieConverter()
        cubie = conv.convert_to_cubie(labels)
        assert cubie is not None, "cube rejected"
        return cubie[0], cubie[1]

    def test_solved_cube(self):
        labels = [Face.UP] * 9 + [Face.RIGHT] * 9 + [Face.FRONT] * 9 + [Face.DOWN] * 9 + [Face.LEFT] * 9 + [
            Face.BACK] * 9

        corners, edges = self.assert_conversion_passed(labels)

        corner_ids = [cid for cid, _ in corners]
        assert sorted(corner_ids) == list(range(8)), f"Corner IDs wrong: {corner_ids}"

        edge_ids = [eid for eid, _ in edges]
        assert sorted(edge_ids) == list(range(12)), f"Edge IDs wrong: {edge_ids}"

        corner_ori = [cori for _, cori in corners]
        assert all(ori == 0 for ori in corner_ori), f"Corners not in neutral orientation: {corner_ori}"

        edge_ori = [eori for _, eori in edges]
        assert all(ori == 0 for ori in edge_ori), f"Edge not in neutral orientation: {edge_ori}"

    def test_up_face_turned_once_clockwise(self):
        # solved cube with an Up Face clockwise turn
        labels = ([Face.UP] * 9 +
                  [Face.BACK] * 3 + [Face.RIGHT] * 6 +
                  [Face.RIGHT] * 3 + [Face.FRONT] * 6 +
                  [Face.DOWN] * 9 +
                  [Face.FRONT] * 3 + [Face.LEFT] * 6 +
                  [Face.LEFT] * 3 + [Face.BACK] * 6)

        actual = self.assert_conversion_passed(labels)

        TestCubieUtil.assert_U_clockwise_from_solved(actual)

    def test_up_face_turned_once_counterclockwise(self):
        # solved cube with an Up Face counterclockwise turn
        labels = ([Face.UP] * 9 +
                  [Face.FRONT] * 3 + [Face.RIGHT] * 6 +
                  [Face.LEFT] * 3 + [Face.FRONT] * 6 +
                  [Face.DOWN] * 9 +
                  [Face.BACK] * 3 + [Face.LEFT] * 6 +
                  [Face.RIGHT] * 3 + [Face.BACK] * 6)

        actual = self.assert_conversion_passed(labels)

        TestCubieUtil.assert_U_counterclockwise_from_solved(actual)

    def test_front_face_turned_once_clockwise(self):
        # solved cube with a Front face clockwise turn
        labels = ([Face.UP] * 6 + [Face.LEFT] * 3 +
                  ([Face.UP] + [Face.RIGHT] * 2) * 3 +
                  [Face.FRONT] * 9 +
                  [Face.RIGHT] * 3 + [Face.DOWN] * 6 +
                  ([Face.LEFT] * 2 + [Face.DOWN]) * 3 +
                  [Face.BACK] * 9)

        actual = self.assert_conversion_passed(labels)

        TestCubieUtil.assert_F_clockwise_from_solved(actual)

    def test_front_face_turned_once_counterclockwise(self):
        # solved cube with a Front face counterclockwise turn
        labels = ([Face.UP] * 6 + [Face.RIGHT] * 3 +
                  ([Face.DOWN] + [Face.RIGHT] * 2) * 3 +
                  [Face.FRONT] * 9 +
                  [Face.LEFT] * 3 + [Face.DOWN] * 6 +
                  ([Face.LEFT] * 2 + [Face.UP]) * 3 +
                  [Face.BACK] * 9)

        actual = self.assert_conversion_passed(labels)

        TestCubieUtil.assert_F_counterclockwise_from_solved(actual)

    def test_right_face_turned_once_clockwise(self):
        # solved cube with a right face clockwise turn
        labels = (([Face.UP] * 2 + [Face.FRONT]) * 3 +
                  [Face.RIGHT] * 9 +
                  ([Face.FRONT] * 2 + [Face.DOWN]) * 3 +
                  ([Face.DOWN] * 2 + [Face.BACK]) * 3 +
                  [Face.LEFT] * 9 +
                  ([Face.UP] + [Face.BACK] * 2) * 3)

        actual = self.assert_conversion_passed(labels)

        TestCubieUtil.assert_R_clockwise_from_solved(actual)

    def test_right_face_turned_once_counterclockwise(self):
        # solved cube with a right face counterclockwise turn
        labels = (([Face.UP] * 2 + [Face.BACK]) * 3 +
                  [Face.RIGHT] * 9 +
                  ([Face.FRONT] * 2 + [Face.UP]) * 3 +
                  ([Face.DOWN] * 2 + [Face.FRONT]) * 3 +
                  [Face.LEFT] * 9 +
                  ([Face.DOWN] + [Face.BACK] * 2) * 3)

        actual = self.assert_conversion_passed(labels)

        TestCubieUtil.assert_R_counterclockwise_from_solved(actual)

    def test_left_face_turned_once_clockwise(self):
        # solved cube with a left face clockwise turn
        labels = (([Face.BACK] + [Face.UP] * 2) * 3 +
                  [Face.RIGHT] * 9 +
                  ([Face.UP] + [Face.FRONT] * 2) * 3 +
                  ([Face.FRONT] + [Face.DOWN] * 2) * 3 +
                  [Face.LEFT] * 9 +
                  ([Face.BACK] * 2 + [Face.DOWN]) * 3)

        actual = self.assert_conversion_passed(labels)

        TestCubieUtil.assert_L_clockwise_from_solved(actual)

    def test_back_face_turned_once_clockwise(self):
        # solved cube with a back face clockwise turn
        labels = ([Face.RIGHT] * 3 + [Face.UP] * 6 +
                  ([Face.RIGHT] * 2 + [Face.DOWN]) * 3 +
                  [Face.FRONT] * 9 +
                  [Face.DOWN] * 6 + [Face.LEFT] * 3 +
                  ([Face.UP] + [Face.LEFT] * 2) * 3 +
                  [Face.BACK] * 9)

        actual = self.assert_conversion_passed(labels)

        TestCubieUtil.assert_B_clockwise_from_solved(actual)

    def test_down_face_turned_once_clockwise(self):
        # solved cube with a down face clockwise turn
        labels = ([Face.UP] * 9 +
                  [Face.RIGHT] * 6 + [Face.FRONT] * 3 +
                  [Face.FRONT] * 6 + [Face.LEFT] * 3 +
                  [Face.DOWN] * 9 +
                  [Face.LEFT] * 6 + [Face.BACK] * 3 +
                  [Face.BACK] * 6 + [Face.RIGHT] * 3)

        actual = self.assert_conversion_passed(labels)

        TestCubieUtil.assert_D_clockwise_from_solved(actual)

    def test_known_valid_scramble_labels(self):
        # LRR DUL BBD LUF LRU RRU DDF DFB BFU UDF FDB RLL DLR RLR BUL DFB BBU FFU
        labels = [
            # U face
            Face.LEFT, Face.RIGHT, Face.RIGHT,
            Face.DOWN, Face.UP, Face.LEFT,
            Face.BACK, Face.BACK, Face.DOWN,

            # R face
            Face.LEFT, Face.UP, Face.FRONT,
            Face.LEFT, Face.RIGHT, Face.UP,
            Face.RIGHT, Face.RIGHT, Face.UP,

            # F face
            Face.DOWN, Face.DOWN, Face.FRONT,
            Face.DOWN, Face.FRONT, Face.BACK,
            Face.BACK, Face.FRONT, Face.UP,

            # D face
            Face.UP, Face.DOWN, Face.FRONT,
            Face.FRONT, Face.DOWN, Face.BACK,
            Face.RIGHT, Face.LEFT, Face.LEFT,

            # L face
            Face.DOWN, Face.LEFT, Face.RIGHT,
            Face.RIGHT, Face.LEFT, Face.RIGHT,
            Face.BACK, Face.UP, Face.LEFT,

            # B face
            Face.DOWN, Face.FRONT, Face.BACK,
            Face.BACK, Face.BACK, Face.UP,
            Face.FRONT, Face.FRONT, Face.UP
        ]

        self.assert_conversion_passed(labels)

if __name__ == '__main__':
    unittest.main()
