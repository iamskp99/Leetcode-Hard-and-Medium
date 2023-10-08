import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
class Solution:
    def rec(self,i,rem,p):
        if i == self.n:
            if p == 0 and rem == 0:
                return 0

            return 10**9

        if rem > self.n:
            return 10**9

        if self.dp[i][rem][p] != -1:
            return self.dp[i][rem][p]

        ans1,ans2,ans3,ans4 = 10**9,10**9,10**9,10**9
        if p == 1:
            if self.s1[i] != self.s2[i]:
                ans1 = self.rec(i+1,rem,0)

            else:
                ans2 = 1+self.rec(i+1,rem,1)
                ans3 = self.x+self.rec(i+1,rem+1,0)

        else:
            if self.s1[i] != self.s2[i]:
                if rem > 0:
                    ans1 = self.rec(i+1,rem-1,0)

                ans2 = 1+self.rec(i+1,rem,1)
                ans3 = self.x+self.rec(i+1,rem+1,0)

            else:
                ans1 = self.rec(i+1,rem,p)

        self.dp[i][rem][p] = min(ans1,ans2,ans3)
        return self.dp[i][rem][p]

    def minOperations(self, s1: str, s2: str, x: int) -> int:
        self.dp = []
        self.x = x
        self.n = len(s1)
        n = self.n
        self.s1 = s1
        self.s2 = s2
        for i in range(n):
            o = []
            for j in range(n+1):
                e = []
                for j in range(2):
                    e.append(-1)

                o.append(e)

            self.dp.append(o)

        ans = self.rec(0,0,0)
        if ans >= 10**9:
            return -1

        return ans