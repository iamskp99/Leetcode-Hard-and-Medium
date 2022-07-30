class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        d = (1+(9*n))**0.5
        limit = int((-1+d)/2)+5
        ans = 0
        for i in range(1,limit):
            som = (2*n)+i-(i**2)
            if som <= 0:
                break
                
            if (som)%(2*i) == 0:
                ans += 1
                
        return ans
        