class Solution:
    def rec(self,i):
        if i == self.n:
            return True

        if self.dp[i] != None:
            return self.dp[i]

        flag = False
        j = 0
        while j < len(self.l):
            t = self.l[j]
            if len(t) > self.n-i:
                j += 1
                continue

            else:
                if self.s[i:i+len(t)] == t:
                    flag = flag|self.rec(i+len(t))

                else:
                    pass

            j += 1

        self.dp[i] = flag
        return flag

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.n = len(s)
        self.dp = [None for ee in range(301)]
        self.l = wordDict
        self.s = s
        return self.rec(0)