class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res=0
        minsofar=prices[0]
        for i in range(1,len(prices)):
            minsofar=min(minsofar,prices[i])
            res=max(res,prices[i]-minsofar)
        return res
