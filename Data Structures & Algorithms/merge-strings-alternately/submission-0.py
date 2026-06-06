class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr_s, ptr_l = 0, 0
        res = ""

        longer, shorter = None, None

        if len(word1) < len(word2):
            longer, shorter = word2, word1
        else:
            longer, shorter = word1, word2

        while ptr_s < len(shorter):
            res += word1[ptr_s]
            ptr_s += 1
            res += word2[ptr_l]
            ptr_l += 1

        res += longer[ptr_l:]

        return res