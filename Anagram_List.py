class anagram_list:

    def __init__(self, lst):
        self.lst = list(map(int, lst.rstrip().split()))
        self.anagrams = None

    def anagram_list(self):

        for word in self.lst:

            if sorted(word) not in self.anagrams:

                self.anagrams