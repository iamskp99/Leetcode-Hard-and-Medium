
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            total = 0
            doubled_remainders = set()

            for j in range(i, n):
                total = (total + nums[j]) % k
                doubled_remainders.add((2 * nums[j]) % k)

                if total == 0 or total in doubled_remainders:
                    ans = max(ans, j - i + 1)

        return ans
