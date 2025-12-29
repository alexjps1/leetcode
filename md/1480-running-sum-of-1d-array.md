# 1480. Running Sum of 1d Array
by Alex JPS  
2023-02-06

https://leetcode.com/problems/running-sum-of-1d-array  
Solution with One For Loop

# Intuition
At first I thought about calculating the running sum for each index of `nums` individually, but this requires nested for loops and additional time.
It's preferable instead to just refer to the last value of our running sum list and add the value of the next element of `nums`.

# Approach
We will use a list `results` to store the running totals in such a way that `results` is a parallel list to `nums`, i.e. `results[5]` is the running total of `nums` up to index 5.
As stated in the intuition, we use a `for` loop to take each new item in `nums` and add it to the previous value of `result` to set the newest value of `result`, which is appended.
We use an `if` statement to deal with the first case, in which we initialize the `results` list with `nums[0]` as its sole item.
This also helps prevent the indexing error we would have had by trying to access the last stored value of a newly-initialized (i.e. empty) list `results`.

# Complexity
$$O(n)$$  
Linear time complexity because we perform one calculation for every element in `nums`.

# Code
[Click here to view code](../py/01480-running-sum-of-1d-array.py)
