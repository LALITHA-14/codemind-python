class Solution:
    def maxProduct(self, n: int) -> int:
        lst=[]
        while(n>0):
            digit = n%10
            lst.append(digit)
            n=n//10
        a = lst[::-1]
        maxproduct=0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                product=a[i]*a[j]
                if product>maxproduct:
                    maxproduct=product
        return maxproduct
