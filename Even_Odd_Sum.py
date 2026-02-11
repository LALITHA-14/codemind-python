#User function Template for python3

class Solution:
    def EvenOddSum(self,N,Arr):
        #code here (return list)
        c=[]
        d=[]
        for i in range(len(Arr)):
            if i%2==0:
                c.append(Arr[i])
            else:
                d.append(Arr[i])
        return sum(c),sum(d)
