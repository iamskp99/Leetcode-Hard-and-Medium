class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans,cur = 0,0
        for ele in s:
            if ele == '(':
                stack.append(cur)
                cur = 0
            else:
                if len(stack) == 0:
                    cur = 0

                else:
                    prev = stack.pop()
                    cur += (prev+1)
                    ans = max(ans,2*cur)

        return ans