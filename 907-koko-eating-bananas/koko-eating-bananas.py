import math
class Solution:
    def helper(self,piles,val):
        ans = 0
        for i in piles:
            ans += math.ceil(i/val)

        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n,k = len(piles),-1
        low,high = 1,10**18
        while low <= high:
            mid = (low+high)//2
            if self.helper(piles,mid) <= h:
                k = mid
                high = mid-1
            else:
                low = mid+1

        return k