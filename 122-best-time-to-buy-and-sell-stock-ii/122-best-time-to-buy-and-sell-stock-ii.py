class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans,n = 0,len(prices)
        for i in range(1,n):
            if prices[i] > prices[i-1]:
                ans += (prices[i]-prices[i-1])
                
        return ans