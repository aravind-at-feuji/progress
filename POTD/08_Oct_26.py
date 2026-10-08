class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        if len(s) == 0 :
            return ""
        res = ""
        sub = ""
        op = 0
        for ch in s :
            if ch == '(' :
                op += 1
            else :
                op -= 1
            sub += ch
            if op == 0 and len(sub) >= 2:
                res += sub[1:-1]
                sub = ""
        
        return res

        