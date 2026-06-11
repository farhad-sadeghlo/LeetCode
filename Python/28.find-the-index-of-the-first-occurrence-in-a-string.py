#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
# @lc code=end

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    result = solution.strStr(haystack, needle)
    print(result)  # Output: 2