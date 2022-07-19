class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = 10**18
        ans = -1
        for i in prices:
            mi = min(i,mi)
            ans = max(ans,i-mi)
            
        return ans
            