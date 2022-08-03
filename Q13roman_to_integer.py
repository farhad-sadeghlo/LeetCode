class roman_to_integer:

    def __init__(self, roman_num):

        self.roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9,
                          'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        self.result = 0
        self.roman_num = roman_num

    def romanToInt(self):
        i = 0
        while i < len(self.roman_num):

            if i + 1 < len(self.roman_num) and self.roman_num[i:i + 2] in self.roman_dic:

                self.result += self.roman_dic[self.roman_num[i:i + 2]]
                i += 2

            else:

                self.result += self.roman_dic[self.roman_num[i]]
                i += 1

        return print(self.result)
