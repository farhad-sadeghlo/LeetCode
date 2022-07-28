class validAnagram:

    def __init__(self, s: str, t: str) -> bool:

        self.first = s
        self.second = t

    def anagram(self):

        if len(self.first) != len(self.second):
            return False

        firstlist_condition = []
        firstlist = self.first
        secondlist = self.second

        for char in firstlist:

            if char in secondlist:

                firstlist_condition.append('True')
                firstlist.replace(char, '')
                secondlist.replace(char, '')

        return print(len(firstlist_condition) == len(firstlist))
