#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(str(x) for x in digits)
        num = int(num) + 1
        return [int(x) for x in str(num)]
# @lc code=end

