class Solution:
    #Fast modular exponentiation
    def power(self,x,y):
        M = (10**9)+7
        ans = 1
        while(y>0):
            if(y%2 == 1):
                ans = (ans*x)%M
            y = y //2
            x = (x*x)%M
        return ans%M

    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        
        s = set()
        d,count,ma = {},0,0
        for i in range(len(nums)):
            x = nums[i]
            d[x] = i
        
        for i in range(len(nums)):
            x = nums[i]
            ma = max(ma,d[x])
            if ma == i:
                count += 1
        
        return self.power(2,count-1)