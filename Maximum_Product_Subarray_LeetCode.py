class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currmin=nums[0]
        currmax=nums[0]
        maxprod=nums[0]
        for i in range(1,len(nums)):
            temp=max(nums[i],currmax*nums[i],currmin*nums[i])
            currmin=min(nums[i],currmax*nums[i],currmin*nums[i])
            currmax=temp
            maxprod=max(maxprod,currmax)
        return maxprod
