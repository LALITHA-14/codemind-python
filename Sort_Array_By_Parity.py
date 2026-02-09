class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in nums:
            if i%2==0:
                lst.append(i)
        for j in nums:
            if j%2==1:
                lst.append(j)
        return lst
