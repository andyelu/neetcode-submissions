class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren_map = {'}':'{', ')':'(', ']':'['}

        for ch in s:
            if ch in paren_map:
                if stack and stack.pop() == paren_map[ch]:
                    continue
                return False
            stack.append(ch)

        return not stack

