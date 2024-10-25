class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        visited = set()
        n = len(dominoes)
        ans = ['.' for i in range(n)]
        prev = -1
        stack = []
        for i in range(n):
            if dominoes[i] == 'L':
                ans[i] = 'L'
                if prev != -1:
                    a = prev
                    b = i
                    a += 1
                    b -= 1
                    while a <= b:
                        if a == b:
                            visited.add(a)

                        else:
                            visited.add(a)
                            visited.add(b)
                            ans[a],ans[b] = 'R','L'

                        a += 1
                        b -= 1

                else:
                    while len(stack) > 0:
                        ind = stack.pop()

                        visited.add(ind)
                        ans[ind] = 'L'

                prev = -1
                stack = []

            elif dominoes[i] == 'R':
                ans[i] = 'R'
                stack = []
                prev = i

            else:
                stack.append(i)

        i = n-1
        stack = []
        while i > -1:
            x = dominoes[i]
            if x == 'R':
                while len(stack) > 0:
                    ele = stack.pop()
                    if ele in visited:
                        break

                    ans[ele] = 'R'

            elif x == 'L':
                stack = []

            else:
                stack.append(i)

            i -= 1

        return "".join(ans)

                

                        