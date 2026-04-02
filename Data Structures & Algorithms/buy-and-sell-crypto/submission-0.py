class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low sell high 
        p1 = p2 = 0 
        maxx = 0 
        while p2 < len(prices): 
            maxx = max(maxx, prices[p2] - prices[p1])
            if prices[p2] < prices[p1]: 
                p1 = p2 
            p2 = p2 + 1 
        return maxx

