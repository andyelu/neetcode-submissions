class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n:1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                dp[i] = 0
                return 0
            curr_enc = dfs(i+1)
            if i < n-1:
                if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
                    curr_enc += dfs(i+2)
            dp[i] = curr_enc
            return curr_enc
        return dfs(0)