
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        s = s.split()
        return len(s[-1])
# leetcode submit region end(Prohibit modification and deletion)
