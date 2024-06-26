class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1:
            gg = matrix[0].count(0)
            if gg > 0:
                for i in range(len(matrix[0])):
                    matrix[0][i] = 0

            return matrix

        if len(matrix[0]) == 1:
            gg = 0
            for i in range(len(matrix)):
                if matrix[i][0] == 0:
                    gg += 1

            if gg > 0:
                for i in range(len(matrix)):
                    matrix[i][0] = 0

            return matrix

        n,m = len(matrix),len(matrix[0])
        flag,gflag = 0,0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        flag = 1

                    else:
                        matrix[i][0] = 0

                    if j == 0:
                        gflag = 1

                    else:
                        matrix[0][j] = 0

        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(1,m):
                    matrix[i][j] = 0

        for j in range(1,m):
            if matrix[0][j] == 0:
                for i in range(1,n):
                    matrix[i][j] = 0

        if flag:
            for i in range(m):
                matrix[0][i] = 0

        if gflag:
            for i in range(n):
                matrix[i][0] = 0

        return matrix

