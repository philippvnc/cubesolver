from my_math.combinatorics import Combinatorics


class GroupEncoder:

    def __init__(self, possible_positions: list[int], group:list[int]):
        self.group = group
        self.n_group = len(self.group)
        self.max = Combinatorics.comb(len(possible_positions), self.n_group) - 1
        # order non group positions before group positions
        # needed to ensure meaningful 0 index
        self.positions = (
                [p for p in possible_positions if p not in self.group] +
                [p for p in possible_positions if p in self.group]
        )
        self.n_positions = len(self.positions)

    def encode(self,
               positions: list[int]) -> int:
        """
        positions: [id] the positions to be encoded
        gives int encoding reflecting how the group is positioned in relationship
        to the possible positions for the given positions using combinatorics.
        0 means all group members are positioned in their group.
        does not consider placement inside group.
        """

        index = 0 # if index does not change, none of the group members is in the group
        remaining_group_elements = self.n_group # how many members of the group are still not placed

        # start from the back
        for position_index in range(self.n_positions - 1, -1, -1):
            # get which position is in current position index
            position = self.positions[position_index]
            element = positions[position]
            # if that element belongs to given group
            if element in self.group:
                # compute index shift and add to index
                # per located element, how many ways are there
                # to place the remaining elements in the non visited positions
                index += Combinatorics.comb(position_index, remaining_group_elements)
                remaining_group_elements -= 1
                if remaining_group_elements == 0:
                    # stop once all group elements have been located
                    break

        # invert index to achieve cleaner mapping
        # 0 -> all group elements are in their group
        # self.max -> none of the group elements are in their group
        return self.max - index
