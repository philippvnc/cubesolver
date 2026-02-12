import unittest

from algorithm.group_encoder import GroupEncoder


class TestGroupEncoder(unittest.TestCase):

    def assert_encoding_equals(self, possible_positions, group, positions, expected_encoding):
        encoder = GroupEncoder(possible_positions, group)
        encoding = encoder.encode(positions)
        self.assertEqual(encoding, expected_encoding)

    def test_element_is_where_it_belongs_at_the_end(self):
        possible_positions = [0, 1]
        group = [1]
        positions_to_encode = [0, 1]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_element_is_where_it_belongs_at_the_beginning(self):
        possible_positions = [0, 1]
        group = [0]
        positions_to_encode = [0, 1]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_element_is_where_it_belongs_at_the_middle(self):
        possible_positions = [0, 1, 2]
        group = [1]
        positions_to_encode = [0, 1, 2]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_element_is_where_it_belongs_with_narrowed_possible_positions(self):
        possible_positions = [0, 1]
        group = [1]
        positions_to_encode = [0, 1, 2, 3]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_elements_are_where_they_belong_at_the_end(self):
        possible_positions = [0, 1, 2, 3, 4, 5]
        group = [4, 5]
        positions_to_encode = [0, 1, 2, 3, 4, 5]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_elements_are_where_they_belong_at_the_beginning(self):
        possible_positions = [0, 1, 2, 3, 4, 5]
        group = [0, 1]
        positions_to_encode = [0, 1, 2, 3, 4, 5]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_elements_are_where_they_belong_at_the_middle(self):
        possible_positions = [0, 1, 2, 3, 4, 5]
        group = [2, 3]
        positions_to_encode = [0, 1, 2, 3, 4, 5]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_elements_are_where_they_belong_scattered(self):
        possible_positions = [0, 1, 2, 3, 4, 5]
        group = [2, 3, 5]
        positions_to_encode = [0, 1, 2, 3, 4, 5]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_elements_are_where_they_belong_scattered_non_ordered(self):
        possible_positions = [2, 1, 3, 5, 4, 0]
        group = [1, 4, 2]
        positions_to_encode = [0, 1, 2, 3, 4, 5]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_encoding_is_invariant_to_order_in_group(self):
        possible_positions = [0, 1, 2]
        group = [0, 1]
        positions_to_encode = [0, 1, 2]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

        # swapped elements inside group should be 0 too
        positions_to_encode = [1, 0, 2]
        self.assert_encoding_equals(possible_positions, group, positions_to_encode, 0)

    def test_encoding_is_unique_but_compact_for_single_element_groups(self):
        possible_positions = [0, 1, 2, 3]
        group = [0]
        encoder = GroupEncoder(possible_positions, group)

        positions = [[0, 1, 2, 3],
                     [1, 0, 2, 3],
                     [1, 2, 0, 3],
                     [1, 3, 2, 0]]
        encodings = []
        for i in range(4):
            group_encoding = encoder.encode(positions[i])
            encodings.append(group_encoding)
        self.assertListEqual(sorted(encodings), [0, 1, 2, 3])

    def test_encoding_is_unique_but_compact_for_multi_element_group_and_element_order_is_ignored_in_and_out_of_group(self):
        possible_positions = [0, 1, 2, 3]
        group = [0, 1]
        encoder = GroupEncoder(possible_positions, group)

        encodings = []
        # all possible ways the elements could be positioned
        positions = [
            [0, 1, 2, 3],  # both in group
            [0, 1, 3, 2],  # both in group
            [1, 0, 2, 3],  # both in group
            [1, 0, 3, 2],  # both in group
            [0, 2, 1, 3],  # one element in first group pos, one in first non-group pos
            [0, 3, 1, 2],  # one element in first group pos, one in first non-group pos
            [1, 3, 0, 2],  # one element in first group pos, one in first non-group pos
            [1, 2, 0, 3],  # one element in first group pos, one in first non-group pos
            [0, 2, 3, 1],  # one element in first group pos, one in second non-group pos
            [0, 3, 2, 1],  # one element in first group pos, one in second non-group pos
            [1, 2, 3, 0],  # one element in first group pos, one in second non-group pos
            [1, 3, 2, 0],  # one element in first group pos, one in second non-group pos
            [2, 0, 1, 3],  # one element in second group pos, one in first non-group pos
            [3, 0, 1, 2],  # one element in second group pos, one in first non-group pos
            [2, 1, 0, 3],  # one element in second group pos, one in first non-group pos
            [3, 1, 0, 2],  # one element in second group pos, one in first non-group pos
            [3, 1, 2, 0],  # one element in second group pos, one in second non-group pos
            [2, 0, 3, 1],  # one element in second group pos, one in second non-group pos
            [2, 1, 3, 0],  # one element in second group pos, one in second non-group pos
            [3, 0, 2, 1],  # one element in second group pos, one in second non-group pos
            [2, 3, 0, 1],  # both out of group
            [2, 3, 1, 0],  # both out of group
            [3, 2, 0, 1],  # both out of group
            [3, 2, 1, 0],  # both out of group
        ]

        for position in positions:
            encoding = encoder.encode(position)
            encodings.append(encoding)

        # assert that no index is skipped
        self.assertEqual(sorted(set(encodings)), [0, 1, 2, 3, 4, 5])
        # assert that all 4 both in group variants encode to 0
        self.assertEqual(set(encodings[0:4]), {0})
        # assert that all 4 both out of group variants encode to 5
        self.assertEqual(set(encodings[20:24]), {5})
        # assert remaining symmetric cases map to identical encodings:
        self.assertEqual(len(set(encodings[4:8])), 1)
        self.assertEqual(len(set(encodings[8:12])), 1)
        self.assertEqual(len(set(encodings[12:16])), 1)
        self.assertEqual(len(set(encodings[16:20])), 1)



if __name__ == '__main__':
    unittest.main()
