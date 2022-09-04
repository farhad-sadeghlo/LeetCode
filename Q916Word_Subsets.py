from collections import Counter
class wordSubsets:

    def __init__(self, words, strings):

        self.words = list(map(int, words.rstrip().split()))
        self.strings = list(map(int, strings.rstrip().split()))
        self.lst_words = []

    def subsets(self):

        dic = {}
        for a_string in self.strings:
            for char, num in Counter(a_string).items():
                if char not in dic.keys() or dic[char] < num:
                    dic[char] = num
        print(dic)
        for word in self.words:
            word_counts = Counter(word)
            if all(char in word_counts and num <= word_counts[char] for char, num in dic.items()):
                self.lst_words.append(word)

        return print(self.lst_words)
