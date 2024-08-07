# dacd i = 3
# dada i = 2
# dbaa i = 1
#      i = 2
#      i = 3
# dbab i = 3
# dbac i = 3


class Solution:
    def smallestBeautifulString(self, s, k: int) -> str:
        a = ord("a")
        k += a
        s = list(map(ord, s))
        n = len(s)
        i = n - 1
        s[i] += 1
        while i < n:
            if s[i] == k:
                if i == 0:
                    return ""
                s[i] = a
                i -= 1
                s[i] += 1
            elif i and s[i] == s[i - 1] or i > 1 and s[i] == s[i - 2]:
                s[i] += 1
            else:
                i += 1
        return "".join(map(chr, s))
