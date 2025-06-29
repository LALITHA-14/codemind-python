from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        result = [i for i in nums if freq[i]%2!=0]
        return result
