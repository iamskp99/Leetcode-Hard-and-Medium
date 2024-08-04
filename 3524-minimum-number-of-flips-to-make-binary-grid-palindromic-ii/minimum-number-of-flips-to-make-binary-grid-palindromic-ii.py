class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        ans = 0
        ones,doubles = 0,0
        for i in range(n//2):
            for j in range(m//2):
                one = grid[i][j]+grid[i][m-j-1]+grid[n-i-1][j]+grid[n-i-1][m-j-1]
                ans += min(one,4-one)

            if m%2:
                c0,c1 = grid[i][m//2],grid[n-i-1][m//2]
                if c0 == c1 and c1 == 1:
                    doubles += 1

                if c0 != c1:
                    ones += 1
                    ans += 1

        if n%2:
            for i in range(m//2):
                c0,c1 = grid[n//2][i],grid[n//2][m-i-1]
                if c0 == c1 and c1 == 1:
                    doubles += 1

                if c0 != c1:
                    ones += 1
                    ans += 1

            if (n*m)%2 and grid[n//2][m//2]:
                if doubles%2:
                    if ones > 0:
                        ans += 1

                    else:
                        ans += 3

                else:
                    ans += 1

            else:
                if doubles%2 == 0:
                    pass

                else:
                    if ones == 0:
                        ans += 2

                    else:
                        pass

            return ans

        if doubles%2 == 0:
            pass

        else:
            if ones >= 1:
                pass

            else:
                ans += 2

        return ans