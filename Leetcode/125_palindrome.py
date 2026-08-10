class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""
        for i in s :
            if i.isalnum() :
                palin += i.lower()
        l , r = 0, len(palin) - 1
        while l <= r :
            if palin[l] != palin[r] :
                return False
            l += 1
            r -= 1
        return True