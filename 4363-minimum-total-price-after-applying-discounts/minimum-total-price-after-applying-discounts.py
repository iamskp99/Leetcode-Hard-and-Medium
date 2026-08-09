class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        discounts.sort(reverse=True)
        prices.sort(reverse=True)
        i,n = 0,len(prices)
        ans,j = 0,0
        while i < n:
            if j == len(discounts):
                ans += prices[i]
            else:
                ans += (prices[i]*(100-discounts[j])/100)
                j += 1
            i += 1

        return ans