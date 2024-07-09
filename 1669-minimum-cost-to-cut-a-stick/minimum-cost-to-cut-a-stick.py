class Solution:
    def rec(self,start,end):
        if start == end or end == start+1:
            return 0

        if self.dp[start][end] != -1:
            return self.dp[start][end]

        ans = 10**18
        for i in range(start+1,end):
            cnt = (self.cuts[end]-self.cuts[start])+self.rec(start,i)+self.rec(i,end)
            ans = min(ans,cnt)

        self.dp[start][end] = ans
        return ans


    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0]+cuts+[n]
        cuts.sort()
        self.cuts = cuts
        self.dp = []
        for i in range(103):
            o = [-1 for j in range(103)]
            self.dp.append(o)

        return self.rec(0,len(self.cuts)-1)