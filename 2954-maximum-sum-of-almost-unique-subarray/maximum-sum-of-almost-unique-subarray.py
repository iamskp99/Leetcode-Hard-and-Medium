class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        d,som,i = {},0,0
        while i < k:
            x = nums[i]
            som += x
            if x in d:
                d[x] += 1

            else:
                d[x] = 1

            i += 1

        ans = 0
        if len(d) >= m:
            ans = max(ans,som)

        i = 0
        j = k
        while j < len(nums):
            x = nums[i]
            som -= x
            if d[x] > 1:
                d[x] -= 1

            else:
                del d[x]

            x = nums[j]
            som += x
            if x in d:
                d[x] += 1

            else:
                d[x] = 1

            if len(d) >= m:
                ans = max(ans,som)
            
            j += 1
            i += 1

        return ans