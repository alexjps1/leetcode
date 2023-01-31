# 14. Longest Common Prefix
by Alex JPS  
2023-01-30  

https://leetcode.com/problems/longest-common-prefix/
Solution with Nested For Loops

# Intuition
To find the longest prefix of strings, we must incrementally check whether all of the strings have a matching substring at the beginning.
We do this until we reach a point where one or more strings differ.

# Approach
First, note that the shortest string is also the longest possible prefix.
It is therefore useful to find the length of the shortest string so we can halt the program if it ever reaches a prefix of that length.
We use a simple `for` loop that starts with `strs[0]` as `shortest` and makes comparisons with other items of `strs` until the shortest string's length is found.

Next, we begin with an empty `prefix` string which we'll incrementally add to.
We use a `for` loop that iterates up to length of the shortest string, using `i` as an index for which character to check in each string.
The nested `for` loop goes through each string and makes sure the character at index `i` in each string matches `strs[0]`.
It was arbitrary to choose `strs[0]` as the standard to which all other strings are compared; choosing any string from `strs` would achieve the same effect since we are checking that they are identical so far.
If we find a mismatch, we return the `prefix` we have so far.
Otherwise, once all strings are determined to match, we add the character at index `i` to our prefix and continue to the next iteration of the outer `for` loop.
This loop continues until a mismatch or until we reach the longest possible prefix.

# Complexity
$$O(n)$$
Linear time complexity because we perform same number of calculations on each element of `strs` in the worst case.

# Code
[Click here to view code](../py/14-longest-common-prefix.py)