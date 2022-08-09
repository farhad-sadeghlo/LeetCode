# There is a special square room with mirrors on each of the four walls.
# Except for the southwest corner, there are receptors on each of the remaining
# corners, numbered 0, 1, and 2.
#
# The square room has walls of length p and a laser ray from the southwest corner
# first meets the east wall at a distance q from the 0th receptor.
#
# Given the two integers p and q, return the number of the receptor that the
# ray meets first.
#
# The test cases are guaranteed so that the ray will meet a receptor eventually.
#
# Example1:
#
# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
#
# Example 2:
#
# Input: p = 3, q = 1
# Output: 1

class mirror_reflection:
    def __init__(self, p, q):
        self.p = int(p)
        self.q = int(q)
    def reflection(self):
        while self.p % 2 == 0 and self.q % 2 == 0:
            self.p = self.p / 2
            self.q = self.q / 2
        if self.p % 2 == 0:
            return print(2)
        return print(0) if self.q % 2 == 0 else print(1)
