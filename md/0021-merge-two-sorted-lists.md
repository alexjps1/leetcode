# 21. Merge Two Sorted Lists
by Alex JPS  
2023-03-09

https://leetcode.com/problems/merge-two-sorted-lists  
Simple 3-Step Solution with While Loop

# Intuition
Instead of creating a new linked list based on comparisons made between `list1`and `list2`, change the `next` values of existing nodes to rearrange them into a new list.

# Approach

## Step 1 - First Comparison

If `list1` or `list2` is of `None` type, it's empty. If a list is empty, return the non-empty list. If both are empty, return an empty list (i.e. `return None`). If both lists are non-empty, continue by making comparisons.

Every comparison will be between the head of each list (i.e between `list1` and `list2`). First comparison: set `head` of the merged list to the lower of `list1` and `list2`. Move the head of that lower list forward (i.e. `list1 = list1.next`), preparing the next comparison. Finally, set `index = head`. Here, `index` points to the last node moved to the merged list, but we will ultimately return `head` since it will always refer to the first node of the merged list.

## Step 2 - Loop

Use a `while list1 and list2` loop to make comparisons while both lists are still non-empty.
Because we step the heads of `list1` and `list2` forward after each comparison, a list becomes empty after all of its nodes have been included in the merged list.

Each comparison checks for the lowest of `list1.val` and `list2.val`. Recall `list1` and `list2` refer to the head of their respective linked lists, so we always comapare the lowest element of one list to the lowest of the other.

Remember, `index` gives us a handle by which we thread our way through the two given lists. We need to make sure `index` always points to the last node moved to the merged list, and we also make sure `index.next` points to the next node of the merged list.

Let's say for instance that `list1` is the lowest:
- `index.next = list1` link the next node to the end of merged list
- `list1 = list1.next` step forward the head of list #1
- `index = index.next` step forward the index of the merged list

Once the `while` loop finishes, one of the two given lists is empty. Move on to step 3.

## Step 3 - Tie Up Loose Ends

Becaues one of the two given lists is empty, the only thing left to do is take `index.next` and set it to the head of the remaining list. This links the remaining list to the merged list. All done! 

# Complexity
- Time complexity:
$$O(n)$$
Each node of list1 or list2 is observed only once.

- Space complexity:
$$O(n)$$
We do not create any new nodes.

# Code
[Click here to view code](../py/0021-merge-two-sorted-lists.py)
