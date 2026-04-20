class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        alnum = set("qwertyuiopasdfghjklzxcvbnm1234567890")
        s = s.lower()

        while (l <= r):
            if (s[l] not in alnum):
                l += 1
                continue
            if (s[r] not in alnum):
                r -= 1
                continue
            
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1

        return True

