class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float("infinity")
        res_l,res_r = 0,0
        l,r = 0,0

        # valid window -- window that has every character in t.
        # Increment r until we have a valid window or r >= len(s)
        # when r's position creates a valid window, increment 
        # l with the iteration condition of keeping valid window.
        # Then update res

        t_char_counts = {}
        for ch in t:
            t_char_counts[ch] = t_char_counts.get(ch, 0) + 1
        
        t_char_distinct = len(t_char_counts)

        win_t_chars = {}
        
        # indicates the amount of conditions we have met
        # aka, the amount of keys in the window map that have
        # a value >= to the corresponding value in the t map
        have = 0  
        
        while r < len(s):
            if s[r] in t_char_counts:
                win_t_chars[s[r]] = win_t_chars.get(s[r], 0) + 1
                if win_t_chars[s[r]] == t_char_counts[s[r]]:
                    have += 1

            # shrink window through the first t_char
            while have == t_char_distinct:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res_l = l
                    res_r = r
                if s[l] in win_t_chars:
                    win_t_chars[s[l]] -= 1
                    if win_t_chars[s[l]] < t_char_counts[s[l]]:
                        have -= 1
                l += 1
            
            r += 1

        return s[res_l:res_r+1] if min_len != float("infinity") else ""

            