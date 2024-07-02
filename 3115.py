from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        p = 0
        q = len(nums) - 1

        def is_prime(n):
            if n == 1:
                return False
            elif n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        return False
                return True
            else:
                return False

        while not is_prime(nums[p]):
            p += 1

        while not is_prime(nums[q]):
            q -= 1
        return q - p


if __name__ == "__main__":
    print(Solution().maximumPrimeDifference([4, 2, 9, 5, 3]))
    print(Solution().maximumPrimeDifference([4, 9, 2, 8]))
