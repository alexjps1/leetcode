# 382. Linked List Random Node
by Alex JPS  
2023-03-10

Solution With At Most Two Passes  
https://leetcode.com/problems/linked-list-random-node/

# Intuition

First, find the length of the linked list. Then, select a random node (number in range of list length) and return that node's value.

# Approach

In the constructor `__init__`, find the length of the linked list. We keep a count `self.len` which we increment each time we step to the next node using `index = index.next`.

In `getRandom`, we use `node = random.randrange(self.len)` to select the number of a random node. We set `index = self.head` and use a `while` loop to step the index forward (as we did in the constructor) while simultaneously decrementing `node`. When `node == 0`, that means `index` has reached the selected node. Return its value with `return index.val`.

# Complexity
- Time complexity:
$$O(n)$$
Loops through entire linked list at most two whole times (exactly once in the constructor and at most one whole time in `getRandom`)

- Space complexity:
$$O(n)$$
Does not create new nodes.

# Code
[Click here to view code](../py/382-linked-list-random-node.py)
