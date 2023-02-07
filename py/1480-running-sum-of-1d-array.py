"""
1480. Running Sum of 1d Array
by Alex JPS
2023-02-06

https://leetcode.com/problems/running-sum-of-1d-array
Solution with One For Loop
"""

class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i == 0:
                result = [nums[i]]
            else:
                result.append(result[i-1] + nums[i])
        return result
