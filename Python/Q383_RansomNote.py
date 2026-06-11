# Solution without using hashmap
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, '', 1)
                ransomNote = ransomNote.replace(letter, '', 1)
            else:
                return False
        if ransomNote:
            return False
        return True
