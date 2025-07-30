#User function Template for python3

class Solution:
    def firstRepChar(self, s):
        # code here
        c=[]
        for i in s:
            if i in c:
                return i
            c.append(i)
        return -1
