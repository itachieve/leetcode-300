import math
class Solution:
    """ https://leetcode.com/problems/count-primes/
    """
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False

        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        return len([x for x in primes if primes[x] is True])