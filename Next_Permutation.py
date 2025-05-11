class Solution:
    def nextPermutation(self, arr):
        # code here
        n=len(arr)
        pivot=-1
        # for finding pivot
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                pivot=i
                break
        # if no pivot is present
        if pivot==-1:
            arr.reverse()
            return
        # find the rightmost element and swapping
        for i in range(n-1,pivot,-1):
            if arr[i]>arr[pivot]:
                arr[i],arr[pivot]=arr[pivot],arr[i]
                break
        # reversing the leftout array elements
        left,right=pivot+1,n-1 # pivot+1-next element after the pivot, (n-1)-last element of the array
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        
                        
