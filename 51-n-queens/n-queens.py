class Solution:
    def rec(self,i,n,ans,board,visited,row):
        if i == n:
            mat = []
            for a in range(n):
                o = []
                for b in range(n):
                    o.append(board[a][b])

                ss = "".join(o)
                mat.append(ss)

            ans.append(mat)
            return

        for j in range(n):
            if j in row or (j,i) in visited:
                continue

            row.add(j)
            ea,eb = j-1,i+1
            while ea > -1 and eb < n:
                if (ea,eb) in visited:
                    visited[(ea,eb)] += 1
                else:
                    visited[(ea,eb)] = 1
                ea -= 1
                eb += 1

            ea,eb = j+1,i+1
            while ea < n and eb < n:
                if (ea,eb) in visited:
                    visited[(ea,eb)] += 1
                else:
                    visited[(ea,eb)] = 1
                ea += 1
                eb += 1

            board[j][i] = 'Q'
            self.rec(i+1,n,ans,board,visited,row)

            ea,eb = j-1,i+1
            while ea > -1 and eb < n:
                if visited[(ea,eb)] > 1:
                    visited[(ea,eb)] -= 1
                else:
                    del visited[(ea,eb)]
                ea -= 1
                eb += 1

            ea,eb = j+1,i+1
            while ea < n and eb < n:
                if visited[(ea,eb)] > 1:
                    visited[(ea,eb)] -= 1
                else:
                    del visited[(ea,eb)]
                ea += 1
                eb += 1

            row.remove(j)
            board[j][i] = '.'

        return

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = []
        for i in range(n):
            o = []
            for j in range(n):
                o.append('.')
            board.append(o)

        self.rec(0,n,ans,board,{},set())
        return ans