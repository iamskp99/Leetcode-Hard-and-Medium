class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        cur = []
        for ele in s:
            if ele == '(':
                stack.append(cur)
                cur = []

            elif ele == ')':
                cur = cur[::-1]
                if len(stack):
                    com = stack.pop()
                cur = com+cur
            else:
                cur.append(ele)

        return "".join(cur)