class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = len(num)
        while num[n - 1] == "0":
            n -= 1
        return num[:n]


if __name__ == "__main__":
    ans = Solution().removeTrailingZeros("51230100")
    ans = Solution().removeTrailingZeros("123")
    print(ans)
