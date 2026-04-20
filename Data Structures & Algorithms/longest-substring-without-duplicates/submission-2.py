class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_chars = set()

        res = 0

        l,r = 0,0

        # increment r each iteration -- check if s[r] in the set. If it is
        # we increment the l pointer until s[l] == s[r] -- while we do this
        # remove s[l] from the set

        while r < len(s):
            if s[r] in substring_chars:
                while s[l] != s[r]:
                    substring_chars.remove(s[l])
                    l += 1

                substring_chars.remove(s[l])
                l += 1
            substring_chars.add(s[r])
            r += 1

            res = max(res, r-l)
        return res