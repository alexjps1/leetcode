# 13. Roman to Integer
by Alex JPS  
2023-01-28  

https://leetcode.com/problems/roman-to-integer/  
Solution with Dict and one For Loop

# Intuition
In most cases, a Roman Numeral is simply the sum of the values of its characters. The only exception is when a lower-value character is placed before a higher-value one, which indicates a subtraction (i.e. IV is V minus I).

# Approach
A simple dictionary `conv` keeps track of each character's value for easy conversion. Then, using a For Loop, we keep a running total `total` as we add the value of each character.

We also keep a `prev` variable referring to the previous value. In cases where the value of the previous character is lesser than the value of the current character, we subtract the previous value twice (once to account for us incorrectly adding that value to `total` in the previous iteration).

Note that `prev` starts with a value of 1000 since M is the largest Roman numberal, thus we will not enounter a case where M is lesser than the character succeeding it. Also, we must always assign the current character's value to `prev` once we finish adding to our running total.

# Complexity
$$O(n)$$
Linear time complexity because we perform one calculation per character in a Roman numeral.

# Code
[Click here to view code](../py/0013-roman-to-integer.py)
