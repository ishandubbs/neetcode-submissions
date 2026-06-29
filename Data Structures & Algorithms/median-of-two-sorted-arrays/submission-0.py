class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            # swap the two arrays
            A, B = B, A
        # log(min(n, m))
        left = 0
        right = len(A) - 1
        while True:
            i = (left + right) // 2 #A
            j = half - i - 2 #B

            Aleft = A[i] if i >= 0 else float("-infinity") #out of bounds
            Aright = A[i + 1]if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity") #out of bounds
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1