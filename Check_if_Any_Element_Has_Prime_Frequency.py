from collections import Counter
class Solution:
    def isprime(self,n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        for i in freq:
            if self.isprime(freq[i]):
                return True
        return False
