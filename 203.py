from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
    # 单调栈
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2*n):
            while stack and nums[i % n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return res
if __name__ == "__main__":
    print(Solution().nextGreaterElements([1,2,1]))
    print(Solution().nextGreaterElements([1,2,3,4,3]))
