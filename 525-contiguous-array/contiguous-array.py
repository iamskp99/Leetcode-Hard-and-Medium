class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}
        n = len(nums)
        som = 0
        ans = 0
        for i in range(n):
            x = nums[i]
            som += 1 if x == 1 else -1 

            if som not in d:
                d[som] = i

            else:
                ans = max(ans,i-d[som])

        return ans