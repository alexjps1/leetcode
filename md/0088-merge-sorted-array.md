# Intuition
Move elements in `nums1` to the side somehow to facilitate populating that array in-place (better to avoid allocating extra space). Then, start at index 0 of `nums1` and iteratively pick the lowest number from either array.

# Approach
Transpose elements of `nums1` to the end of `nums1` to free up space at the beginning of the array to populate it. Let's call the new non-zero area at the end of `nums1` the "end zone." **In retrospect, this could be avoided by simply working from the end to the beginning of the array. Oh well.**

Then, keep 3 pointers: one for the next element of `nums1`, one for the next element of `nums2`, and one for the index in `nums1` currently being populated (the "result pointer"). At each step, populate using the lowest number of the two arrays and, when one array runs out of elements, continuously use elements from the other until the result pointer reaches the end of `nums1`.

Make sure to remove elements of `nums1` from the "end zone" as they are used to populate the final array, since the final array must ultimately use the entire `nums1` space.

# Complexity
- Time complexity: One pass through `nums1` to move elements to the end. Then, one pass through each of `nums1` and `nums2` to populate the final array (which is also `nums1`).
$$ O(2m + n) $$

- Space complexity: Does not allocate additional arrays, so just length of `nums1` and `nums2`

# Code
```python3 []
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # trivial cases
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        # move nums1 elements to the end of the list
        for idx in range(m-1, -1, -1):
            nums1[idx + n] = nums1[idx]
            nums1[idx] = None
        
        # compare nums1 and nums2 elements
        ptr_result = 0
        ptr1 = n
        ptr2 = 0
        while ptr_result < m + n:
            if ptr1 == m + n:
                # use next number from nums2
                nums1[ptr_result] = nums2[ptr2]
                ptr2 += 1
            elif ptr2 == n or nums1[ptr1] < nums2[ptr2]:
                # use next number from nums1
                nums1[ptr_result] = nums1[ptr1]
                ptr1 += 1
            else:
                # use next number from nums2
                nums1[ptr_result] = nums2[ptr2]
                ptr2 += 1
            ptr_result += 1
```
