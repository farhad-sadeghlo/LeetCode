import ast
class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        num = ast.literal_eval(str(num))
        while num > 0:
            if (num % 2 == 0):
                num = num / 2
            else:
                num = num - 1
            counter = counter + 1
        return counter