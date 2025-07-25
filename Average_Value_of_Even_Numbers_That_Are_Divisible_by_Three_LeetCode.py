class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sums=0
        c=0
        for i in range(len(nums)):
            if nums[i]%3==0 and nums[i]%2==0:
                sums+=nums[i]
                c+=1
        if c!=0:
            return sums//c
        return c
