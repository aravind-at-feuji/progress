class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 :
            return True
        if len(s) > len(t):
            return False
        l = 0 
        for i in range(len(t)) :
            if s[l] == t[i] :
                l += 1
            if l == len(s):
                return True
        return False