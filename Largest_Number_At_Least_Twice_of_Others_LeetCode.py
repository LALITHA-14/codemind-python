class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_value=max(nums)
        max_index=nums.index(max_value)
        for i in nums:
            if i!=max_value and max_value<2*i:
                return -1
        return max_index
