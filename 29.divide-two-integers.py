#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
    #     class DivideTwoIntegers:
    # def __init__(self, dividend: int, divisor: int) -> int:
    #     self.dividend = dividend
    #     self.divisor = divisor

        max_int = 2**31 - 1
        min_int = -2**31
        if dividend == min_int and divisor == -1:
            return max_int
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiplier = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiplier <<= 1
            dividend -= temp
            quotient += multiplier
        return -quotient if negative else quotient

# if __name__ == "__main__":
#     div = DivideTwoIntegers(2**30, 1)
#     print(div.divide())  # Output: 3
# @lc code=end

