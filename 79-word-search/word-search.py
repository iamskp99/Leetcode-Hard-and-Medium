class Solution:
    def rec(self,x,y,i,mat,board,n,m,word):
        if i == len(word):
            return True

        if x < 0 or y < 0 or x == n or y == m:
            return False

        if mat[x][y] == 0:
            return False

        if board[x][y] != word[i]:
            return False

        ans = False
        o = [(0,1),(0,-1),(1,0),(-1,0)]
        mat[x][y] = 0
        for ele in o:
            ans = ans | self.rec(x+ele[0],y+ele[1],i+1,mat,board,n,m,word)

        mat[x][y] = 1
        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board),len(board[0])
        mat = []
        for i in range(n):
            o = [1 for j in range(m)]
            mat.append(o)
        
        for i in range(n):
            for j in range(m):
                if self.rec(i,j,0,mat,board,n,m,word):
                    return True

        return False
