#
# @lc app=leetcode id=2929 lang=python3
#
# [2929] Distribute Candies Among Children II
#
from math import comb
# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = 0
        for i in range(2 ** 3):
            violators = bin(i).count('1')
            over = violators * (limit + 1)
            remaining = n - over
            if remaining < 0:
                continue
            sign = (-1) ** violators
            total += sign * comb(remaining + 3 - 1, 3 - 1)
        return total
        
# @lc code=end

