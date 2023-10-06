class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        som = sum(nums)
        n = len(nums)
        mul = target//som
        ans = mul*n
        target = target%som
        p = {0:-1}
        cur = 0
        nums = nums+nums
        n = len(nums)
        for i in range(n):
            x = nums[i]
            cur += x
            p[cur] = i

        res = 10**18
        uu = 0
        for i in range(n):
            uu += nums[i]
            gg = uu-target
            if gg in p:
                w = p[gg]
                res = min(res,i-w)

        if res == 10**18:
            return -1

        return res+ans

            