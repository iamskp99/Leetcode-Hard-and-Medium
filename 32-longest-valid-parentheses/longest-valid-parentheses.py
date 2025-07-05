class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        l,r = 0,0
        i,n = 0,len(s)
        while i < n:
            if s[i] == '(':
                l += 1
            else:
                r += 1

            if r > l:
                l,r = 0,0
            else:
                if r == l:
                    ans = max(ans,2*l)
                else:
                    pass
            i += 1

        # s = s[::-1]
        l,r = 0,0
        i = n-1
        while i > -1:
            if s[i] == ')':
                l += 1
            else:
                r += 1

            if r > l:
                l,r = 0,0
            else:
                if r == l:
                    ans = max(ans,2*l)
                else:
                    pass

            i -= 1

        return ans

        