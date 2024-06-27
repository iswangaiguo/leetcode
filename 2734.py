class Solution:
    def smallestString(self, s: str) -> str:
        t = list(s)
        for i, c in enumerate(t):
            if c == 'a':
                continue
            for j in range(i, len(t)):
                if t[j] == 'a':
                    break
                t[j] = chr(ord(t[j]) - 1)
            return ''.join(t)
        t[-1] = 'z'
        return ''.join(t)


        

if __name__ == "__main__":
    print(Solution().smallestString("cbabc"))
    print(Solution().smallestString("acbbc"))
    print(Solution().smallestString("leetcode"))
