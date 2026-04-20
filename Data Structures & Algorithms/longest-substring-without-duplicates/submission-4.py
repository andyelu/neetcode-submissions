class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_chars = {}

        res = 0

        l,r = 0,0

        # increment r each iteration -- check if s[r] in the set. If it is
        # we increment the l pointer until s[l] == s[r] -- while we do this
        # remove s[l] from the set

        # instead of using a set, we could use a hashmap to map char to index,
        # which will make the iteration logic a lil cleaner

        while r < len(s):
            if s[r] in substring_chars:
                # remember not to have substring_chars[s[r]] as the loop condition
                # as it will be evaluated each iteration
                new_pos = substring_chars[s[r]] + 1
                while l < new_pos: 
                    # along the way, clear the mappings that become obsolete
                    substring_chars.pop(s[l])
                    l += 1

            substring_chars[s[r]] = r
            r += 1

            res = max(res, r-l)
        return res