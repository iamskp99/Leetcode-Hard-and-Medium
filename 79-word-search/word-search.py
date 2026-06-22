class Solution:
    def rec(self,i,r,c):
        if i == len(self.word)-1:
            if self.board[r][c] == self.word[i]:
                return True
            return False

        neighbours = [(0,-1),(0,1),(-1,0),(1,0)]
        self.visited.add((r,c))
        cur_ans = False
        for x in neighbours:
            if r+x[0] < 0 or r+x[0] >= self.n:
                continue

            if c+x[1] < 0 or c+x[1] >= self.m:
                continue

            if (r+x[0],c+x[1]) in self.visited:
                continue

            if self.board[r+x[0]][c+x[1]] == self.word[i+1]:
                cur_ans = cur_ans|self.rec(i+1,r+x[0],c+x[1])

        self.visited.remove((r,c))
        return cur_ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.visited = set()
        n,m = len(self.board),len(self.board[0])
        self.n,self.m = n,m
        for i in range(n):
            for j in range(m):
                if self.board[i][j] == self.word[0]:
                    ans = self.rec(0,i,j)
                    if ans:
                        return True

        return False


# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]