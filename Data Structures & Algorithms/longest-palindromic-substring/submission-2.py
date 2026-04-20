class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStr = ""

        for mid in range(len(s)):
            l = mid
            r = mid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(maxStr):
                    maxStr = s[l:r+1]
                l -= 1
                r += 1

            l = mid
            r = mid+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(maxStr):
                    maxStr = s[l:r+1]
                l -= 1
                r += 1

        return maxStr
