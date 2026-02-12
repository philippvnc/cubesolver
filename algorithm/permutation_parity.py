class PermutationParity:

    @staticmethod
    def determine(permutation: list[int]) -> int:
        """
        Compute the number of swaps needed to order the given permutation.
        :param permutation: the permutation to compute the parity of
        :return: the parity of the given permutation. 0 for even swap count, 1 for odd swap count
        """
        visited = [False] * len(permutation)
        parity = 0

        for i in range(len(permutation)):
            if visited[i]:
                continue

            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = permutation[j]
                cycle_len += 1

            if cycle_len > 0:
                parity ^= (cycle_len - 1) & 1

        return parity