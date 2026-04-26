class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        mele = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mele = max(grid[i][j],mele)

        mbit,s = len(bin(mele)[2:]),set()
        i = mbit
        ans = 0
        while i > -1:
            cur = True
            for e1 in range(len(grid)):
                cc = False
                for e2 in range(len(grid[0])):
                    sflag = False
                    for item in s:
                        if (2**item)&grid[e1][e2]:
                            sflag = True
                            break

                    if sflag:
                        continue

                    if not grid[e1][e2]&(2**i):
                        cc = True

                if not cc:
                    cur = False

            if cur:
                s.add(i)
            else:
                ans = ans|(2**i)

            i -= 1

        return ans