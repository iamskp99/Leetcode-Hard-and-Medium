import math
class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:


        res,n = k,len(nums)
        ans = 0
        M = (10**9)+7
        for i in range(n):
            diff = nums[i]-res
            if diff < 0:
                res -= nums[i]
            else:
                som = math.ceil(diff/k)
                ans += som
                res += (k*som)
                res -= nums[i]

        def inv(n):
            return power(n, M - 2)

        def power(x, y):
            ans = 1
            while (y > 0):
                if (y % 2 == 1):
                    ans = (ans * x) % M
                y = y // 2
                x = (x * x) % M

            return ans % M

        result = ((ans)*((ans+1)%M))%M
        ans = (result*inv(2))%M
        return ans