import math
class Solution:
    def rec(self,i,j,k):
        if i == self.n:
            return 1
        
        if self.dp[i][j][k] != -1:
            return self.dp[i][j][k]
        
        ans = 0
        for x in range(1,7):
            if math.gcd(j,x) == 1 and j != x and x != k:
                ans = (ans+self.rec(i+1,x,j))%self.M
                
        self.dp[i][j][k] = ans
        return ans
            
    def distinctSequences(self, n: int) -> int:
        self.dp = []
        self.n = n
        self.M = (10**9)+7
        for i in range(n):
            o = []
            for j in range(7):
                p = []
                for k in range(7):
                    p.append(-1)
                    
                o.append(p)
                
            self.dp.append(o)
            
        ans = 0
        for i in range(1,7):
            ans = (ans+self.rec(1,i,0))%self.M
            
        return ans
        