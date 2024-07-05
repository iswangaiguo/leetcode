from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            max_col = -1
            replaced_nums = []
            for j in range(m):
                if matrix[j][i] == -1:
                    replaced_nums.append(j)
                max_col = max(max_col, matrix[j][i])
            for col in replaced_nums:
                matrix[col][i] = max_col
        return matrix

        # better 
        # for j in range(len(matrix[0])):
        #   mx = max(row[j] for row in matrix)
        #   for row in matrix:
        #       if row[j] == -1:
        #           row[j] = mx
        #   return matrix

if __name__ == "__main__":
    print(Solution().modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))
    print(Solution().modifiedMatrix([[3,-1],[5,2]]))
