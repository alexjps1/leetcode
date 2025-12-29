"""
724. Find Pivot Index
by Alex JPS
2023-02-06

https://leetcode.com/problems/find-pivot-index
Solution with Simple Calculation of Left & Right Sums
"""

class Solution:

    def pivotIndex(self, nums: list[int]) -> int:
        i = 0
        cur = nums[0]
        left = 0
        right = sum(nums[1:])
        while True:
            if left == right:
                return i
            elif i == len(nums) - 1:
                return -1
            else:
                # proceed to next case
                left += cur
                i += 1
                right -= nums[i]
                cur = nums[i]
