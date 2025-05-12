class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        candidate1, candidate2=None,None
        count1, count2=0,0
        for i in nums:
            if i==candidate1:
                count1+=1
            elif i==candidate2:
                count2+=1
            elif count1==0:
                candidate1,count1=i,1
            elif count2==0:
                candidate2,count2=i,1
            else:
                count1-=1
                count2-=1
        # Second pass
        result=[]
        n=len(nums)
        if (nums.count(candidate1))>n//3:
            result.append(candidate1)
        if  candidate1!=candidate2 and (nums.count(candidate2))>n//3:
            result.append(candidate2)
        return sorted(nums)
        
