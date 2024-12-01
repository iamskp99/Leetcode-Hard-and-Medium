M = (10**9)+7
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        c,d = {},{}
        ans = 0
        for i in nums:
            som = 0
            mul,mul1,mul2 = 0,0,0
            if i-1 in d:
                som = (som+d[i-1])%M
                mul1 = 0 if i-1 not in c else c[i-1]

            if i+1 in d:
                som = (som+d[i+1])%M
                mul2 = 0 if i+1 not in c else c[i+1]
            
            mul += 1
            mul = mul+mul1+mul2
            if i in c:
                c[i] += mul
            else:
                c[i] = mul
                
            # c[i] = mul
            gg = (i*mul)%M
            som = (som+gg)%M

            if i in d:
                d[i] = (d[i]+som)%M
            else:
                d[i] = som

            ans = (ans+som)%M

        return ans
