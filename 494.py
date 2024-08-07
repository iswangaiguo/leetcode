from typing import List
from functools import cache

# p q
# p + q = s
# p - q = t
# p = (s + t) / 2
# q = (s - t) / 2


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2 == 0:
            return 0
        m = s // 2

        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])

        return dfs(len(nums) - 1, m)
