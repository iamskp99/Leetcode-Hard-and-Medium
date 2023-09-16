from itertools import permutations
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        emp,pos = [],[]
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    emp.append((i,j))

                val = grid[i][j]
                while val > 1:
                    pos.append((i,j))
                    val -= 1

        l = [i for i in range(len(emp))]
        p = permutations(l)
        ans = 10**18
        for o in p:
            cnt = 0
            for g in range(len(emp)):
                e = emp[o[g]]
                c = pos[g]
                cnt += (abs(e[0]-c[0])+abs(e[1]-c[1]))

            ans = min(cnt,ans)

        return ans
