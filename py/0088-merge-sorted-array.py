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
