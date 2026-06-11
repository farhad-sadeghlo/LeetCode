import ast
class Solution:
    def maximumWealth(self, accounts_str: str) -> int:
        maxlst = 0
        accounts = ast.literal_eval(accounts_str)
        for lst in accounts:
            maxsum = sum(lst)
            maxlst = max(maxsum, maxlst)
        return print(maxlst)