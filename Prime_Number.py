class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):  # optimization: check up to √n
            if n % i == 0:
                return False
        return True
