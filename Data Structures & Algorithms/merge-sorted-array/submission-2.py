class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # since this is a basic merge sort
        # whereas The array nums1 has a total length of (m+n), 
        # with the first m elements containing the values to be merged, 
        # and the last n elements set to 0 as placeholders.

        # iterate nums1, then compare each element of nums1 with nums2
        # then just insert the smaller element into nums1 at the correct position
        # while we push the larger element to the right
        
        # merge in reverse order
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        if m > 0:
            while m > 0:
                nums1[last] = nums1[m - 1]
                m -= 1
                last -= 1
        else:
            while n > 0:
                nums1[last] = nums2[n - 1]
                n -= 1
                last -= 1