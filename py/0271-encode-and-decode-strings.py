from typing import List


# my first attempt (not optimal)
class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ":"
        i = 1
        delimiter = ";"
        for s in strs:
            if delimiter in s:
                delimiter = f"{delimiter};"
                i += 1
        ans = f"{i}:{delimiter.join(strs)}"
        return ans

    def decode(self, s: str) -> List[str]:
        if s[0] == ":":
            return []
        delim_num = ""
        i = 0
        while s[i] != ":":
            delim_num = f"{delim_num}{s[i]}"
            i += 1
        delim_num = int(delim_num)
        delimiter = "".join([";"] * delim_num)
        return s[i + 1 :].split(delimiter)


# the optimal solution uses a delimiter like this "number$"
# where the number is the number of characters in the next string
# and $ marks the beginning of that string
