class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            # retrieve the initial num representing str length
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1

            length = int(length)
                
            i += 1

            str_elem = ""

            str_i = i
            while str_i < i + length:
                str_elem += s[str_i]
                str_i += 1

            i = str_i
            
            res.append(str_elem)

        return res