class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        curr, p1, p2 = 0,1,0

        for i in range(n-1, -1, -1):
            if s[i] != '0':
                curr = p1
                if i+1 < n:
                    if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
                        curr += p2
            if i != 0:
                curr, p1, p2 = 0, curr, p1
        return curr