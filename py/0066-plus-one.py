from typing import List


# funny solution
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(j) for j in list(str(int("".join(str(i) for i in digits)) + 1))]


# solution withou string manipulation
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] > 9:
                digits[i] -= 10
                digits[i - 1] += 1
        if digits[0] == 0:
            return digits[1:]
        else:
            return digits
