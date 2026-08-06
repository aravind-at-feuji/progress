
# 3345. Smallest Divisible Digit Product I
"""
You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

 

Example 1:

Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.
"""
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def product(num) :
            res = 1
            while num > 0 :
                digit = num % 10
                res *= digit
                num = num // 10
            return res
        while True :
            if product(n) % t == 0 :
                return n
            n += 1
        return -1