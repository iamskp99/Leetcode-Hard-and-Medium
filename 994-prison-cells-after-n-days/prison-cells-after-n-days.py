class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        pcells = [0 for i in range(8)]
        cnt,ind = 0,None
        l,visited = [],{}
        while cnt < n:
            tcells = cells.copy()
            xx = tuple(cells)
            if xx in visited:
                ind = visited[xx]
                break
            for i in range(8):
                if i == 0 or i == 7:
                    tcells[i] = 0
                    continue

                if not cells[i-1]^cells[i+1]:
                    tcells[i] = 1
                else:
                    tcells[i] = 0

            l.append(cells)
            visited[tuple(cells)] = cnt
            pcells = cells.copy()
            cells = tcells
            cnt += 1

        if cnt == n:
            return cells
        
        rem = n-cnt
        o = l[ind:len(l)]
        return o[rem%len(o)]

        
