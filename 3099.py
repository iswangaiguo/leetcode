class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        sum = 0
        tmp = x
        while tmp:
            sum += tmp % 10
            tmp = tmp // 10
        return -1 if x % sum else sum

if __name__ == "__main__":
    print(Solution().sumOfTheDigitsOfHarshadNumber(18))
    print(Solution().sumOfTheDigitsOfHarshadNumber(23))

