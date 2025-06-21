class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix),len(matrix[0])
        exception_flag = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 0:
                    continue
                else:
                    if i == 0:
                        exception_flag = 1
                        matrix[0][j] = 0
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        # print(matrix)
        for i in range(1,n):
            flag = 1 if matrix[i][0] == 0 else 0
            if flag:
                for j in range(1,m):
                    matrix[i][j] = 0

        # print(matrix)
        for i in range(m):
            flag = 1 if matrix[0][i] == 0 else 0
            if flag:
                for j in range(1,n):
                    matrix[j][i] = 0

        if exception_flag:
            for i in range(m):
                matrix[0][i] = 0

        return