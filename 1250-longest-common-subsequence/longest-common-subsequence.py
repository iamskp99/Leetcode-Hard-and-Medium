class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i = len(text1)
        j = len(text2)
        dp = []
        for e1 in range(i):
            o = [-1 for e2 in range(j)]
            dp.append(o)
        # print(dp)
        return self.lcs(text1,i-1,text2,j-1, dp)
    
    def lcs(self,text1,index1,text2,index2, dp):
            if index1 == -1 or index2 == -1:
                return 0
            if(dp[index1][index2] == -1):
                if(text1[index1] == text2[index2]):
                    dp[index1][index2] = 1 + self.lcs(text1,index1-1,text2,index2-1, dp)
                else:
                    dp[index1][index2] = max(self.lcs(text1,index1-1,text2,index2, dp), self.lcs(text1,index1,text2,index2-1, dp))
            return dp[index1][index2]