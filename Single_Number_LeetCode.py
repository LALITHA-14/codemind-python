from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for i in nums:
            if freq[i]%2!=0:
                return i
