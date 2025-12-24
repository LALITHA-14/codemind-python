class Solution:
    def countLessEqual(self, arr, x):
        #code here
        c=0
        for i in arr:
            if i<=x:
                c+=1
        return c
