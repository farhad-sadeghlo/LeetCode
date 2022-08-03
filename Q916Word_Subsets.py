class wordSubsets:

    def __init__(self, words, chars):

        self.words = words.replace("]", "").replace("[", "").replace('"', '').split(',')
        self.chars = chars.replace("]", "").replace("[", "").replace('"', '').split(',')
        self.lst_words = []

    def subsets(self):

        self.lst_words = [word for word in self.words if all(char in word for char in self.chars)]

        return print(self.lst_words)
 