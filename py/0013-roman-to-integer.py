"""
13. Roman to Integer
by Alex JPS
2023-01-28

https://leetcode.com/problems/roman-to-integer/
Solution with Dict and one For Loop
"""

class Solution:

    def romanToInt(self, s: str) -> int:
        """Convert Roman numeral str to int"""
        conv = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev = 1000
        total = 0
        for char in s:
            if prev < conv[char]:
                total -= 2*prev
            total += conv[char]
            prev = conv[char]
        return total