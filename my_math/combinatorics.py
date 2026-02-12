class Combinatorics:

    # replacement for my_math.comb since it is not included in pybricks
    @staticmethod
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        res = 1
        for i in range(1, k + 1):
            res = res * (n - k + i) // i
        return res