
#IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        value1, value2 = 0, 0 

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                value1 = int(a[i])
            else:
                value1 = 0
            if j >= 0:
                value2 = int(b[j])
            else:
                value2 = 0

            total = value1 + value2 + carry

            result.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        return "".join(reversed(result))

#IMPORTANT!! Submit Code Region End(Do not remove this line)