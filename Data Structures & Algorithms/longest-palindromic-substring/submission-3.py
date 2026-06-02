class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res_idx, res_len = 0, 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > res_len:
                        res_len = j-i+1
                        res_idx = i
        
        return s[res_idx:res_idx + res_len]