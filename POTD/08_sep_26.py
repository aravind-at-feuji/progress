class Solution:
    def countCommas(self, n: int) -> int:
        s = str(n)

        if len(s) < 4 :
            return 0
        return 1 + (n - 1000)
        