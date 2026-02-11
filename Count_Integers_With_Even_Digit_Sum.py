class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            digit_sum=sum(int(d) for d in str(i))
            if i<=num and digit_sum%2==0:
                c+=1
        return c
