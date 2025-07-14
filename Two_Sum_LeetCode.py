class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sums=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sums=nums[i]+nums[j]
                if sums==target:
                    return i,j
