class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[]
        for i in range(n+1):
            a=bin(i)[2:]
            lst.append(a.count('1'))
        return lst
