class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window -- track frequency of each character
        # window is valid if size - max_freq <= k

        # max_freq should NOT be adjusted as we increment l pointer
        # this was my initial oversight. We don't care about decrementing
        # this because our result wants a maximized max_freq. Decrementing
        # this will be extra work that won't get us to our goal quicker

        l,r = 0,0
        char_freq = {}
        res = 0
        max_freq = 0

        while r < len(s):
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1
            max_freq = max(max_freq, char_freq[s[r]])

            # increment l, remove counts along the way
            while r-l+1 - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1
                    
            res = max(res, r-l+1)
            r += 1
        
        return res
                

                

