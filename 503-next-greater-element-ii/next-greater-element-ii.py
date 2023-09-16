class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        org = len(nums)
        nums = nums+nums
        stack = []
        n = len(nums)-1
        i = n
        ans = [-1 for i in range(n+1)]
        while i > -1:
            x = nums[i]
            while len(stack) > 0 and stack[-1] <= x:
                stack.pop()

            if len(stack) > 0:
                ans[i] = stack[-1]
                stack.append(x)

            else:
                stack.append(x)

            i -= 1

        return ans[0:org]                