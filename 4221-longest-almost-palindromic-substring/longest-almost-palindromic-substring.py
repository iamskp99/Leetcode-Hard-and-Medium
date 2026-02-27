class Solution:
    def rec(self,s,i,j,flag):
        if i == -1 or j == self.n:
            if flag:
                return 0
            elif i != -1 or j != self.n:
                return 1
            return -1*(10**18)

        if i == j:
            return 1+self.rec(s,i-1,j+1,flag)
        
        if s[i] == s[j]:
            return 2+self.rec(s,i-1,j+1,flag)
        else:
            if flag:
                return 0
            else:
                return 1+max(self.rec(s,i-1,j,1),self.rec(s,i,j+1,1))
    
    def almostPalindromic(self, s: str) -> int:
        ans = 2
        self.n = len(s)
        for i in range(self.n):
            ans = max(ans,self.rec(s,i,i,0),self.rec(s,i,i+1,0))
        return ans
        