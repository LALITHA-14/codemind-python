class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        pivot=-1
        # Finding the pivot element
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        # If no pivot find
        if pivot==-1:
            nums.reverse()
            return
        # Finding the rightmost element -> greater than the pivot
        for i in range(n-1,pivot,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break
        # Reversing the remaining elements in the array
        # pivot+1 -> pivot's next element, n-1 -> last element of the array
        left,right=pivot+1,n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
