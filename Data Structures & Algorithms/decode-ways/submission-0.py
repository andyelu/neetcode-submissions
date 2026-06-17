class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [0] * (n+1)  # substring start index to number encodings
        memo[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] != '0':
                memo[i] = memo[i+1]
                if i+1 < n and int(s[i:i+2]) <= 26:
                    memo[i] += memo[i+2]

        return memo[0]
        

        
            


