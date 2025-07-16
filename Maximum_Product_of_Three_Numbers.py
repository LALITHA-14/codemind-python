class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],  # product of 3 largest
            nums[0] * nums[1] * nums[-1]     # product of 2 smallest and largest
        )
