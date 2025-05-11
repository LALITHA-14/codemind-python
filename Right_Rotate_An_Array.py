class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n # handling when k > size of array
        # reverse the entire array
        reverse(nums,0,n-1)
        # reverse the n-k array
        reverse(nums,k,n-1)
        # reverse the k array
        reverse(nums,0,k-1)
def reverse(nums,start,end):
    while start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1
