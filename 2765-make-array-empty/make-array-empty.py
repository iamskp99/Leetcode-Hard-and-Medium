class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i

        A = nums
        res = n = len(A)
        A.sort()
        for i in range(1, n):
            if pos[A[i]] < pos[A[i - 1]]:
                res += n - i
        return res