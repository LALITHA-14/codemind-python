class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        duplicates=[]
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1] and (not duplicates or duplicates[-1]!=nums[i]):
                duplicates.append(nums[i])
        if duplicates:
            return True
        return False
