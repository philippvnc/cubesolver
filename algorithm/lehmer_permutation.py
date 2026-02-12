class LehmerPermutation:

    @staticmethod
    def encode(permutation: list[int]) -> int:
        """
        implements a lehmer encoding of permutation
        :param permutation: the permutation to compute the unique index of
        :return: the unique index of given permutation
        """
        index = 0
        factor = 1
        n = len(permutation)

        for i in range(n - 1, -1, -1):
            count = 0
            for j in range(i + 1, n):
                if permutation[j] < permutation[i]:
                    count += 1
            index += count * factor
            factor *= (n - i)

        return index
