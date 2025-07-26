class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        if len(nums)<=2:
            return -1
        else:
            for i in range(len(nums)):
                if nums[i]!=mini and nums[i]!=maxi:
                    return nums[i]
