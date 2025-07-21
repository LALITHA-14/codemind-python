class Solution:
    from collections import Counter
    def sumOfUnique(self, nums: List[int]) -> int:
        sums=0
        freq=Counter(nums)
        for i in freq:
            if freq[i]==1:
               sums+=i
        return sums
