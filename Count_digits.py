#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        av=n
        count=0
        while av!=0:
            digit = av%10
            av = av//10
            if digit!=0 and n%digit==0:
                count+=1
        return count
