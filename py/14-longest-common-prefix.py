"""
14. Longest Common Prefix
by Alex JPS
2023-01-30

https://leetcode.com/problems/longest-common-prefix
Solution with Nested For Loops
"""

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # get shortest string (longest possible prefix)
        shortest = len(strs[0])
        for string in strs:
            if len(string) < shortest:
                shortest = len(string)
        # Check for matching prefix
        prefix = ""
        for i in range(shortest):
            for string in strs:
                if string[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix