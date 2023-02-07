# 724. Find Pivot Index
by Alex JPS  
2023-02-06

https://leetcode.com/problems/find-pivot-index  
Solution with Simple Calculation of Left & Right Sums

# Intuition
Say we're iterating through every index of `nums`.
Notice that when we move from one index to the next, `nums[previous index]` is added to the left sum and `nums[new index]` is subtracted from the right sum.
This observation helps us avoid re-doing the summation of the `nums` items left and right of the current index every time.

# Approach
We define `i` the current index, `cur` the value of `nums` at `i`, `left` the sum of items of `nums` with index <`i`, and `right` the sum of items of `nums` with index >`i`.
We initialize these variables with values appropriate for index 0, from which we will begin iterating using and a `while` loop.

We use `while True` since the loop only needs to stop when a value is to be returned.
We use an `if` statement to check if `left` is equal to `right`, the condition under which the pivot index is found; here we return the current index `i`.
Otherwise, if `i` equals the final index of `nums`, we return `-1` to indicate that there no pivot point was found through our iteration.
If none of these conditions apply, it is time to move to the next index.
We apply the logic outlined in the Intuition section to correctly adjust the values of `left` and `right` without requiring a summation of the elements of `nums` indexed lesser than and grater than `i` respectively.
The loop is ready for its next iteration.

# Complexity
$$O(n)$$
Linear time complexity because we perform the same number of calculations in each iteration of our loop.

# Code
[Click here to view code](../py/724-find-pivot-index.py)
