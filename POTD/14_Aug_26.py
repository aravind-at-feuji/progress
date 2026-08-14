class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l , r = 0, 0
        ditn = {}
        res = 0
        max_occur = 0
        while r < len(s):
            char = s[r]
            ditn[char] = ditn.get(char, 0) + 1
            while l <= r and ditn[char] > 2 :
                ditn[s[l]] = ditn.get(s[l] , 0) - 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


        