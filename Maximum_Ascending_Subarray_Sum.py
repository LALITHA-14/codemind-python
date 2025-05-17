class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                maxsum+=nums[i]
            else:
                maxsum=nums[i]
            res=max(res,maxsum)
        return res
