import numpy as np
from collections import defaultdict

class validAnagram:

    def __init__(self):

        self.first, self.second = map(str, input('please type in your words: ').strip().split())

    def anagram(self):

        if sorted(self.first) == sorted(self.second):
            return print(True)
        else:
            return print(False)
