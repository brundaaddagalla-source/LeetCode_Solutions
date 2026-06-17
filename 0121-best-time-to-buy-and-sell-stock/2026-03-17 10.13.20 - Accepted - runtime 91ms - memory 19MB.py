class Solution(object):
    def maxProfit(self, prices):
        # b=min(prices)
        # temp=prices[prices.index(b):]
        # s=max(temp)
        # if s==None:
        #     return 0
        # profit=s-b
        # return profit
        b=float("inf")
        profit=0
        for i in prices:
            if i<b:
                b=i
            else:
                profit=max(profit,i-b)
        return profit