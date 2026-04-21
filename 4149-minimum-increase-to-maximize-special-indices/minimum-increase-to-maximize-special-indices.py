import sys
sys.setrecursionlimit(10**5)
class Solution:
    def rec(self,i,flag):
        if i == self.n or i == self.n-1:
            return 0
        
        if self.dp[i][flag] != -1:
            return self.dp[i][flag]
        
        cur = 10**18
        if self.nums[i] > self.nums[i-1] and self.nums[i] > self.nums[i+1]:
            cur = self.rec(i+2,flag)
        else:
            cur = (max(self.nums[i-1],self.nums[i+1])-self.nums[i]+1)
            cur = cur+self.rec(i+2,flag)

        if flag:
            pass
        else:
            cur = min(cur,self.rec(i+1,1))

        self.dp[i][flag] = cur
        return cur
        

    def minIncrease(self, nums: List[int]) -> int:
        # Rule : Only increase until the element becomes 
        # strictly greater.
        n = len(nums)
        self.nums = nums
        self.n = n
        self.dp = []
        for i in range(n):
            o = []
            for j in range(2):
                o.append(-1)
                o.append(-1)
            self.dp.append(o)

        ans = 0
        if n%2:
            for i in range(1,n-1,2):
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    pass
                else:
                    ans += (max(nums[i-1],nums[i+1])-nums[i]+1)

        else:
            # print(self.dp[0][0],"OO")
            ans = self.rec(1,0)
        return ans
