from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int],  worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        res = i = best = 0
        worker.sort()
        for w in worker:
            while i < len(jobs) and w >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            res += best
        return res

