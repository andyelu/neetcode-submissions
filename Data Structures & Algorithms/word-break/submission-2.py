class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                can = i + len(word)
                if can <= n and s[i:can] == word and dp[can]:
                    dp[i] = True

        return dp[0]