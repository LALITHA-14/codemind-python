#User function Template for python3


class Solution:
    def findMissing(self,a,b):
    # code here
        b1=set(b)
        lst=[]
        for i in a:
            if i not in b1:
                lst.append(i)
        return lst
