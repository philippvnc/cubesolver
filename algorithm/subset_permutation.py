from algorithm.lehmer_permutation import LehmerPermutation

class SubsetPermutation:

    def __init__(self, subset: list[int]):
        """
        creates a new subset permutation with given subset
        :param subset: list of subset coordinates for this subset permutation
        """
        self.__subset = subset

    def encode(self, permutation: list[int]) -> int:
        """
        encodes the subset of given permutation according to lehmer permutation.
        example:
        subset : [0, 1, 2]
        permutation : [0, 1, 2, 4, 3]
        return 0 since the subset of the permutation has lehmer index 0, even though permutation has no lehmer index 0.
        :param permutation: list of numbers
        :return: lehmer index of the permutation subset
        """
        return LehmerPermutation.encode([permutation[i] for i in self.__subset])

