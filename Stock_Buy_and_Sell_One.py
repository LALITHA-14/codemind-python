class Solution:
    def maximumProfit(self, prices):
        # code here
        res=0
        minsofar=prices[0]
        for i in range(1,len(prices)):
            minsofar=min(minsofar,prices[i])
            res=max(res,prices[i]-minsofar)
        return res
