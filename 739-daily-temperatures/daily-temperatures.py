class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n,stack = len(temperatures),[]
        ans = [0 for i in range(n)]
        i = n-1
        while i > -1:
            tup = (temperatures[i],i)
            if i == n-1:
                pass
            else:
                while len(stack) > 0 and stack[-1][0] <= tup[0]:
                    stack.pop()

                if len(stack) > 0:
                    ans[i] = stack[-1][-1]-i

            stack.append(tup)
            i -= 1

        return ans