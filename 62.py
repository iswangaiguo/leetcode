from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # @cache
        # def dfs(i, j):
        #     if i == 0 and j == 0:
        #         return 1
        #     if i < 0 or j < 0:
        #         return 0
        #     return dfs(i - 1, j) + dfs(i, j - 1)
        #
        # return dfs(m - 1, n - 1)
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]


if __name__ == "__main__":
    # print(Solution().uniquePaths(3, 7))
    # print(Solution().uniquePaths(3, 2))
    dp = [[1] * 2] + [[1] + [0] * (2 - 1) for _ in range(3 - 1)]
    print(dp)
