import ast
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = []
        nums = ast.literal_eval(nums)
        sum.append(nums[0])
        for i in range(1, len(nums)):
            sum.append(sum[i-1] + nums[i])
        return sum