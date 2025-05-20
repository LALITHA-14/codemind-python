class Solution:
    def thirdLargest(self,arr):
        # code here
        arr.sort(reverse=True)
        if (len(arr)<=2):
            return -1
        return arr[2]
