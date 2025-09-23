class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sx,sy = startPos
        fx,fy = homePos
        ans = 0
        if sx <= fx:
            for i in range(sx+1,fx+1):
                ans += rowCosts[i]
        else:
            i = sx-1
            while i > fx-1:
                ans += rowCosts[i]
                i -= 1

        if sy <= fy:
            for i in range(sy+1,fy+1):
                ans += colCosts[i]
        else:
            i = sy-1
            while i > fy-1:
                ans += colCosts[i]
                i -= 1
        
        return ans