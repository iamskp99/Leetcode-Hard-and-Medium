class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor,count = 0,0
        for i in range(n):
            ele = nums[i]
            if ele == 0:
                count += 1
            else:
                xor = xor^ele

        if count == n:
            return 0
        
        if xor != 0:
            return n

        return n-1
