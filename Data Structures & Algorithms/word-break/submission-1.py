class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [False] * (n+1)
        memo[n] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                can = i + len(word)
                if can <= n and memo[can] and word == s[i:can]:
                    memo[i] = True
        
        return memo[0]