class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        d,n = {},len(nums)
        som,ans = 0,10**18
        for i in range(n):
            som += nums[i]
            d[som] = i+1
            if som == x:
                ans = min(ans,i+1)

        p = {}
        som = 0
        # print("HII",ans)
        i,cnt = n-1,0
        while i > -1:
            som += nums[i]
            cnt += 1
            p[som] = cnt
            if som == x:
                ans = min(ans,cnt)
            else:
                if x-som in d and d[x-som]-1 < i:
                    ans = min(ans,d[x-som]+cnt)
            
            i -= 1
        
        # print("HII",ans,d,p)
        som = 0
        for i in range(n):
            som += nums[i]
            if x-som in p and n-p[x-som] > i:
                ans = min(ans,p[x-som]+i+1)
        
        # print("HIII",x-som)
        return ans if ans != 10**18 else -1