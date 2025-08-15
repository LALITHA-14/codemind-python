class Solution:
    def findExtra(self,a,b):
        #add code here
        for i in range(len(b)):
            if a[i]!=b[i]:
                return i
        return len(a)-1
