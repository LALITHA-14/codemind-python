#User function template for Python

class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        n=len(arr)
        if n==0:
            return 0
        i=0
        for j in range(1,n):
            if arr[j]!=arr[i]:
                i+=1
                arr[i]=arr[j]
        return i+1
