class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        p = [0 for i in range(n+1)]
        for i in range(n):
            p[i+1] = p[i]+(nums[i]%modulo == k)

        d = {}
        ans = 0
        for i in range(n+1):
            j = p[i]-k
            if j%modulo in d:
                ans += d[j%modulo]

            if p[i]%modulo in d:
                d[p[i]%modulo] += 1

            else:
                d[p[i]%modulo] = 1

        return ans